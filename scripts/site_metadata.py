"""Build crawlable research content from the same catalog as the interactive UI."""
from __future__ import annotations

import json
import hashlib
from html import escape
from pathlib import Path
from urllib.parse import quote, urlsplit

DEFAULT_SITE_URL = "https://agentic-creation.github.io/"
PROJECT_NAME = "Agentic Artifact Creation"
DESCRIPTION = "A research survey and open catalog of AI agents that construct, inspect, and revise documents, images, audio, video, 3D worlds, and software."
REPOSITORY = "https://github.com/GeminiLight/awesome-agentic-artifact-creation"
SURVEY = "https://arxiv.org/abs/2608.28122"
SURVEY_DATA = json.loads((Path(__file__).resolve().parents[1] / "data/survey.json").read_text(encoding="utf-8"))
AUTHORS = SURVEY_DATA["authors"]


def survey_article(site_url: str, *, include_abstract: bool = False) -> dict:
    article = {
        "@type": "ScholarlyArticle", "@id": SURVEY, "url": SURVEY,
        "name": SURVEY_DATA["title"], "headline": SURVEY_DATA["title"],
        "author": [{"@type": "Person", "name": name} for name in AUTHORS],
        "datePublished": SURVEY_DATA["publication_date"], "inLanguage": "en",
        "identifier": SURVEY_DATA["doi"], "version": SURVEY_DATA["version"],
        "sameAs": "https://doi.org/" + SURVEY_DATA["doi"],
        "mainEntityOfPage": {"@id": site_url + "survey.html"},
    }
    if include_abstract:
        article['abstract'] = '\n\n'.join(SURVEY_DATA['abstract'])
    return article


def catalog_note(summary: dict) -> str:
    return (
        f'The <a href="{SURVEY}v1">August 2026 preprint</a> reviews '
        f'{SURVEY_DATA["reviewed_works"]} works ({SURVEY_DATA["systems"]} systems and '
        f'{SURVEY_DATA["benchmarks"]} benchmarks). This separately audited web catalog contains '
        f'{summary["total"]} records ({summary["systems"]} systems and {summary["benchmarks"]} benchmarks); '
        f'{summary["named_systems"]} systems have verified names. Catalog counts follow the '
        f'<a href="{REPOSITORY}/blob/main/AUDIT.md">inclusion audit and venue policy</a>, '
        'rather than reproducing the preprint’s frozen corpus.'
    )


def document_page(site_url: str, filename: str, title: str, description: str, body: str,
                  graph: list, extra_head: str = "") -> str:
    navigation = ''.join(
        f'<a href="{path}"' + (' aria-current="page"' if filename == path else '') + f'>{label}</a>'
        for path, label in [("./", "Research atlas"), ("survey.html", "Survey"),
                            ("papers.html", "All papers"), ("benchmarks.html", "Benchmarks")]
    )
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{escape(title)}</title><meta name="description" content="{escape(description, quote=True)}">
    {metadata(site_url + filename, title, description, graph)}{extra_head}
    <link rel="icon" href="favicon.svg" type="image/svg+xml"><script src="assets/theme.js"></script><link rel="stylesheet" href="assets/styles.css"></head>
    <body><a class="skip-link" href="#content">Skip to content</a><main class="index-page" id="content">
    <nav class="document-nav" aria-label="Research resources">{navigation}</nav>{body}
    <footer class="document-footer"><p>Catalog maintained by <a href="https://tianfu.wang/">Tianfu Wang</a> · <a href="{REPOSITORY}">GitHub</a> · <a href="{REPOSITORY}/blob/main/AUDIT.md">Audit methodology</a></p>
    <p>Catalog data: CC BY 4.0. Referenced papers retain their own licenses.</p></footer></main></body></html>'''


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
    <meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
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
        {"@type": "WebSite", "@id": site_url + "#website", "url": site_url, "name": PROJECT_NAME, "alternateName": "Awesome Agentic Artifact Creation", "description": DESCRIPTION, "inLanguage": "en", "sameAs": REPOSITORY},
        {"@type": "CollectionPage", "@id": site_url + "#webpage", "url": site_url, "name": PROJECT_NAME, "description": DESCRIPTION, "isPartOf": {"@id": site_url + "#website"}, "mainEntity": {"@id": site_url + "#dataset"}, "about": {"@id": SURVEY}},
        survey_article(site_url),
        {"@type": "Dataset", "@id": site_url + "#dataset", "name": PROJECT_NAME + " catalog", "description": f"{summary['total']} research records organized by artifact family and application domain. " + DESCRIPTION, "url": site_url + "papers.html", "license": "https://creativecommons.org/licenses/by/4.0/", "isBasedOn": REPOSITORY + "/tree/main/data", "creator": {"@type": "Person", "name": "Tianfu Wang", "url": "https://tianfu.wang/", "sameAs": "https://github.com/GeminiLight"}, "version": hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()[:12], "citation": SURVEY, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": site_url + "data/catalog.json"}},
    ]
    index = index.replace("<!-- SITE_DESCRIPTION -->", f'<meta name="description" content="{escape(DESCRIPTION, quote=True)}">')
    index = index.replace("<!-- SITE_METADATA -->", metadata(site_url, "Agentic Artifact Creation — AI Agents, Papers & Benchmarks", DESCRIPTION, graph))
    index = index.replace("<!-- CATALOG_NOTE -->", catalog_note(summary))
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
    title = "Agentic Artifact Creation — Complete Paper Index"
    desc = f"Browse all {summary['total']} papers on AI agents for artifact creation, with authors, publication venues, original papers, and code."
    directory_graph = [{"@type": "CollectionPage", "@id": site_url + "papers.html", "url": site_url + "papers.html", "name": title, "description": desc, "isPartOf": {"@id": site_url + "#website"}, "mainEntity": {"@id": site_url + "#dataset"}}, graph[-1]]
    directory_body = f'''<p class="eyebrow">Complete research index</p><h1>Agentic Artifact Creation paper index.</h1>
    <p>{escape(desc)}</p><p>Generated from the same audited dataset as the <a href="./#catalog">interactive catalog</a>. Each record links to its original source. <a href="data/catalog.json">Download JSON</a>.</p>
    <aside class="corpus-note" aria-label="Corpus scope">{catalog_note(summary)}</aside>
    <nav class="index-nav" aria-label="Artifact families">{''.join(navigation)}</nav>{''.join(sections)}
    <p><a href="survey.html#citation">Cite the survey</a> · <a href="benchmarks.html">Browse only benchmarks</a></p>'''
    directory = document_page(site_url, "papers.html", title, desc, directory_body, directory_graph)
    (output / "papers.html").write_text(directory, encoding="utf-8")
    build_survey_page(output, payload, site_url)
    build_benchmark_page(output, papers, site_url)
    (output / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{escape(site_url + path)}</loc></url>\n' for path in ('', 'papers.html', 'survey.html', 'benchmarks.html')) + '</urlset>\n', encoding="utf-8")
    # Effective only if deployed at the host root; project Pages uses the host's robots.txt.
    (output / "robots.txt").write_text(f'User-agent: *\nAllow: /\n\nSitemap: {site_url}sitemap.xml\n', encoding="utf-8")
    return index


def build_survey_page(output: Path, payload: dict, site_url: str) -> None:
    """A single-paper abstract page; citation tags never describe the whole catalog."""
    paper = SURVEY_DATA
    title = paper["title"]
    description = "Read the survey abstract, authors, construction framework, and citation for Agentic Artifact Creation; explore the separately audited paper catalog."
    citation = (
        '@article{wang2026agenticartifactcreation,\n'
        f'  title = {{{title}}},\n'
        '  author = {' + ' and '.join(name.rsplit(' ', 1)[1] + ', ' + name.rsplit(' ', 1)[0] for name in AUTHORS) + '},\n'
        '  year = {2026},\n'
        f'  eprint = {{{paper["arxiv_id"]}}},\n'
        '  archivePrefix = {arXiv},\n'
        '  primaryClass = {cs.MM},\n'
        f'  doi = {{{paper["doi"]}}},\n'
        f'  url = {{{SURVEY}}}\n'
        '}\n'
    )
    (output / 'data/survey.bib').write_text(citation, encoding='utf-8')
    (output / 'data/survey.json').write_text(json.dumps(paper, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    citation_fields = [("citation_title", title), *[("citation_author", name) for name in AUTHORS],
                       ("citation_publication_date", paper["publication_date"].replace('-', '/')),
                       ("citation_doi", paper["doi"]), ("citation_arxiv_id", paper["arxiv_id"]),
                       ("citation_abstract_html_url", site_url + 'survey.html')]
    # Scholar requires a same-site PDF for citation_pdf_url. The public full text
    # lives at arXiv, so link it visibly without claiming a locally hosted PDF.
    head = ''.join(f'<meta name="{key}" content="{escape(value, quote=True)}">' for key, value in citation_fields)
    authors = ', '.join(escape(name) for name in AUTHORS)
    abstract = ''.join(f'<p>{escape(paragraph)}</p>' for paragraph in paper['abstract'])
    families = ''.join(f'<li><a href="papers.html#{quote(family["name"], safe="")}">{escape(family["name"])}</a>: ' + ', '.join(escape(t['name']) for t in family['types']) + '.</li>' for family in payload['families'])
    body = f'''<header class="document-heading"><p class="eyebrow">Survey · arXiv:{paper['arxiv_id']}</p>
    <h1>{escape(title)}</h1><p class="document-authors">{authors}</p>
    <p class="document-meta">Published <time datetime="{paper['publication_date']}">28 August 2026</time> · Public preprint {paper['version']} · Literature through <time datetime="{paper['literature_cutoff']}">20 August 2026</time></p>
    <div class="document-actions"><a href="{SURVEY}">Read on arXiv ↗</a><a href="https://arxiv.org/pdf/{paper['arxiv_id']}">Full paper PDF ↗</a><a href="data/survey.bib" download>Download BibTeX</a></div></header>
    <section id="abstract" class="document-prose"><h2>Abstract</h2>{abstract}</section>
    <section id="framework" class="document-prose"><h2>What makes artifact creation agentic?</h2>
    <p>An AI system constructs or revises a persistent deliverable, and intermediate observations can change what it does next. The framework connects construction policy, operational representation, and runtime verification. A fixed sequence of agents or stages alone does not establish this feedback-conditioned control.</p>
    <p><a href="./#construction-loop">Explore the construction framework</a> or read the <a href="{REPOSITORY}/blob/main/AUDIT.md">operational inclusion rule</a>.</p></section>
    <section class="document-prose" id="scope"><h2>Which artifacts does the survey cover?</h2><ul>{families}</ul>
    <p>Application contexts are a separate axis: creative production, brand communication, educational support, professional work, scientific research, and engineering design.</p></section>
    <section class="document-prose" id="corpus"><h2>Why do the paper and website have different counts?</h2><p>{catalog_note(payload['summary'])}</p>
    <p>The published abstract above preserves the public preprint’s numbers. The downloadable <a href="data/catalog.json">catalog JSON</a> and <a href="papers.html">complete paper index</a> describe the web catalog. Use the <a href="benchmarks.html">benchmark index</a> to find its evaluation resources.</p></section>
    <section id="citation" class="document-prose"><h2>How to cite the survey</h2><p>{authors} (2026). <em>{escape(title)}</em>. arXiv:{paper['arxiv_id']}. <a href="https://doi.org/{paper['doi']}">doi:{paper['doi']}</a>.</p>
    <pre class="document-citation" tabindex="0" aria-label="Survey BibTeX"><code>{escape(citation)}</code></pre><p><a href="data/survey.bib" download>Download BibTeX</a> · <a href="data/survey.json">Paper metadata as JSON</a></p></section>'''
    article = survey_article(site_url, include_abstract=True)
    page = {"@type": "WebPage", "@id": site_url + 'survey.html', "url": site_url + 'survey.html',
            "name": title, "description": description, "isPartOf": {"@id": site_url + '#website'},
            "mainEntity": {"@id": SURVEY}}
    (output / 'survey.html').write_text(document_page(site_url, 'survey.html', title, description, body, [page, article], head), encoding='utf-8')


def build_benchmark_page(output: Path, papers: list[dict], site_url: str) -> None:
    benchmarks = [paper for paper in papers if paper['entry_kind'] == 'benchmark']
    title = "Agentic Artifact Creation — Benchmarks & Evaluation"
    description = f"Explore {len(benchmarks)} audited benchmarks for agentic artifact creation, grouped by artifact family with original papers and available code."
    families = list(dict.fromkeys(paper['artifact_family'] or 'Unclassified' for paper in benchmarks))
    sections = []
    nav = []
    for family in families:
        group = [p for p in benchmarks if (p['artifact_family'] or 'Unclassified') == family]
        nav.append(f'<a href="#{quote(family, safe="")}">{escape(family)} · {len(group)}</a>')
        sections.append(f'<section id="{escape(family, quote=True)}"><h2>{escape(family)} <small>({len(group)})</small></h2><ol class="paper-list">' + ''.join(paper_html(p) for p in group) + '</ol></section>')
    body = f'''<p class="eyebrow">Evaluation resources · {len(benchmarks)} benchmarks</p><h1>Benchmarks for agentic artifact creation.</h1>
    <p>{escape(description)}</p><p>Benchmark inclusion is assessed separately from system inclusion in the <a href="papers.html">audited catalog</a>. Read the <a href="survey.html#framework">survey framework</a> for artifact, process, and system evaluation; each original paper describes its tasks and metrics.</p>
    <nav class="index-nav" aria-label="Benchmark artifact families">{''.join(nav)}</nav>{''.join(sections)}'''
    ordered = [p for family in families for p in benchmarks if (p['artifact_family'] or 'Unclassified') == family]
    items = {"@type": "ItemList", "@id": site_url + 'benchmarks.html#list', "numberOfItems": len(benchmarks), "itemListOrder": "https://schema.org/ItemListUnordered",
             "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": p['link'], "name": p['title']} for i, p in enumerate(ordered)]}
    graph = [{"@type": "CollectionPage", "@id": site_url + 'benchmarks.html', "url": site_url + 'benchmarks.html',
              "name": title, "description": description, "isPartOf": {"@id": site_url + '#website'}, "mainEntity": {"@id": items['@id']}}, items]
    (output / 'benchmarks.html').write_text(document_page(site_url, 'benchmarks.html', title, description, body, graph), encoding='utf-8')
