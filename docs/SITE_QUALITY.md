# Website polish and discovery

The website remains a Python-built static site. The catalog is the source of truth for both the interactive UI and the complete HTML paper index.

## Build and preview

```sh
python3 scripts/build_site.py
python3 -m http.server 8937 --bind 127.0.0.1 --directory _site
python3 -m unittest discover -s tests
```

Open http://127.0.0.1:8937/. Serve `_site`, not the `site` source template. For a custom domain, pass its full URL, including any path prefix:

```sh
python3 scripts/build_site.py --site-url https://example.org/research/
```

The default canonical address is https://tianfuwang.tech/awesome-agentic-artifact-creation/, the live custom domain configured for GitHub Pages. The `geminilight.github.io` address redirects to this host. Do not change it to a local preview URL for production.

## What changed

- Local system sans-serif typography across headings, body, charts, labels, and citations. No Google Fonts request.
- Consistent heading hierarchy, action placement, controls, focus states, gallery surfaces, and desktop/mobile spacing.
- Refined 3D materials and labels; selectable stages; pause/resume on desktop and mobile. Rendering stops when the page is hidden, the scene is offscreen, or motion is paused. Reduced-motion users receive a scalable, readable SVG overview.
- Institution emblems are served locally, removing six institution-host dependencies (HKU was already local).
- Build-time summary counts, first 10 papers, taxonomy links, and a full `papers.html` index with all records. Failed catalog requests preserve the initial papers and expose a retry action.
- Search remains visible on mobile while advanced filters can be collapsed. The catalog defaults to 10 papers per page, supports copying a filtered view, and moves keyboard focus to the first result after pagination.
- Compact illustrated mobile taxonomy cards, unified statistics and insight sections, clearer resource links, and a full-width citation panel. Chart marks support touch inspection and arrow-key navigation with one tab stop per chart.
- Canonical links, Open Graph/Twitter metadata, a 1200 × 630 social image, WebSite/CollectionPage/ScholarlyArticle/Dataset JSON-LD, and sitemap generation.
- A visible research reading guide, source links, audit methodology, citation, downloadable data, and a chart-data table.

The social-image source is `scripts/templates/social-preview.html`. Render it in Chromium at 1200 × 630 and save the viewport screenshot to `site/assets/social-preview.png` when changing the artwork. Counts are deliberately omitted from this image so it cannot silently become stale.

## Observed live baseline

The deployed page returned HTTP 200. Its raw HTML had no canonical, Open Graph preview, or JSON-LD, and the interactive paper list was empty before JavaScript. The host-root robots file allowed the tested search crawlers, including Googlebot, Bingbot, OAI-SearchBot, PerplexityBot, and Claude-SearchBot. Its sitemap declaration pointed to `https://tianfuwang.tech/sitemap.xml`.

A robots file in a GitHub Pages project subdirectory does **not** control crawling. The generated project `robots.txt` is useful only if the site is later served at a host root. For the current project URL, submit its sitemap directly in Search Console and Bing Webmaster Tools, or add its sitemap to the root-domain repository's robots file. This change does not modify that separate repository.

## Release verification

1. After deploying, fetch the public homepage, `papers.html`, `sitemap.xml`, and `assets/social-preview.png`; verify HTTP 200 and the intended canonical host.
2. Inspect the homepage and paper index in Google Search Console URL Inspection. Submit the project sitemap in Google Search Console and Bing Webmaster Tools.
3. Validate the emitted JSON-LD with Schema.org Validator / Google Rich Results Test. Structured data describes the site; it does not guarantee a rich result or AI citation.
4. Check PageSpeed Insights after deployment for actual field data when available. Local browser checks do not establish Core Web Vitals.
5. Compare indexed pages, impressions, clicks, and relevant queries after deployment. For AI visibility, periodically repeat a fixed prompt set with paraphrases across the engines that matter, recording cited URLs separately from mentions. No ranking, traffic, or AI share-of-voice measurement was performed for this code change.

Possible prompt intents: agentic artifact creation survey; AI agents for document and image creation; benchmarks for agentic 3D creation; artifact construction verification and feedback. Earned visibility can come from relevant paper/project repositories and survey or benchmark resource lists that accept a substantive contribution; no outreach or messages were sent.

## Evidence and limitations

Google documents that AI search eligibility relies on indexability and normal SEO foundations, without special AI markup: https://developers.google.com/search/docs/appearance/ai-features

Google recommends making content accessible and explains JavaScript rendering limitations: https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics

This implementation improves crawlable content and source clarity. It does not establish that Google/Bing has indexed the deployed changes, and it does not promise ranking or AI citations. Decorative institution emblems retain empty `alt` because the adjacent institution names already provide their accessible labels.

## Local verification results

- 76 Python tests passed, including catalog/index reconciliation, emitted metadata, custom deployment URL consistency, and HTML escaping.
- Browser checks passed at 390 × 844 and 1440 × 1000: search, empty results, reset, pagination, mobile stage selection, desktop 3D selection, pause/resume, dynamic reduced-motion switching, and light/dark rendering.
- The refinement pass also checked 320px and 768px widths, the single-line hero title, collapsed/expanded mobile filters, copying a catalog view, menu Escape handling, pagination focus, and chart arrow-key/Escape controls. No page-level horizontal overflow was observed at the four tested widths.
- JavaScript-disabled checks: the homepage retains its 10 initial records and actual summary counts; the complete index contains all 257 records.
- A deliberately blocked catalog request retained the initial papers and displayed recovery guidance.
- All seven affiliation images loaded locally. The static diagram and social preview were visually reviewed.
- Axe-core WCAG 2 A/AA scan after all sections were revealed and transitions settled: zero reported violations in both light and dark modes. Automated scans still leave manual-review items; this is not a full screen-reader or accessibility certification.
