import json
import re
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
        publication_venues = payload["publication_venues"]
        self.assertEqual(
            summary["publication_venue_chart_total"],
            sum(venue["count"] for venue in publication_venues),
        )
        self.assertLessEqual(
            summary["publication_venue_chart_total"], summary["published"]
        )
        self.assertEqual(
            len(publication_venues),
            len({venue["name"] for venue in publication_venues}),
        )
        self.assertNotIn("arXiv", {venue["name"] for venue in publication_venues})
        self.assertTrue(all(venue["domain"] for venue in publication_venues))
        self.assertGreaterEqual(
            len({venue["domain"] for venue in publication_venues}), 8
        )

    def test_date_is_omitted_only_from_the_publication_venue_treemap(self) -> None:
        payload = build_payload()
        publication_venues = {
            venue["name"]: venue["count"]
            for venue in payload["publication_venues"]
        }

        self.assertTrue(
            any(
                paper["venue_display_name"] == "DATE"
                for paper in payload["papers"]
            )
        )
        self.assertNotIn("DATE", publication_venues)
        self.assertEqual(
            payload["summary"]["publication_venue_chart_total"],
            sum(publication_venues.values()),
        )

    def test_venue_treemap_shares_use_the_displayed_venue_total(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            charts = (output / "assets" / "charts.js").read_text(
                encoding="utf-8"
            )

            self.assertIn(
                "catalog.summary.publication_venue_chart_total", charts
            )

    def test_site_contains_runtime_assets_and_catalog(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            self.assertTrue((output / "index.html").is_file())
            self.assertTrue((output / "assets" / "styles.css").is_file())
            self.assertTrue((output / "assets" / "app.js").is_file())
            self.assertTrue((output / "assets" / "charts.js").is_file())
            self.assertTrue((output / "assets" / "construction-loop.js").is_file())
            self.assertTrue(
                (output / "assets" / "fig2-construction-process.png").is_file()
            )
            self.assertTrue(
                (output / "assets" / "fig2-construction-process.pdf").is_file()
            )
            self.assertTrue((output / "assets" / "logo-mark.svg").is_file())
            self.assertTrue(
                (output / "assets" / "logo-mark-dark.svg").is_file()
            )
            self.assertTrue((output / "favicon.svg").is_file())
            self.assertTrue((output / "favicon-dark.svg").is_file())
            self.assertTrue((output / ".nojekyll").is_file())
            index = (output / "index.html").read_text(encoding="utf-8")
            styles = (output / "assets" / "styles.css").read_text(
                encoding="utf-8"
            )
            logo = (output / "assets" / "logo-mark.svg").read_text(
                encoding="utf-8"
            )
            dark_logo = (output / "assets" / "logo-mark-dark.svg").read_text(
                encoding="utf-8"
            )
            favicon = (output / "favicon.svg").read_text(encoding="utf-8")
            dark_favicon = (output / "favicon-dark.svg").read_text(
                encoding="utf-8"
            )
            self.assertIn('id="construction-loop"', index)
            self.assertIn("data-loop-status", index)
            self.assertIn("decision control<br>agent topology", index)
            self.assertIn("intermediate form<br>edit interface", index)
            self.assertIn("observation source<br>feedback function", index)
            self.assertRegex(
                index, r'src="assets/charts\.js\?v=[0-9a-f]{12}"'
            )
            self.assertRegex(
                index, r'src="assets/app\.js\?v=[0-9a-f]{12}"'
            )
            self.assertRegex(
                index,
                r'src="assets/construction-loop\.js\?v=[0-9a-f]{12}"',
            )
            self.assertRegex(
                index,
                r'src="assets/fig2-construction-process\.png\?v=[0-9a-f]{12}"',
            )
            self.assertRegex(
                index, r'href="assets/styles\.css\?v=[0-9a-f]{12}"'
            )
            self.assertRegex(index, r'href="favicon\.svg\?v=[0-9a-f]{12}"')
            self.assertRegex(
                index,
                r'data-light-href="favicon\.svg\?v=[0-9a-f]{12}"',
            )
            self.assertRegex(
                index,
                r'data-dark-href="favicon-dark\.svg\?v=[0-9a-f]{12}"',
            )
            self.assertRegex(
                styles, r'url\("logo-mark\.svg\?v=[0-9a-f]{12}"\)'
            )
            self.assertRegex(
                styles, r'url\("logo-mark-dark\.svg\?v=[0-9a-f]{12}"\)'
            )
            self.assertIn("Six colored artifact-family modules", logo)
            self.assertEqual(logo, favicon)
            self.assertEqual(dark_logo, dark_favicon)
            self.assertIn('<rect width="1254" height="1254" fill="#fff"/>', logo)
            self.assertNotIn(
                '<rect width="1254" height="1254" fill="#fff"/>', dark_logo
            )
            self.assertIn('stop-color="#f7f9fc"', dark_logo)
            self.assertNotIn("<image", logo)
            self.assertNotIn("data:image", logo)
            self.assertNotIn("<image", dark_logo)
            self.assertNotIn("data:image", dark_logo)
            self.assertRegex(
                index,
                r'data-catalog-url="data/catalog\.json\?v=[0-9a-f]{12}"',
            )
            self.assertIn('id="venue-chart"', index)
            self.assertLess(
                index.index('href="#analysis">Analysis'),
                index.index('href="#catalog">Explore'),
            )
            self.assertLess(index.index('id="analysis"'), index.index('id="catalog"'))
            self.assertIn('id="page-size"', index)
            self.assertIn('id="pagination"', index)
            self.assertNotIn('id="load-more"', index)
            self.assertIn('@phosphor-icons/web@2.1.2', index)
            self.assertIn('ph-github-logo', index)
            self.assertIn('data-construction-loop', index)
            self.assertNotIn('src="visualization/', index)

            payload = json.loads(
                (output / "data" / "catalog.json").read_text(encoding="utf-8")
            )
            self.assertEqual(payload["summary"]["total"], len(payload["papers"]))

    def test_site_exposes_a_system_aware_theme_selector(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            index = (output / "index.html").read_text(encoding="utf-8")
            styles = (output / "assets" / "styles.css").read_text(encoding="utf-8")
            theme = (output / "assets" / "theme.js").read_text(encoding="utf-8")

            self.assertTrue((output / "assets" / "theme.js").is_file())
            self.assertRegex(index, r'src="assets/theme\.js\?v=[0-9a-f]{12}"')
            self.assertIn('aria-label="Color theme"', index)
            self.assertIn('data-theme-option="system"', index)
            self.assertIn('data-theme-option="light"', index)
            self.assertIn('data-theme-option="dark"', index)
            self.assertIn("prefers-color-scheme: dark", styles)
            self.assertIn(':root[data-theme="dark"]', styles)
            self.assertIn('id="site-favicon"', index)
            self.assertIn('document.querySelector("#site-favicon")', theme)
            self.assertIn("favicon.dataset.darkHref", theme)
            self.assertIn("updateFavicon(resolved)", theme)

    def test_catalog_tags_icon_artifact_and_application_dimensions_only(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            app = (output / "assets" / "app.js").read_text(encoding="utf-8")
            styles = (output / "assets" / "styles.css").read_text(encoding="utf-8")

            self.assertIn('artifact: "ph-cube"', app)
            self.assertIn('application: "ph-compass"', app)
            self.assertIn(
                '{ value: paper.artifact_family, dimension: "artifact" }',
                app,
            )
            self.assertIn('{ value: paper.artifact_type }', app)
            self.assertIn(
                '{ value: paper.application_domain, dimension: "application" }',
                app,
            )
            self.assertIn(".paper-tag i {", styles)

    def test_scope_uses_distinct_visual_galleries_for_both_axes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            index = (output / "index.html").read_text(encoding="utf-8")
            app = (output / "assets" / "app.js").read_text(encoding="utf-8")
            styles = (output / "assets" / "styles.css").read_text(encoding="utf-8")

            self.assertIn('class="axis-tab-icon"', index)
            artifact_tab = index.split('id="artifact-tab"', 1)[1].split(
                "</button>", 1
            )[0]
            self.assertIn('class="ph ph-cube"', artifact_tab)
            self.assertIn("What is constructed", index)
            self.assertIn("Where it matters", index)
            self.assertIn("const ARTIFACT_VISUALS = {", app)
            self.assertIn("const APPLICATION_VISUALS = {", app)
            for visual in (
                "textual",
                "visual",
                "audio",
                "video",
                "spatial",
                "behavioral",
            ):
                self.assertIn(f'visual: "{visual}"', app)
                self.assertIn(f'data-artifact-visual="{visual}"', app)
            for visual in (
                "creative",
                "brand",
                "education",
                "professional",
                "science",
                "engineering",
            ):
                self.assertIn(f'visual: "{visual}"', app)
                self.assertIn(f'data-application-visual="{visual}"', app)
            self.assertIn("function createArtifactMiniature", app)
            self.assertIn("function createApplicationMiniature", app)
            self.assertIn(".taxonomy-list,", styles)
            self.assertIn(".artifact-miniature", styles)
            self.assertIn(".application-miniature", styles)
            self.assertIn("@keyframes artifact-audio-wave", styles)
            self.assertIn("@keyframes artifact-spatial-float", styles)
            self.assertIn("@keyframes scope-panel-enter", styles)

    def test_scope_miniatures_use_layered_materials_and_display_surfaces(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            app = (output / "assets" / "app.js").read_text(encoding="utf-8")
            styles = (output / "assets" / "styles.css").read_text(encoding="utf-8")

            self.assertGreaterEqual(app.count("<linearGradient"), 12)
            self.assertGreaterEqual(app.count("<radialGradient"), 12)
            for layer in (
                "miniature-platform",
                "miniature-depth",
                "miniature-highlight",
                "miniature-detail",
            ):
                self.assertEqual(12, app.count(f'class="{layer}"'))
                self.assertIn(f".{layer}", styles)
            self.assertIn("@keyframes miniature-highlight-sweep", styles)
            self.assertIn("@keyframes miniature-platform-breathe", styles)

    def test_scope_showcase_motion_is_calm_interactive_and_accessible(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            app = (output / "assets" / "app.js").read_text(encoding="utf-8")
            styles = (output / "assets" / "styles.css").read_text(encoding="utf-8")

            self.assertIn("const MINIATURE_SHOWCASE_INTERVAL = 3600;", app)
            self.assertIn("function setupMiniatureShowcaseMotion()", app)
            self.assertIn("function setupMiniatureCardTilt()", app)
            self.assertIn('window.matchMedia("(pointer: fine)")', app)
            self.assertIn('window.matchMedia("(prefers-reduced-motion: reduce)")', app)
            self.assertIn("document.hidden", app)
            self.assertIn("new IntersectionObserver", app)
            self.assertIn('classList.toggle("is-showcase-active"', app)
            self.assertIn('new CustomEvent("aac:axischange"', app)
            self.assertIn("setupMiniatureShowcaseMotion();", app)
            self.assertIn("setupMiniatureCardTilt();", app)
            self.assertIn("--card-tilt-x", styles)
            self.assertIn("--card-tilt-y", styles)
            self.assertIn(".is-showcase-active", styles)
            self.assertIn("@keyframes miniature-stage-arrive", styles)

    def test_catalog_dimension_tags_are_filter_buttons(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            app = (output / "assets" / "app.js").read_text(encoding="utf-8")
            styles = (output / "assets" / "styles.css").read_text(encoding="utf-8")

            self.assertIn('createElement("button", className)', app)
            self.assertIn("tag.dataset.catalogView = dimension", app)
            self.assertIn("filterCatalogFromTag(dimension, value)", app)
            self.assertIn(".paper-tag-filter", styles)

    def test_primary_navigation_tracks_every_major_section(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            index = (output / "index.html").read_text(encoding="utf-8")
            app = (output / "assets" / "app.js").read_text(encoding="utf-8")
            styles = (output / "assets" / "styles.css").read_text(encoding="utf-8")

            self.assertEqual(2, index.count('href="#construction-loop">Concept</a>'))
            self.assertIn("function setupSectionNavigation()", app)
            self.assertIn('link.setAttribute("aria-current", "location")', app)
            self.assertIn(".desktop-nav a.is-current", styles)

    def test_mobile_construction_process_uses_readable_interactive_steps(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            index = (output / "index.html").read_text(encoding="utf-8")
            motion = (output / "assets" / "construction-loop.js").read_text(
                encoding="utf-8"
            )
            styles = (output / "assets" / "styles.css").read_text(encoding="utf-8")

            self.assertIn('class="loop-mobile-process"', index)
            self.assertEqual(5, index.count("data-loop-mobile-step="))
            self.assertIn("Artifact becomes the next task", index)
            self.assertIn("function setupMobileProcess()", motion)
            self.assertIn(".loop-mobile-step.is-active", styles)
            for stage in ("task", "policy", "representation", "verification", "artifact"):
                self.assertIn(f'data-loop-mobile-step="{stage}"', index)

    def test_heavy_visual_assets_load_progressively(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            index = (output / "index.html").read_text(encoding="utf-8")
            motion = (output / "assets" / "construction-loop.js").read_text(
                encoding="utf-8"
            )

            self.assertTrue(
                (output / "assets" / "fig2-construction-process.webp").is_file()
            )
            self.assertRegex(
                index,
                r'srcset="assets/fig2-construction-process\.webp\?v=[0-9a-f]{12}"',
            )
            self.assertIn('loading="lazy"', index)
            self.assertIn('rootMargin: "160px 0px"', motion)
            self.assertIn("function loadThreeWhenNearViewport()", motion)

    def test_construction_process_uses_a_neutral_loader_before_3d(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            index = (output / "index.html").read_text(encoding="utf-8")
            motion = (output / "assets" / "construction-loop.js").read_text(
                encoding="utf-8"
            )
            styles = (output / "assets" / "styles.css").read_text(encoding="utf-8")

            self.assertIn('class="loop-stage reveal is-loading"', index)
            self.assertIn('class="loop-loading"', index)
            self.assertRegex(
                styles,
                r"\.loop-fallback\s*\{[^}]*opacity:\s*0",
            )
            self.assertRegex(
                styles,
                r"\.loop-stage\.is-fallback\s+\.loop-fallback\s*\{[^}]*opacity:\s*1",
            )
            self.assertIn("@keyframes process-loader-node", styles)
            self.assertIn('root.classList.remove("is-loading")', motion)

    def test_visible_construction_process_initializes_without_an_extra_scroll(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            motion = (output / "assets" / "construction-loop.js").read_text(
                encoding="utf-8"
            )

            self.assertIn("function constructionLoopIsNearViewport()", motion)
            self.assertIn("bounds.top <= window.innerHeight + 160", motion)
            self.assertIn("if (constructionLoopIsNearViewport())", motion)

    def test_d3_uses_one_deferred_distribution_instead_of_an_esm_waterfall(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            index = (output / "index.html").read_text(encoding="utf-8")
            charts = (output / "assets" / "charts.js").read_text(encoding="utf-8")

            self.assertIn("d3@7.9.0/dist/d3.min.js", index)
            self.assertIn('src="assets/charts.js?', index)
            self.assertIn('defer></script>', index)
            self.assertNotIn("import * as d3", charts)
            self.assertIn("const d3 = window.d3", charts)
            self.assertTrue(charts.startswith("(() => {\n"))
            self.assertTrue(charts.rstrip().endswith("})();"))

    def test_hero_artifact_family_chart_excludes_application_only_records(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            charts = (output / "assets" / "charts.js").read_text(encoding="utf-8")

            hero_chart = re.search(
                r"function drawHeroFamilies\(.*?\n\}\n\nfunction drawComposition",
                charts,
                re.DOTALL,
            )
            self.assertIsNotNone(hero_chart)
            self.assertNotIn("Application-only", hero_chart.group(0))
            self.assertNotIn("applicationOnly", hero_chart.group(0))
            self.assertIn(
                "Horizontal bars compare paper counts across the six artifact families.",
                hero_chart.group(0),
            )

    def test_mobile_controls_expose_generous_touch_targets(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            styles = (output / "assets" / "styles.css").read_text(encoding="utf-8")

            mobile_styles = styles.split("@media (max-width: 640px)", 1)[1]
            self.assertRegex(
                mobile_styles,
                r"\.theme-option\s*\{[^}]*width:\s*40px;[^}]*height:\s*40px;",
            )
            self.assertRegex(
                mobile_styles,
                r"\.mobile-menu summary\s*\{[^}]*min-width:\s*44px;[^}]*min-height:\s*44px;",
            )

    def test_mobile_catalog_filters_collapse_into_a_disclosure(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            index = (output / "index.html").read_text(encoding="utf-8")
            app = (output / "assets" / "app.js").read_text(encoding="utf-8")
            styles = (output / "assets" / "styles.css").read_text(encoding="utf-8")

            self.assertIn('class="filter-panel-toggle"', index)
            self.assertIn('aria-controls="catalog-filter-controls"', index)
            self.assertIn('id="catalog-filter-controls"', index)
            self.assertIn("function setupFilterDisclosure()", app)
            self.assertIn(".filter-panel.is-expanded .filter-panel-controls", styles)

    def test_mobile_analysis_charts_explain_horizontal_exploration(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            index = (output / "index.html").read_text(encoding="utf-8")
            styles = (output / "assets" / "styles.css").read_text(encoding="utf-8")

            self.assertEqual(4, index.count('class="chart-mobile-hint"'))
            for chart_id in (
                "composition-chart",
                "venue-chart",
                "trend-chart",
                "matrix-chart",
            ):
                chart = re.search(
                    rf'<div\s+[^>]*id="{chart_id}"[^>]*>', index, re.DOTALL
                )
                self.assertIsNotNone(chart)
                self.assertIn('tabindex="0"', chart.group(0))
            self.assertIn(".chart-mobile-hint", styles)
            charts = (output / "assets" / "charts.js").read_text(encoding="utf-8")
            self.assertIn("function centerChartOnNarrowViewport", charts)
            self.assertIn('centerChartOnNarrowViewport("#composition-chart")', charts)

    def test_publication_status_filter_only_lists_statuses_in_the_catalog(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            index = (output / "index.html").read_text(encoding="utf-8")
            payload = json.loads(
                (output / "data" / "catalog.json").read_text(encoding="utf-8")
            )

            status_select = index.split('id="status-filter"', 1)[1].split(
                "</select>", 1
            )[0]
            option_values = set(re.findall(r'<option value="([^"]*)"', status_select))
            catalog_statuses = {paper["type"] for paper in payload["papers"]}

            self.assertEqual(catalog_statuses, option_values - {""})

    def test_interactive_framework_is_named_a_construction_process(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            index = (output / "index.html").read_text(encoding="utf-8")

            self.assertIn("A live construction process.", index)
            self.assertIn("three-dimensional construction process", index)
            self.assertIn(">Construction process</span>", index)

    def test_construction_process_cycles_through_the_spatial_stage_order(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            motion = (output / "assets" / "construction-loop.js").read_text(
                encoding="utf-8"
            )

            flow_details = re.search(
                r"const flowDetails = \[(.*?)\n\s+\];",
                motion,
                re.DOTALL,
            )
            self.assertIsNotNone(flow_details)
            stages = re.findall(r'stage: "([^"]+)"', flow_details.group(1))
            self.assertEqual(
                ["task", "policy", "representation", "verification", "artifact"],
                stages,
            )

    def test_artifact_feedback_path_returns_to_the_task(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            motion = (output / "assets" / "construction-loop.js").read_text(
                encoding="utf-8"
            )
            index = (output / "index.html").read_text(encoding="utf-8")

            feedback_path = re.search(
                r"const artifactToTaskFeedbackPoints = \[(.*?)\n\s+\];",
                motion,
                re.DOTALL,
            )
            self.assertIsNotNone(feedback_path)
            x_coordinates = [
                float(value)
                for value in re.findall(r"\[(-?[0-9.]+),", feedback_path.group(1))
            ]
            self.assertGreater(x_coordinates[0], 6.5)
            self.assertLess(x_coordinates[-1], -6.5)
            self.assertIn("artifact can begin the next task cycle", index)
            self.assertNotIn("feedback to the policy", index)

    def test_construction_process_gives_each_stage_unique_active_motion(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            motion = (output / "assets" / "construction-loop.js").read_text(
                encoding="utf-8"
            )

            self.assertIn("const stageMotionControllers = {", motion)
            for controller in (
                "animateTaskStage",
                "animatePolicyStage",
                "animateRepresentationStage",
                "animateVerificationStage",
                "animateArtifactStage",
            ):
                self.assertIn(f"function {controller}", motion)
            self.assertIn("group.userData.activeAmount", motion)
            self.assertIn("viewport.dataset.activeStage", motion)

    def test_construction_process_crossfades_stage_transitions(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            motion = (output / "assets" / "construction-loop.js").read_text(
                encoding="utf-8"
            )
            styles = (output / "assets" / "styles.css").read_text(encoding="utf-8")

            duration = re.search(r"STAGE_DURATION_SECONDS = ([0-9.]+)", motion)
            self.assertIsNotNone(duration)
            self.assertGreaterEqual(float(duration.group(1)), 3.0)
            self.assertIn("function dampMotion", motion)
            self.assertIn("Math.exp(-sharpness * delta)", motion)
            self.assertIn("@property --loop-active-x", styles)
            self.assertIn("transition: --loop-active-x", styles)

    def test_active_stage_motion_uses_a_calm_shared_tempo(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            motion = (output / "assets" / "construction-loop.js").read_text(
                encoding="utf-8"
            )

            tempo = re.search(r"ACTIVE_MOTION_TEMPO = ([0-9.]+)", motion)
            self.assertIsNotNone(tempo)
            self.assertLessEqual(float(tempo.group(1)), 0.65)
            self.assertGreaterEqual(
                motion.count("elapsed * ACTIVE_MOTION_TEMPO"),
                6,
            )

    def test_active_motion_phase_is_independent_from_transition_weights(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            motion = (output / "assets" / "construction-loop.js").read_text(
                encoding="utf-8"
            )

            variable_time_scales = re.findall(
                r"activeMotionTime\s*\*\s*\([^)]*(?:activeAmount|hoverAmount)[^)]*\)",
                motion,
            )
            variable_speed_constants = re.findall(
                r"const \w+Speed\s*=\s*[^;]*(?:activeAmount|hoverAmount)[^;]*;",
                motion,
            )
            self.assertEqual([], variable_time_scales)
            self.assertEqual([], variable_speed_constants)

    def test_stage_pulses_use_continuous_easing_at_their_turning_points(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            motion = (output / "assets" / "construction-loop.js").read_text(
                encoding="utf-8"
            )

            self.assertIn("function smoothPulse(phase)", motion)
            self.assertNotIn("Math.max(0, Math.sin", motion)

    def test_camera_easing_is_frame_rate_independent(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            motion = (output / "assets" / "construction-loop.js").read_text(
                encoding="utf-8"
            )

            self.assertNotIn("camera.position.x +=", motion)
            self.assertNotIn("camera.position.y +=", motion)
            self.assertIn("camera.position.x = dampMotion(", motion)
            self.assertIn("camera.position.y = dampMotion(", motion)

    def test_construction_policy_uses_five_small_controls(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            motion = (output / "assets" / "construction-loop.js").read_text(
                encoding="utf-8"
            )

            layout = re.search(
                r"const policyControlLayout = \[(.*?)\n\s+\];", motion, re.DOTALL
            )
            self.assertIsNotNone(layout)
            self.assertEqual(5, layout.group(1).count("{ kind:"))

    def test_site_exposes_progressive_motion_hooks(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            index = (output / "index.html").read_text(encoding="utf-8")

            self.assertIn('class="hero-copy reveal reveal-sequence"', index)
            self.assertEqual(5, index.count("data-count-up"))
            self.assertGreaterEqual(index.count("data-reveal-order"), 4)

    def test_survey_insights_bridge_analysis_to_catalog_exploration(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            index = (output / "index.html").read_text(encoding="utf-8")
            styles = (output / "assets" / "styles.css").read_text(encoding="utf-8")

            self.assertEqual(2, index.count('href="#insights">Insights</a>'))
            self.assertLess(
                index.index('href="#insights">Insights</a>'),
                index.index('href="#catalog">Explore</a>'),
            )
            self.assertLess(index.index('id="analysis"'), index.index('id="insights"'))
            self.assertLess(index.index('id="insights"'), index.index('id="catalog"'))
            self.assertEqual(4, index.count('class="insight-claim reveal"'))
            for insight in (
                "More agents do not create more agency.",
                "A score is not yet actionable feedback.",
                "Accepted evidence has a version.",
                "Control should match construction difficulty.",
            ):
                self.assertIn(insight, index)
            self.assertIn('href="#catalog" class="insight-link insight-link-primary"', index)
            self.assertIn(".insight-claim.is-visible::before", styles)
            self.assertIsNotNone(
                re.search(
                    r"@media \(prefers-reduced-motion: reduce\).*?\.insight-claim",
                    styles,
                    re.DOTALL,
                )
            )

    def test_about_section_explains_project_and_provides_copyable_citation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = build_site(Path(temporary_directory) / "public")
            index = (output / "index.html").read_text(encoding="utf-8")
            app = (output / "assets" / "app.js").read_text(encoding="utf-8")
            styles = (output / "assets" / "styles.css").read_text(encoding="utf-8")

            self.assertIn("An open research instrument.", index)
            self.assertIn('id="survey-citation"', index)
            self.assertIn("@misc{wang2026agenticartifactcreation,", index)
            self.assertIn(
                "Agentic Artifact Creation: A Survey of Systems, Evaluation, "
                "Principles, and Opportunities",
                index,
            )
            self.assertIn("data-copy-citation", index)
            self.assertIn('aria-live="polite"', index)
            self.assertIn("function setupCitationCopy()", app)
            self.assertIn("function copyWithSelection()", app)
            self.assertIn("navigator.clipboard.writeText", app)
            self.assertIn("setupCitationCopy();", app)
            self.assertIn(".citation-panel", styles)
            self.assertIn(".citation-copy.is-copied", styles)


if __name__ == "__main__":
    unittest.main()
