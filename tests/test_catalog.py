import sys
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from generate_readme import (  # noqa: E402
    README_PATH,
    heading_anchor,
    load_papers,
    load_taxonomy,
    render_readme,
)
from build_catalog import derive_papers, load_audit, render_papers  # noqa: E402


class CatalogTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.taxonomy = load_taxonomy()
        cls.audit = load_audit()
        cls.papers = load_papers(taxonomy=cls.taxonomy)

    def test_audit_covers_current_candidate_set(self):
        self.assertEqual(len(self.audit), 156)
        self.assertEqual(
            Counter(row["original_role"] for row in self.audit),
            {"system": 147, "benchmark": 9},
        )
        self.assertEqual(
            Counter(row["audit_verdict"] for row in self.audit),
            {
                "include_system": 133,
                "include_benchmark": 11,
                "pending_full_text": 7,
                "exclude": 5,
            },
        )

    def test_public_catalog_is_derived_from_audit(self):
        self.assertEqual(len(self.papers), 144)
        self.assertEqual(
            Counter(paper["entry_kind"] for paper in self.papers),
            {"system": 133, "benchmark": 11},
        )
        self.assertEqual(
            (ROOT / "data" / "papers.csv").read_text(encoding="utf-8"),
            render_papers(derive_papers(self.audit)),
        )

    def test_artifact_family_distribution(self):
        self.assertEqual(
            Counter(paper["section"] for paper in self.papers),
            {
                "Text and Document Artifacts": 23,
                "2D Visual Artifacts": 42,
                "Music and Audio Artifacts": 9,
                "Video and Animation Artifacts": 26,
                "3D and Spatial Artifacts": 21,
                "Software and Executable Artifacts": 23,
            },
        )

    def test_taxonomy_paths_are_fully_populated(self):
        populated = {(paper["section"], paper["group"]) for paper in self.papers}
        expected = {
            (section["name"], group)
            for section in self.taxonomy
            for group in section["groups"]
        }
        self.assertEqual(populated, expected)

    def test_heading_anchors_are_unique(self):
        names = [section["name"] for section in self.taxonomy]
        names.extend(group for section in self.taxonomy for group in section["groups"])
        anchors = [heading_anchor(name) for name in names]
        self.assertEqual(len(anchors), len(set(anchors)))

    def test_generated_readme_is_current(self):
        self.assertEqual(
            README_PATH.read_text(encoding="utf-8"),
            render_readme(self.papers, self.taxonomy),
        )


if __name__ == "__main__":
    unittest.main()
