"""Build crawlable research content from the same catalog as the interactive UI."""
from __future__ import annotations

import json
from html import escape
from pathlib import Path
from urllib.parse import quote, urlsplit

DEFAULT_SITE_URL = "https://tianfuwang.tech/awesome-agentic-artifact-creation/"
PROJECT_NAME = "Awesome Agentic Artifact Creation"
DESCRIPTION = "A survey and open catalog of agentic systems for creating, inspecting, and revising artifacts."
REPOSITORY = "https://github.com/GeminiLight/awesome-agentic-artifact-creation"
SURVEY = "https://arxiv.org/abs/2608.28122"
AUTHORS = ["Tianfu Wang", "Zhezheng Hao", "Xilin Xia", "Lixin Liu", "Mengkang Hu", "Hongzhang Liu", "Xi Chen", "Ziyan Liu", "Xiankun Lin", "Weijia Zhang", "Nicholas Jing Yuan", "Hui Xiong"]


def normalize_site_url(url: str) -> str:
    parsed = urlsplit(url)
    if parsed.scheme not in {"https", "http"} or not parsed.netloc or parsed.query or parsed.fragment:
        raise ValueError("Site URL must be an absolute HTTP(S) URL without a query or fragment")
    return url.rstrip("/") + "/"


def paper_html(paper: dict) -> str:
    e = escape
    tags = "".join(f'<span class="paper-tag">{e(paper[key])}</span>' for key in ("artifact_family", "artifact_type", "application_domain") if paper[key])
    name = paper["name"] if paper["name"].lower() not in {"n/a", "na", "none"} else ""
    code = f'<a href="{e(paper["code"], quote=True)}">Code</a>' if paper["code"] else ""
    return f'''<li class="paper-item" id="paper-{e(paper['bib_key'], quote=True)}">
      <div class="paper-body"><div class="paper-kicker"><span>{e(paper['entry_kind'].title())}</span><span class="system-name">{e(name)}</span></div>
      <h3 class="paper-title"><a href="{e(paper['link'], quote=True)}">{e(paper['title'])}</a></h3>
      <p class="paper-authors">{e(paper['authors'])}</p><div class="paper-tags">{tags}</div></div>
      <div class="paper-meta"><span class="paper-venue">{e(paper['venue_display_name'])}</span><span class="paper-year">{e(paper['year'])}</span>
      <span class="status-pill {e(paper['type'], quote=True)}">{e(paper['type'].title())}</span><div class="paper-links"><a href="{e(paper['link'], quote=True)}">Paper</a>{code}</div></div></li>'''


def metadata(url: str, title: str, description: str, graph: list) -> str:
    image = normalize_site_url(url.rsplit("/", 1)[0] if url.endswith(".html") else url) + "assets/social-preview.png"
    return f'''<link rel="canonical" href="{escape(url, quote=True)}">
    <meta name="robots" content="index,follow,max-image-preview:large">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="{PROJECT_NAME}">
    <meta property="og:title" content="{escape(title, quote=True)}">
    <meta property="og:description" content="{escape(description, quote=True)}">
    <meta property="og:url" content="{escape(url, quote=True)}">
    <meta property="og:image" content="{escape(image, quote=True)}">
    <meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
    <meta property="og:image:alt" content="Agentic Artifact Creation research atlas: text, images, audio, video, spatial and behavioral artifacts">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{escape(title, quote=True)}">
    <meta name="twitter:description" content="{escape(description, quote=True)}">
    <meta name="twitter:image" content="{escape(image, quote=True)}">
    <script type="application/ld+json">{json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False).replace('<', chr(92) + 'u003c')}</script>'''


def build_discovery(output: Path, index: str, payload: dict, site_url: str) -> str:
    site_url = normalize_site_url(site_url)
    summary = payload["summary"]
    graph = [
        {"@type": "WebSite", "@id": site_url + "#website", "url": site_url, "name": PROJECT_NAME, "description": DESCRIPTION, "inLanguage": "en", "sameAs": REPOSITORY},
        {"@type": "CollectionPage", "@id": site_url + "#webpage", "url": site_url, "name": PROJECT_NAME, "description": DESCRIPTION, "isPartOf": {"@id": site_url + "#website"}, "mainEntity": {"@id": site_url + "#dataset"}, "about": {"@id": SURVEY}},
        {"@type": "ScholarlyArticle", "@id": SURVEY, "url": SURVEY, "name": "Agentic Artifact Creation: Systems, Evaluation, Principles, and Opportunities", "author": [{"@type": "Person", "name": name} for name in AUTHORS], "sameAs": "https://doi.org/10.48550/arXiv.2608.28122"},
        {"@type": "Dataset", "@id": site_url + "#dataset", "name": PROJECT_NAME + " catalog", "description": f"{summary['total']} research records organized by artifact family and application domain. " + DESCRIPTION, "url": site_url + "papers.html", "license": "https://creativecommons.org/licenses/by/4.0/", "isBasedOn": REPOSITORY + "/tree/main/data", "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": site_url + "data/catalog.json"}},
    ]
    index = index.replace("<!-- SITE_METADATA -->", metadata(site_url, "Agentic Artifact Creation — AI Agents, Papers & Benchmarks", DESCRIPTION, graph))
    # Initial content remains useful without hydration; the complete index is a separate, linked document.
    papers = sorted(payload["papers"], key=lambda p: (-int(p["year"]), p["venue_display_name"], p["title"]))
    index = index.replace("<!-- INITIAL_PAPERS -->", "\n".join(paper_html(p) for p in papers[:10]))
    index = index.replace('<strong id="result-count">...</strong>', f'<strong id="result-count">{summary["total"]}</strong>')
    for key, value in summary.items():
        index = index.replace(f'data-stat="{key}" data-count-up>...</dd>', f'data-stat="{key}" data-count-up>{value:,}</dd>')
    for target, records in (("family-overview", payload["families"]), ("application-overview", payload["applications"])):
        links = "".join(f'<a class="static-taxonomy-link" href="papers.html#{quote(row["name"], safe="")}">{escape(row["name"])} <span>{row["count"]} papers</span></a>' for row in records) if target == "family-overview" else "".join(f'<a class="static-taxonomy-link" href="papers.html">{escape(row["name"])} <span>{row["count"]} papers</span></a>' for row in records)
        index = index.replace(f'id="{target}"></div>', f'id="{target}">{links}</div>')

    rows = "".join(f'<tr><th scope="row">{escape(row["name"])}</th><td>{row["count"]}</td></tr>' for row in payload["families"])
    table = '<details class="chart-data-summary"><summary>Read the chart data · artifact family counts</summary><table><caption>Audited catalog: ' + str(summary["total"]) + ' papers; ' + str(sum(r["count"] for r in payload["families"])) + ' have an artifact-family label. Unclassified records remain in the full index.</caption><thead><tr><th scope="col">Artifact family</th><th scope="col">Papers</th></tr></thead><tbody>' + rows + '</tbody></table><a href="data/catalog.json">Download all chart data as JSON</a></details>'
    index = index.replace("<!-- CHART_DATA_SUMMARY -->", table)

    families = [row["name"] for row in payload["families"]]
    if any(not p["artifact_family"] for p in papers):
        families.append("Unclassified")
    sections = []
    navigation = []
    for family in families:
        group = [p for p in papers if (p["artifact_family"] or "Unclassified") == family]
        anchor = quote(family, safe="")
        navigation.append(f'<a href="#{anchor}">{escape(family)} · {len(group)}</a>')
        sections.append(f'<section id="{escape(family, quote=True)}"><h2>{escape(family)} <small>({len(group)})</small></h2><ol class="paper-list">' + "\n".join(paper_html(p) for p in group) + '</ol></section>')
    title = "Agentic AI Paper Index — Systems & Benchmarks"
    desc = f"Browse all {summary['total']} papers on AI agents for artifact creation, with authors, publication venues, original papers, and code."
    directory_graph = [{"@type": "CollectionPage", "@id": site_url + "papers.html", "url": site_url + "papers.html", "name": title, "description": desc, "isPartOf": {"@id": site_url + "#website"}}]
    directory = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{escape(title)}</title><meta name="description" content="{escape(desc, quote=True)}">
    {metadata(site_url + 'papers.html', title, desc, directory_graph)}
    <link rel="icon" href="favicon.svg" type="image/svg+xml"><script src="assets/theme.js"></script><link rel="stylesheet" href="assets/styles.css"></head>
    <body><main class="index-page"><a href="./">← Back to the research atlas</a><p class="eyebrow" style="margin-top:40px">Complete research index</p><h1>AI agents that create artifacts.</h1>
    <p>{escape(desc)}</p><p>Generated from the same audited dataset as the <a href="./#catalog">interactive catalog</a>. Each record links to its original source. <a href="data/catalog.json">Download JSON</a>.</p>
    <nav class="index-nav" aria-label="Artifact families">{''.join(navigation)}</nav>{''.join(sections)}
    <p><a href="./#about">About the survey and citation</a> · <a href="{REPOSITORY}/blob/main/AUDIT.md">Audit methodology</a> · CC BY 4.0</p></main></body></html>'''
    (output / "papers.html").write_text(directory, encoding="utf-8")
    (output / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{escape(site_url + path)}</loc></url>\n' for path in ('', 'papers.html')) + '</urlset>\n', encoding="utf-8")
    # Effective only if deployed at the host root; project Pages uses the host's robots.txt.
    (output / "robots.txt").write_text(f'User-agent: *\nAllow: /\n\nSitemap: {site_url}sitemap.xml\n', encoding="utf-8")
    return index
