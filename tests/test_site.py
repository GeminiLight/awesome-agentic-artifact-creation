import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from build_site import build_payload, build_site  # noqa: E402


class SiteBuildTests(unittest.TestCase):
    def test_payload_counts_reconcile(self) -> None:
        payload = build_payload()
        papers = payload["papers"]
        summary = payload["summary"]

        self.assertEqual(summary["total"], len(papers))
        self.assertEqual(
            summary["total"], summary["systems"] + summary["benchmarks"]
        )
        self.assertEqual(
            summary["total"], sum(year["count"] for year in payload["years"])
        )
        self.assertEqual(6, len(payload["families"]))
        self.assertEqual(6, len(payload["applications"]))
        self.assertEqual(
            len(papers), len({paper["bib_key"] for paper in papers})
        )

    def test_site_contains_runtime_assets_and_catalog(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            self.assertTrue((output / "index.html").is_file())
            self.assertTrue((output / "assets" / "styles.css").is_file())
            self.assertTrue((output / "assets" / "app.js").is_file())
            self.assertTrue((output / "assets" / "charts.js").is_file())
            self.assertTrue((output / "assets" / "logo-mark.svg").is_file())
            self.assertTrue((output / "favicon.svg").is_file())
            self.assertTrue((output / ".nojekyll").is_file())
            index = (output / "index.html").read_text(encoding="utf-8")
            self.assertIn('src="assets/charts.js"', index)
            self.assertNotIn('src="visualization/', index)

            payload = json.loads(
                (output / "data" / "catalog.json").read_text(encoding="utf-8")
            )
            self.assertEqual(payload["summary"]["total"], len(payload["papers"]))


if __name__ == "__main__":
    unittest.main()
