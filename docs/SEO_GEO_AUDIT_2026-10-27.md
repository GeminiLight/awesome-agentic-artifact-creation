# Search discovery audit — 27 October 2026

The canonical website is https://agentic-creation.github.io/. Its source is this
repository; `agentic-creation/agentic-creation.github.io` checks out `main`, runs
validation, and publishes the build. The manuscript is a separate repository.

## Observed baseline

| Priority | Finding | Evidence | Action and verification |
| --- | --- | --- | --- |
| P1 | The complete paper index is not yet known to Google. | Search Console URL Inspection on 27 October reports `URL is unknown to Google` for `papers.html`. The live URL returns 200 and has a self-canonical. | Preserve its crawlable records, strengthen descriptive resource navigation, resubmit the sitemap after deployment, and request indexing in Search Console. Inspect again after Google recrawls; deployment alone does not establish indexing. |
| P1 | The project lacks a dedicated, complete single-paper abstract page. | The homepage has authors and a citation but only a brief survey description; its sitemap lists only the homepage and paper index. No `citation_*` tags appear on those live pages. | Add `survey.html` with the complete public abstract, verified authors, date, DOI, single-paper citation metadata, and links to the public full text. Check raw HTML and downloaded citation. |
| P1 | Preprint and catalog counts need a clear distinction. | The public arXiv v1 abstract describes 259 works (230 systems, 29 benchmarks). The audited catalog contains 257 records (229 systems, 28 benchmarks), including 218 named systems. | Explain the separate scopes near homepage counts, in the full index, and on the paper page. Generate catalog counts from the existing data without changing inclusion decisions. |
| P2 | Dataset metadata lacks a creator. | Search Console detects a Dataset rich result with `Missing field "creator"` as a warning. | Add the catalog maintainer and visible attribution, plus a content-derived dataset version. Check JSON-LD locally; the historical Google warning can remain until a recrawl. |
| P2 | Bibliographic resources and evaluation entries lack focused navigation. | The static index contains all records; a benchmark-only document is absent. | Add `benchmarks.html` from audited benchmark records, direct internal links, and sitemap entries. Reconcile every listed benchmark against the catalog. |

The homepage **is indexed**: URL Inspection reports `Submitted and indexed`,
successful mobile crawling, and matching Google/user canonicals. Its reported
last crawl is 22 October 2026 at 01:47:13 UTC. The new project property was
configured on 26 October; Search Analytics returned no rows for 26 September–24
October. This is unavailable performance evidence, not proof of zero traffic.
The sitemap was submitted on 26 October and was still pending, with zero
reported errors or warnings, at the audit.

Live HTML already contains canonical, Open Graph, Twitter, and JSON-LD metadata,
10 initial papers, and a linked complete index. Live `robots.txt` allows
Googlebot, Bingbot, OAI-SearchBot, PerplexityBot, and Claude-SearchBot. This verifies
declared access, not successful crawling by every vendor. Seven affiliation
emblems intentionally have empty alt text because adjacent text names the
institutions; they are decorative, not missing content descriptions.

## Implementation

- `data/survey.json` stores the **public arXiv v1** bibliographic record and
  author-written abstract. Do not silently replace it with an unpublished
  manuscript revision. The paper's frozen counts remain separate from catalog
  totals. Publication date is not a site modification date.
- `survey.html` is a single-paper abstract and reference page. Citation metadata
  belongs here, not on the multi-paper catalog. Full text is linked at arXiv;
  no `citation_pdf_url` claims a same-site PDF that we do not host. Scholar
  inclusion of this page is not guaranteed; arXiv remains the full-text source.
- `benchmarks.html` contains precisely the audited benchmark subset. It does not
  rank benchmarks or compare results measured under different protocols.
- All four HTML resources have consistent canonicals, social descriptions,
  genuine internal links, and content-versioned shared assets. New pages use
  the existing responsive typography and color themes. No fabricated freshness
  dates or new taxonomy/keyword-variant pages are emitted.

## Reproducible verification

```sh
python3 scripts/build_catalog.py --check
python3 scripts/generate_readme.py --check
python3 -m unittest discover -s tests
python3 scripts/build_site.py
```

Fetch the deployed homepage, `papers.html`, `survey.html`, `benchmarks.html`,
`sitemap.xml`, `data/survey.bib`, `data/survey.json`, and the social image. Check
HTTP 200 and canonical URLs. Validate deployed structured data with Google's
Rich Results Test or Schema.org Validator. The automated suite checks actual
HTML, custom base URLs, benchmark membership, abstract/citation consistency,
dataset attribution, and local file/fragment links. It does not simulate a
search engine's index or measure field Core Web Vitals.

## Measurement and earned visibility

Use Search Console to inspect each HTML page after recrawling. Review query/page
impressions and clicks in 7-day and 28-day windows once this newly configured
property has data. Compare branded queries (`Agentic Artifact Creation`, paper
title, author) separately from document/image/3D creation and evaluation queries.
Google's AI feature traffic is included in the overall Web performance report;
do not invent a separate AI Overview filter or treat ordinary impressions as
an AI citation rate. Check Bing Webmaster Tools access before submitting its
sitemap; no Bing ownership or indexing claim is made by this audit.

An unmeasured panel has been prepared locally for ChatGPT search and Perplexity:
10 intents × 3 independently written paraphrases × 3 repeats × 2 engines.
Record actual answers and source URLs before computing any rate. Count direct
citations of this domain separately from citations of arXiv/GitHub and from
unlinked name mentions. There is **no measured GEO citation rate** in this audit.
Suggested first comparison: one week after deployment, then after 28 days;
these are measurement recommendations, not a configured recurring automation.

Useful existing source targets are the paper's [Hugging Face page](https://huggingface.co/papers/2608.28122)
for branded paper discovery, the [public arXiv record](https://arxiv.org/abs/2608.28122)
for bibliographic identity, and the [canonical GitHub catalog](https://github.com/GeminiLight/awesome-agentic-artifact-creation)
for artifact/benchmark browsing. Search Console already reports the Hugging Face
page among referring URLs. Verify official website links on these records and
contribute useful, source-backed corrections where needed. Catalog maintainer
owns follow-up after deployment; no outreach, posting, or edits to third-party
records are part of this change. Avoid buying mentions or creating promotional
pages for every query variant.

This week's priorities are publishing and checking these resources, requesting
indexing of the complete index, and establishing the first real measurement
panel. The next run must report what engines actually cite, not a readiness score.

## Primary references

- [Google: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features): ordinary indexing and SEO foundations apply; no special AI schema is required or guarantees citation.
- [Google: crawlable links](https://developers.google.com/search/docs/crawling-indexing/links-crawlable): use actual links and descriptive anchors.
- [Google: Dataset structured data](https://developers.google.com/search/docs/appearance/structured-data/dataset): dataset identity, creator, license, and distribution describe the released catalog.
- [Google Scholar inclusion guidelines](https://scholar.google.com/intl/en/scholar/inclusion.html): accessible author-written abstracts, individual-paper metadata, and same-site PDF rules.
- [Public preprint, arXiv:2608.28122v1](https://arxiv.org/abs/2608.28122v1): published title, authors, abstract, dates, and corpus counts.

The choice of focused paper/benchmark resource pages and the follow-up cadence
are editorial/engineering judgments, not claimed ranking factors. Formatting,
structured data, and bot permission alone do not demonstrate GEO performance.
