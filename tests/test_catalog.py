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
        self.assertEqual(len(self.audit), 206)
        self.assertEqual(
            Counter(row["original_role"] for row in self.audit),
            {"system": 147, "benchmark": 9, "supporting": 50},
        )
        self.assertEqual(
            Counter(row["audit_verdict"] for row in self.audit),
            {
                "include_system": 162,
                "include_benchmark": 15,
                "pending_full_text": 9,
                "exclude": 20,
            },
        )

    def test_public_catalog_is_derived_from_audit(self):
        self.assertEqual(len(self.papers), 177)
        self.assertEqual(
            Counter(paper["entry_kind"] for paper in self.papers),
            {"system": 162, "benchmark": 15},
        )
        self.assertEqual(
            (ROOT / "data" / "papers.csv").read_text(encoding="utf-8"),
            render_papers(derive_papers(self.audit)),
        )

    def test_names_are_populated_and_propagated(self):
        audit_names = {row["bib_key"]: row["name"] for row in self.audit}
        self.assertTrue(all(audit_names.values()))
        self.assertEqual(audit_names["Image_AutoFigureEdit2026"], "AutoFigure-Edit")
        self.assertEqual(audit_names["Game_VGameGym2025"], "V-GameGym")
        self.assertEqual(audit_names["Text_PersonasToPlot2026"], "MAGNET")
        self.assertEqual(audit_names["Video_BeyondE2E2026"], "LASEV")
        self.assertEqual(audit_names["Game_ZeroCode3D2025"], "UniGen")
        self.assertEqual(
            {key for key, name in audit_names.items() if name == "N/A"},
            {
                "Report_DeepResearchAgent2026",
                "DataVis_MultiAgent2025",
                "Audio_AudioRAGPlus2026",
                "D3_Agentic3DSceneGen2025",
                "CAD_FreeCADLLM2025",
                "Chu2026_AgenticWorldModeling",
                "Data_ReconceptualizingSmartMicroscopy2025",
                "Edu_CourseSyllabus2025",
                "Education_AgenticEducational2025",
                "Hardware_EDA2025",
                "Laboratory_AutonomousLaboratory2026",
                "Simulation_CodingAgentWorldSimulator2026",
                "Simulation_SelfReflection2026",
                "SoftArch_LLM2026",
                "Text_GoodStories2025",
            },
        )
        for paper in self.papers:
            self.assertEqual(paper["name"], audit_names[paper["bib_key"]])

    def test_artifact_family_distribution(self):
        self.assertEqual(
            Counter(paper["artifact_family"] for paper in self.papers),
            {
                "Text and Document Artifacts": 32,
                "2D Visual Artifacts": 45,
                "Music and Audio Artifacts": 9,
                "Video and Animation Artifacts": 27,
                "3D and Spatial Artifacts": 23,
                "Software and Executable Artifacts": 35,
                "": 6,
            },
        )

    def test_artifact_hierarchy_is_split_from_legacy_groups(self):
        papers = {paper["bib_key"]: paper for paper in self.papers}
        self.assertEqual(
            (
                papers["Text_ComedyClub2026"]["artifact_family"],
                papers["Text_ComedyClub2026"]["artifact_type"],
                papers["Text_ComedyClub2026"]["artifact_subtype"],
            ),
            (
                "Text and Document Artifacts",
                "Creative Writing",
                "Performative Texts",
            ),
        )
        self.assertEqual(
            (
                papers["Poster_Paper2Poster2025"]["artifact_type"],
                papers["Poster_Paper2Poster2025"]["artifact_subtype"],
            ),
            ("Visual Documents", "Posters"),
        )
        self.assertEqual(
            (
                papers["CAD_ArtisanCAD2026"]["artifact_type"],
                papers["CAD_ArtisanCAD2026"]["artifact_subtype"],
            ),
            ("3D Assets", "Parametric Models"),
        )

    def test_application_classification_is_optional_and_independent(self):
        papers = {paper["bib_key"]: paper for paper in self.papers}
        self.assertEqual(
            sum(bool(paper["application_domain"]) for paper in self.papers),
            53,
        )
        self.assertEqual(
            papers["Poster_Paper2Poster2025"]["application_domain"],
            "Scientific Research and Communication",
        )
        self.assertEqual(papers["Text_ComedyClub2026"]["application_domain"], "")
        self.assertTrue(
            all(not paper["application_subdomain"] for paper in self.papers)
        )
        self.assertEqual(
            sum(bool(row["application_domain"]) for row in self.audit),
            72,
        )

    def test_chapter_five_supporting_import_is_audited(self):
        supporting = {
            row["bib_key"]: row
            for row in self.audit
            if row["original_role"] == "supporting"
        }
        self.assertEqual(len(supporting), 50)
        self.assertEqual(
            supporting["CAD_SPADA2026"]["audit_verdict"],
            "include_system",
        )
        self.assertEqual(
            supporting["Data_DataJournalistAgent2026"]["audit_verdict"],
            "pending_full_text",
        )
        self.assertEqual(
            supporting["Chu2026_AgenticWorldModeling"]["audit_verdict"],
            "exclude",
        )
        self.assertEqual(
            supporting["Text_NewsAgent2026"]["audit_verdict"],
            "include_benchmark",
        )
        self.assertEqual(
            supporting["Game_Orchid2025"]["link"],
            "https://doi.org/10.1145/3698061.3726906",
        )
        self.assertEqual(
            supporting["Sci_AgenticTCAD2025"]["application_domain"],
            "Scientific Research and Communication",
        )

    def test_heading_anchors_are_unique(self):
        names = [
            family["name"] for family in self.taxonomy["artifact_families"]
        ]
        names.extend(
            artifact_type["name"]
            for family in self.taxonomy["artifact_families"]
            for artifact_type in family["types"]
        )
        names.extend(
            subtype
            for family in self.taxonomy["artifact_families"]
            for artifact_type in family["types"]
            for subtype in artifact_type["subtypes"]
        )
        names.extend(
            domain["name"] for domain in self.taxonomy["application_domains"]
        )
        anchors = [heading_anchor(name) for name in names]
        self.assertEqual(len(anchors), len(set(anchors)))

    def test_generated_readme_is_current(self):
        self.assertEqual(
            README_PATH.read_text(encoding="utf-8"),
            render_readme(self.papers, self.taxonomy),
        )


if __name__ == "__main__":
    unittest.main()
