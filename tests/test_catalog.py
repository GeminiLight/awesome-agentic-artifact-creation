import sys
import re
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
    markdown_text,
    render_readme,
)
from build_catalog import (  # noqa: E402
    derive_papers,
    derive_survey_membership,
    load_audit,
    render_papers,
    render_survey_membership,
)
from catalog_analysis import build_chart_outputs, compute_analysis  # noqa: E402
from venue_registry import load_venues  # noqa: E402


class CatalogTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.taxonomy = load_taxonomy()
        cls.venues = load_venues()
        cls.audit = load_audit()
        cls.papers = load_papers(taxonomy=cls.taxonomy, venues=cls.venues)

    def test_audit_covers_current_candidate_set(self):
        self.assertEqual(len(self.audit), 323)
        self.assertEqual(
            Counter(row["original_role"] for row in self.audit),
            {"system": 242, "benchmark": 29, "supporting": 52},
        )
        self.assertEqual(
            Counter(row["audit_verdict"] for row in self.audit),
            {
                "include_system": 254,
                "include_benchmark": 33,
                "pending_full_text": 19,
                "exclude": 17,
            },
        )

    def test_public_catalog_is_derived_from_audit(self):
        self.assertEqual(len(self.papers), 257)
        self.assertEqual(
            Counter(paper["entry_kind"] for paper in self.papers),
            {"system": 229, "benchmark": 28},
        )
        self.assertEqual(
            (ROOT / "data" / "papers.csv").read_text(encoding="utf-8"),
            render_papers(derive_papers(self.audit, self.venues)),
        )

    def test_survey_membership_is_derived_from_public_views(self):
        membership = derive_survey_membership(self.papers)
        self.assertEqual(len(membership), 257)
        self.assertEqual(
            Counter(
                (row["artifact_view"], row["application_view"])
                for row in membership
            ),
            {
                ("true", "true"): 220,
                ("true", "false"): 30,
                ("false", "true"): 7,
            },
        )
        self.assertEqual(
            (ROOT / "data" / "survey_membership.csv").read_text(
                encoding="utf-8"
            ),
            render_survey_membership(membership),
        )

    def test_published_entries_use_archival_links(self):
        published = [row for row in self.audit if row["type"] == "published"]
        self.assertTrue(published)
        self.assertTrue(
            all("arxiv.org" not in row["link"].casefold() for row in published)
        )

    def test_venue_registry_normalizes_catalog_sources(self):
        self.assertEqual(len(self.venues), 61)
        used_venue_ids = {row["venue_id"] for row in self.audit}
        self.assertEqual(len(used_venue_ids), 60)
        self.assertEqual(
            set(self.venues) - used_venue_ids,
            {"wacv"},
        )
        self.assertTrue(
            all(row["venue_id"] in self.venues for row in self.audit)
        )
        held_venues = {
            "asme_idetc_cie",
            "acl_findings",
            "acl_system_demos",
            "cc",
            "cikm",
            "coling",
            "digital_discovery",
            "ease",
            "emnlp_findings",
            "emnlp_system_demos",
            "fdg",
            "ieee_cog",
            "ieee_tlt",
            "iccc",
            "ismir",
            "learning_at_scale",
            "semeval",
            "wacv_workshops",
        }
        self.assertEqual(
            {
                venue_id
                for venue_id, venue in self.venues.items()
                if venue["catalog_status"] == "hold"
            },
            held_venues,
        )
        self.assertTrue(
            all(
                self.venues[paper["venue_id"]]["catalog_status"] == "include"
                for paper in self.papers
            )
        )
        for paper in self.papers:
            venue = self.venues[paper["venue_id"]]
            self.assertEqual(paper["venue_display_name"], venue["display_name"])
            self.assertEqual(paper["venue_full_name"], venue["full_name"])
            self.assertEqual(paper["venue_kind"], venue["venue_kind"])
            self.assertEqual(
                paper["parent_venue_id"], venue["parent_venue_id"]
            )
        self.assertTrue(
            all(
                not any(char.isdigit() for char in venue["display_name"])
                for venue in self.venues.values()
            )
        )
        audit_by_key = {row["bib_key"]: row for row in self.audit}
        self.assertEqual(audit_by_key["Text_BookWorld2025"]["venue_id"], "acl")
        self.assertEqual(
            audit_by_key["DataViz_LightVA2024"]["venue_id"],
            "ieee_tvcg",
        )
        self.assertEqual(
            audit_by_key["D3_EZBlender2026"]["venue_id"],
            "wacv_workshops",
        )

    def test_anthology_tracks_are_not_mislabeled_as_main_conference(self):
        expected_tracks = {
            r"\.findings-acl\.": "acl_findings",
            r"\.findings-emnlp\.": "emnlp_findings",
            r"\.acl-demo\.": "acl_system_demos",
            r"\.emnlp-demos\.": "emnlp_system_demos",
        }
        for row in self.audit:
            for pattern, venue_id in expected_tracks.items():
                if re.search(pattern, row["link"]):
                    self.assertEqual(row["venue_id"], venue_id, row["bib_key"])

    def test_main_track_refresh_is_synchronized(self):
        expected_venues = {
            "Video_PhyT2V2025": "cvpr",
            "Image_UniEditI2026": "cvpr",
            "Image_MultiTurnConsistent2025": "iccv",
            "Image_Idea2Img2024": "eccv",
            "D3_DreamScene3602024": "eccv",
            "D3_ChatEdit3D2024": "eccv",
            "Code_MapCoder2024": "acl",
            "D3_SceneGenAgent2025": "acl",
            "DataViz_AMACE2025": "emnlp",
            "Code_CodeTree2025": "naacl",
            "Image_CultureTRIP2025": "naacl",
            "Text_MCQGSRefine2025": "naacl",
            "Animation_LogoMotion2025": "chi",
            "Game_DreamGarden2025": "chi",
            "DataViz_DataFormulator2_2025": "chi",
            "Image_APPO2026": "chi",
        }
        audit_by_key = {row["bib_key"]: row for row in self.audit}
        public_by_key = {row["bib_key"]: row for row in self.papers}
        for bib_key, venue_id in expected_venues.items():
            self.assertEqual(audit_by_key[bib_key]["venue_id"], venue_id)
            self.assertIn(bib_key, public_by_key)

        self.assertEqual(audit_by_key["Video_VISTA2025"]["venue_id"], "cvpr")
        self.assertEqual(audit_by_key["Video_VISTA2025"]["year"], "2026")
        self.assertEqual(audit_by_key["Game_RPGAgent2026"]["venue_id"], "chi")
        self.assertEqual(
            audit_by_key["Game_RPGAgent2026"]["audit_verdict"],
            "pending_full_text",
        )
        self.assertNotIn("Game_RPGAgent2026", public_by_key)
        for bib_key in (
            "Slide_DeepPresenter2026",
            "Video_SCMAPR2026",
            "Code_DocAgent2025",
        ):
            self.assertEqual(
                self.venues[audit_by_key[bib_key]["venue_id"]]["catalog_status"],
                "hold",
            )
            self.assertNotIn(bib_key, public_by_key)

    def test_autodesign_is_synchronized(self):
        audit_by_key = {row["bib_key"]: row for row in self.audit}
        public_by_key = {row["bib_key"]: row for row in self.papers}
        row = audit_by_key["Poster_AutoDesign2026"]
        self.assertEqual(row["venue_id"], "arxiv")
        self.assertEqual(row["audit_verdict"], "include_system")
        self.assertEqual(row["evidence_basis"], "full_text")
        self.assertEqual(
            (
                row["artifact_family"],
                row["artifact_type"],
                row["artifact_subtype"],
                row["application_domain"],
            ),
            (
                "2D Visual Artifacts",
                "Visual Documents",
                "Posters",
                "Scientific Research",
            ),
        )
        self.assertIn("Poster_AutoDesign2026", public_by_key)

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
                "Code_VisionRefine2026",
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
                "Report_LateralReader2026",
                "Text_AutoDocumentEditing2025",
                "Video_RLVideoEditing2023",
                "Image_DualAgentSketching2024",
                "Text_MetricalPoetry2025",
            },
        )
        for paper in self.papers:
            self.assertEqual(paper["name"], audit_names[paper["bib_key"]])

    def test_artifact_family_distribution(self):
        self.assertEqual(
            Counter(paper["artifact_family"] for paper in self.papers),
            {
                "Textual Artifacts": 35,
                "2D Visual Artifacts": 61,
                "Audio Artifacts": 11,
                "Video Artifacts": 34,
                "Spatial Artifacts": 35,
                "Behavioral Artifacts": 74,
                "": 7,
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
                "Textual Artifacts",
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
        for key in (
            "Audio_AudioRAGPlus2026",
            "Audio_LVASAgent2025",
            "Audio_WavCraft2024",
        ):
            self.assertEqual(
                (
                    papers[key]["artifact_family"],
                    papers[key]["artifact_type"],
                    papers[key]["artifact_subtype"],
                ),
                ("Audio Artifacts", "", ""),
            )

    def test_application_classification_is_optional_and_independent(self):
        papers = {paper["bib_key"]: paper for paper in self.papers}
        self.assertEqual(
            sum(bool(paper["application_domain"]) for paper in self.papers),
            227,
        )
        self.assertEqual(
            papers["Poster_Paper2Poster2025"]["application_domain"],
            "Scientific Research",
        )
        self.assertEqual(
            papers["Text_ComedyClub2026"]["application_domain"],
            "Creative Production",
        )
        self.assertTrue(
            all(not paper["application_subdomain"] for paper in self.papers)
        )
        self.assertEqual(
            sum(bool(row["application_domain"]) for row in self.audit),
            286,
        )

    def test_chapter_five_supporting_import_is_audited(self):
        supporting = {
            row["bib_key"]: row
            for row in self.audit
            if row["original_role"] == "supporting"
        }
        self.assertEqual(len(supporting), 52)
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
            "Engineering Design",
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

    def test_taxonomy_uses_current_manuscript_labels(self):
        self.assertEqual(
            [family["name"] for family in self.taxonomy["artifact_families"]],
            [
                "Textual Artifacts",
                "2D Visual Artifacts",
                "Audio Artifacts",
                "Video Artifacts",
                "Spatial Artifacts",
                "Behavioral Artifacts",
            ],
        )
        self.assertEqual(
            [domain["name"] for domain in self.taxonomy["application_domains"]],
            [
                "Creative Production",
                "Brand Communication",
                "Educational Support",
                "Professional Work",
                "Scientific Research",
                "Engineering Design",
            ],
        )
        self.assertEqual(
            {
                family["name"]: {
                    artifact_type["name"]: artifact_type["subtypes"]
                    for artifact_type in family["types"]
                }
                for family in self.taxonomy["artifact_families"]
            },
            {
                "Textual Artifacts": {
                    "Creative Writing": ["Narratives", "Performative Texts"],
                    "Professional Documents": [
                        "Informational Reports",
                        "Functional Documents",
                    ],
                    "Scholarly Manuscripts": [],
                },
                "2D Visual Artifacts": {
                    "Data Visualizations": [],
                    "Illustrative Graphics": ["Images", "Diagrams"],
                    "Visual Documents": ["Posters", "Presentations"],
                },
                "Audio Artifacts": {"Music": [], "Spoken Audio": []},
                "Video Artifacts": {
                    "Expository Videos": [],
                    "Narrative Videos": [],
                    "Video Editing and Repair": [],
                },
                "Spatial Artifacts": {
                    "3D Assets": ["Visual Assets", "Parametric Models"],
                    "3D Scenes": ["Spatial Worlds", "Engineered Models"],
                },
                "Behavioral Artifacts": {
                    "Software Systems": [
                        "Software Repositories",
                        "Web Applications",
                        "Games",
                    ],
                    "Simulation Models": [
                        "Virtual World Simulators",
                        "Physical World Models",
                    ],
                },
            },
        )

    def test_catalog_analysis_follows_survey_scope(self):
        rendered = render_readme(self.papers, self.taxonomy)
        scope_position = rendered.index("## Survey Scope")
        analysis_position = rendered.index("## Catalog Analysis")
        content_position = rendered.index("## Content")
        self.assertLess(scope_position, analysis_position)
        self.assertLess(analysis_position, content_position)
        self.assertNotIn("## Catalog at a glance", rendered)
        self.assertIn(
            'src="visualization/artifact-taxonomy-composition.svg"', rendered
        )
        self.assertIn('src="visualization/family-trends.svg"', rendered)
        self.assertIn(
            'src="visualization/artifact-application-matrix.svg"', rendered
        )
        self.assertIn(
            "**Multimodal & Audio:** ACM MM, IEEE TMM, and ICASSP.", rendered
        )
        self.assertIn(
            "**Data Mining and Information Retrieval:** KDD, The Web Conference, "
            "SIGIR,\n  SIGMOD, VLDB, and TKDE.",
            rendered,
        )
        self.assertIn(
            "**Systems & Hardware:** DATE, DAC, and ICCAD.", rendered
        )
        self.assertIn("monitored by this survey include:", rendered)
        self.assertIn("**Interdisciplinary & General Science:**", rendered)
        self.assertIn("Nature Machine\n  Intelligence", rendered)
        self.assertIn("Nature Computational Science", rendered)
        self.assertNotIn("**Interdisciplinary Research:**", rendered)
        self.assertNotIn("**Audio:**", rendered)
        self.assertNotIn("ISMIR", rendered[: rendered.index("## Catalog Analysis")])
        self.assertNotIn("**Audio and Interdisciplinary Research:**", rendered)
        self.assertNotIn("*Sources: generated", rendered)

    def test_header_badges_are_generated_from_catalog(self):
        rendered = render_readme(self.papers, self.taxonomy)
        self.assertNotIn("<!-- catalog-badges -->", rendered)
        self.assertIn(
            "https://agentic-creation.github.io/", rendered
        )
        self.assertIn("https://arxiv.org/abs/2608.28122", rendered)
        self.assertIn('alt="Survey paper — arXiv"', rendered)
        self.assertNotIn("Survey paper — Coming soon", rendered)
        self.assertNotIn(
            "https://github.com/GeminiLight/agentic-creation-survey",
            rendered,
        )
        self.assertNotIn(
            "geminilight.github.io/awesome-agentic-artifact-creation/", rendered
        )
        self.assertIn('src="assets/badge-website.svg" height="56"', rendered)
        self.assertIn('src="assets/badge-paper.svg" height="56"', rendered)
        self.assertIn("Papers-257-4C9D96", rendered)
        self.assertIn("Systems-229-55A2D5", rendered)
        self.assertIn("Benchmarks-28-957CC3", rendered)
        self.assertIn("Venues-36-D58B68", rendered)
        self.assertIn(
            "github/last-commit/GeminiLight/"
            "awesome-agentic-artifact-creation/main",
            rendered,
        )
        first_badge_row = rendered[
            rendered.index("  <p>\n    <a") : rendered.index(
                "  </p>", rendered.index("  <p>\n    <a")
            )
        ]
        self.assertIn("badge-website.svg", first_badge_row)
        self.assertIn("badge-paper.svg", first_badge_row)
        self.assertNotIn("Papers-257", first_badge_row)

        paper_badge = (ROOT / "assets" / "badge-paper.svg").read_text(
            encoding="utf-8"
        )
        self.assertIn("arXiv 2608.28122", paper_badge)
        self.assertNotIn("Coming soon", paper_badge)
        badge_block = rendered[
            rendered.index("  <p>\n    <a") : rendered.index(
                "</div>", rendered.index("  <p>\n    <a")
            )
        ]
        self.assertNotIn(">\n      <img", badge_block)
        self.assertNotIn("</a>\n    </a>", badge_block)

    def test_header_framework_uses_latest_pdf_export(self):
        rendered = render_readme(self.papers, self.taxonomy)
        self.assertIn(
            'href="assets/fig2-construction-process.pdf"', rendered
        )
        self.assertIn(
            'src="assets/fig2-construction-process.png"', rendered
        )

    def test_header_uses_a_theme_aware_brand_logo(self):
        rendered = render_readme(self.papers, self.taxonomy)
        self.assertIn("<picture>", rendered)
        title_index = rendered.index("<h1>Awesome Agentic Artifact Creation</h1>")
        logo_index = rendered.index("<picture>")

        self.assertLess(logo_index, title_index)
        self.assertIn(
            'media="(prefers-color-scheme: dark)"', rendered[:title_index]
        )
        self.assertIn(
            'srcset="site/assets/logo-mark-dark.svg"', rendered[:title_index]
        )
        self.assertIn(
            'src="site/assets/logo-mark.svg"', rendered[:title_index]
        )
        self.assertIn('alt="Agentic Creation"', rendered[:title_index])
        self.assertIn('width="150"', rendered[:title_index])

    def test_license_footer_closes_generated_readme(self):
        rendered = render_readme(self.papers, self.taxonomy)
        self.assertEqual(rendered.count("## License"), 1)
        self.assertTrue(rendered.rstrip().endswith("third-party works."))
        self.assertIn("[CC BY 4.0](LICENSE)", rendered)

    def test_catalog_analysis_metrics(self):
        analysis = compute_analysis(self.papers, self.taxonomy)
        self.assertEqual(analysis.total, 257)
        self.assertEqual(analysis.artifact_classified, 250)
        self.assertEqual(analysis.application_classified, 227)
        self.assertEqual(analysis.dual_classified, 220)
        self.assertEqual(analysis.artifact_only, 30)
        self.assertEqual(analysis.application_only, 7)
        self.assertEqual(analysis.named_systems, 218)
        self.assertEqual(analysis.system_count, 229)
        self.assertEqual(analysis.source_count, 36)
        self.assertEqual(
            [(item.year, item.total) for item in analysis.by_year],
            [(2023, 4), (2024, 28), (2025, 94), (2026, 124)],
        )
        self.assertEqual(analysis.family_counts, (35, 61, 11, 34, 35, 74))
        self.assertEqual(
            analysis.family_type_counts,
            (
                (8, 21, 6),
                (10, 35, 15, 1),
                (5, 0, 6),
                (7, 17, 7, 3),
                (12, 23),
                (63, 11),
            ),
        )
        self.assertEqual(analysis.application_counts, (87, 7, 9, 26, 46, 52))
        self.assertEqual(
            analysis.top_pairs[:3],
            (
                ("Behavioral Artifacts", "Engineering Design", 30),
                ("Video Artifacts", "Creative Production", 25),
                ("Spatial Artifacts", "Engineering Design", 20),
            ),
        )

    def test_generated_visualizations_are_current(self):
        outputs = build_chart_outputs(self.papers, self.taxonomy)
        self.assertEqual(len(outputs), 3)
        for path, expected in outputs.items():
            self.assertEqual(path.read_text(encoding="utf-8"), expected)
            self.assertIn("<svg", expected)
            self.assertIn("color-scheme: light", expected)
            self.assertIn("--background: #FFFFFF", expected)
            self.assertNotIn("prefers-color-scheme: dark", expected)
            for color in (
                "#4C9D96",
                "#66ADD0",
                "#718DCA",
                "#9380C1",
                "#B777A7",
                "#D89368",
            ):
                self.assertIn(color, expected)
            self.assertIn('role="img"', expected)
        family_chart = next(
            content
            for path, content in outputs.items()
            if path.name == "family-trends.svg"
        )
        self.assertIn("Artifact-family paper counts over time", family_chart)
        self.assertNotIn("Share within artifact-classified papers", family_chart)
        composition_chart = next(
            content
            for path, content in outputs.items()
            if path.name == "artifact-taxonomy-composition.svg"
        )
        self.assertIn("Artifact taxonomy composition", composition_chart)
        self.assertIn("Application-only", composition_chart)
        self.assertIn("Family-level", composition_chart)

    def test_application_view_reindexes_all_classified_papers(self):
        rendered = render_readme(self.papers, self.taxonomy)
        self.assertIn(
            '<a href="#application-centered-view">🎯 Application-centered View</a>',
            rendered,
        )
        self.assertIn("## [🎯 Application-centered View](#content)", rendered)
        self.assertNotIn("Application-only and Cross-artifact Work", rendered)
        for domain in self.taxonomy["application_domains"]:
            self.assertIn(f"### [{domain['name']}](#content)", rendered)
        for paper in self.papers:
            expected_occurrences = int(bool(paper["artifact_family"])) + int(
                bool(paper["application_domain"])
            )
            rendered_title = f"**{markdown_text(paper['title'])}**"
            self.assertEqual(
                rendered.count(rendered_title),
                expected_occurrences,
                paper["bib_key"],
            )

    def test_paper_metadata_uses_github_native_format(self):
        rendered = render_readme(self.papers, self.taxonomy)
        self.assertIn(
            "ACL, 2025. [Published](https://aclanthology.org/2025.acl-long.773/) "
            "· [Code](https://github.com/alienet1109/BookWorld) · `System` "
            "· `📦 Textual Artifacts` · `🎯 Creative Production`",
            rendered,
        )
        self.assertIn(
            "arXiv, 2025. [Preprint](https://arxiv.org/abs/2509.13677) "
            "· `System` · `📦 Textual Artifacts`",
            rendered,
        )
        self.assertIn(
            "arXiv, 2025. [Preprint](https://arxiv.org/abs/2511.17906) "
            "· `System` · `🎯 Creative Production`",
            rendered,
        )
        self.assertIn(
            "CHI, 2025. "
            "[Published](https://doi.org/10.1145/3706598.3714233) · "
            "`System` · `📦 Behavioral Artifacts` · `🎯 Creative Production`",
            rendered,
        )
        self.assertNotIn("Findings of ACL,", rendered)
        self.assertNotIn("ACL System Demonstrations,", rendered)
        self.assertNotIn("application: `", rendered)
        self.assertNotIn("**System**", rendered)
        self.assertNotIn("**Benchmark**", rendered)

    def test_content_index_uses_three_columns(self):
        rendered = render_readme(self.papers, self.taxonomy)
        self.assertIn(
            '<tr><th colspan="3"><a href="#artifact-centered-view">'
            "📦 Artifact-centered View</a></th></tr>",
            rendered,
        )
        self.assertIn("## [📦 Artifact-centered View](#content)", rendered)
        self.assertIn('<a id="artifact-centered-view"></a>', rendered)
        self.assertIn("### [Textual Artifacts](#content)", rendered)
        self.assertIn("#### [Creative Writing](#content)", rendered)
        self.assertIn("##### [Narratives](#content)", rendered)
        self.assertNotIn("\n## [Textual Artifacts](#content)\n", rendered)
        self.assertIn("## [🎯 Application-centered View](#content)", rendered)
        self.assertIn('<a id="application-centered-view"></a>', rendered)
        self.assertIn(
            '<tr><th colspan="3"><a href="#application-centered-view">',
            rendered,
        )
        self.assertNotIn('<th colspan="2">', rendered)

    def test_generated_readme_is_current(self):
        self.assertEqual(
            README_PATH.read_text(encoding="utf-8"),
            render_readme(self.papers, self.taxonomy),
        )


if __name__ == "__main__":
    unittest.main()
