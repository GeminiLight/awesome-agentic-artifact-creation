"""Check emitted crawlable pages against the canonical catalog, not JS source strings."""
import json
import re
import sys
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from build_site import build_site
from site_metadata import normalize_site_url, paper_html, SURVEY_DATA


class Page(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.elements = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


class DiscoveryTests(unittest.TestCase):
    def test_every_catalog_record_is_in_the_static_index(self):
        with tempfile.TemporaryDirectory() as directory:
            output = build_site(Path(directory) / 'public')
            data = json.loads((output / 'data/catalog.json').read_text())
            page = Page((output / 'papers.html').read_text())
            ids = [a['id'] for t, a in page.elements if t == 'li' and a.get('class') == 'paper-item']
            self.assertCountEqual(ids, ['paper-' + paper['bib_key'] for paper in data['papers']])
            links = [a.get('href') for t, a in page.elements if t == 'a']
            for paper in data['papers']:
                self.assertIn(paper['link'], links)
            initial = Page((output / 'index.html').read_text())
            self.assertEqual(10, sum(t == 'li' and a.get('class') == 'paper-item' for t, a in initial.elements))

    def test_default_build_consolidates_the_public_catalog_on_its_project_domain(self):
        url = 'https://agentic-creation.github.io/'
        with tempfile.TemporaryDirectory() as directory:
            output = build_site(Path(directory) / 'public')
            for filename in ['index.html', 'papers.html', 'survey.html', 'benchmarks.html']:
                expected = url if filename == 'index.html' else url + filename
                text = (output / filename).read_text()
                page = Page(text)
                self.assertEqual([expected], [a['href'] for t, a in page.elements
                                 if t == 'link' and a.get('rel') == 'canonical'])
                self.assertEqual([expected], [a['content'] for t, a in page.elements
                                 if t == 'meta' and a.get('property') == 'og:url'])
                self.assertEqual([url + 'assets/social-preview.png'],
                                 [a['content'] for t, a in page.elements
                                  if t == 'meta' and a.get('property') == 'og:image'])
                graph = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', text).group(1))
                self.assertNotIn('tianfu.wang/awesome-agentic-artifact-creation', json.dumps(graph))
                for node in graph['@graph']:
                    if node['@type'] in {'WebSite', 'CollectionPage', 'Dataset'}:
                        self.assertTrue(node['url'].startswith(url))
                        self.assertTrue(node['@id'].startswith(url))
            locations = [e.text for e in ElementTree.fromstring(
                (output / 'sitemap.xml').read_text()).findall('.//{*}loc')]
            self.assertEqual([url + path for path in ['', 'papers.html', 'survey.html', 'benchmarks.html']], locations)
            self.assertIn('Sitemap: ' + url + 'sitemap.xml',
                          (output / 'robots.txt').read_text())

    def test_custom_base_url_is_consistent_across_metadata_and_sitemap(self):
        with tempfile.TemporaryDirectory() as directory:
            url = 'https://example.org/research/'
            output = build_site(Path(directory) / 'public', url)
            for file in ['index.html', 'papers.html', 'survey.html', 'benchmarks.html']:
                text = (output / file).read_text()
                page = Page(text)
                canonicals = [a['href'] for t, a in page.elements if t == 'link' and a.get('rel') == 'canonical']
                expected = url if file == 'index.html' else url + file
                self.assertEqual(canonicals, [expected])
                graph = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', text).group(1))
                self.assertTrue(graph['@graph'])
                image = next(a['content'] for t, a in page.elements if a.get('property') == 'og:image')
                self.assertEqual(image, url + 'assets/social-preview.png')
                self.assertTrue((output / 'assets/social-preview.png').is_file())
            tree = ElementTree.fromstring((output / 'sitemap.xml').read_text())
            locations = [e.text for e in tree.findall('.//{*}loc')]
            self.assertEqual([url + path for path in ['', 'papers.html', 'survey.html', 'benchmarks.html']], locations)
            self.assertIn('Sitemap: ' + url + 'sitemap.xml', (output / 'robots.txt').read_text())

    def test_html_escaping_preserves_paper_text(self):
        paper = dict.fromkeys(['artifact_family', 'artifact_type', 'application_domain', 'name', 'code', 'bib_key', 'entry_kind', 'title', 'link', 'authors', 'venue_display_name', 'year', 'type'], '')
        paper.update(title='A <script> & "paper"', link='https://example.org/?a=1&b=2', entry_kind='system', type='preprint')
        html = paper_html(paper)
        self.assertNotIn('<script>', html)
        self.assertIn('&lt;script&gt;', html)
        self.assertIn(('a', {'href': paper['link']}), Page(html).elements)
        with self.assertRaises(ValueError):
            normalize_site_url('https://example.org/?draft=1')

    def test_benchmark_index_matches_only_the_audited_benchmarks(self):
        with tempfile.TemporaryDirectory() as directory:
            output = build_site(Path(directory) / 'public')
            data = json.loads((output / 'data/catalog.json').read_text())
            html = (output / 'benchmarks.html').read_text()
            page = Page(html)
            expected = [p for p in data['papers'] if p['entry_kind'] == 'benchmark']
            ids = [a['id'] for t, a in page.elements if t == 'li' and a.get('class') == 'paper-item']
            self.assertCountEqual(ids, ['paper-' + p['bib_key'] for p in expected])
            graph = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', html).group(1))['@graph']
            items = next(n for n in graph if n['@type'] == 'ItemList')
            self.assertEqual(items['numberOfItems'], len(expected))
            self.assertCountEqual([item['url'] for item in items['itemListElement']], [p['link'] for p in expected])

    def test_single_paper_metadata_and_abstract_are_separate_from_catalog(self):
        from html import unescape
        with tempfile.TemporaryDirectory() as directory:
            output = build_site(Path(directory) / 'public')
            html = (output / 'survey.html').read_text()
            page = Page(html)
            fields = [(a['name'], a['content']) for t, a in page.elements if t == 'meta' and a.get('name', '').startswith('citation_')]
            self.assertEqual([v for k, v in fields if k == 'citation_author'], SURVEY_DATA['authors'])
            self.assertIn(('citation_title', SURVEY_DATA['title']), fields)
            self.assertIn(('citation_publication_date', '2026/08/28'), fields)
            self.assertIn(('citation_doi', SURVEY_DATA['doi']), fields)
            for paragraph in SURVEY_DATA['abstract']:
                self.assertIn(paragraph, unescape(html))
            graph = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', html).group(1))['@graph']
            article = next(n for n in graph if n['@type'] == 'ScholarlyArticle')
            self.assertEqual(article['abstract'], '\n\n'.join(SURVEY_DATA['abstract']))
            self.assertEqual(json.loads((output / 'data/survey.json').read_text()), SURVEY_DATA)
            self.assertIn(SURVEY_DATA['doi'], (output / 'data/survey.bib').read_text())
            for filename in ['index.html', 'papers.html', 'benchmarks.html']:
                self.assertNotIn('name="citation_title"', (output / filename).read_text())

    def test_dataset_creator_has_visible_attribution_and_corresponding_data(self):
        with tempfile.TemporaryDirectory() as directory:
            output = build_site(Path(directory) / 'public')
            for filename in ['index.html', 'papers.html']:
                html = (output / filename).read_text()
                graph = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', html).group(1))['@graph']
                dataset = next(n for n in graph if n['@type'] == 'Dataset')
                self.assertEqual(dataset['creator']['name'], 'Tianfu Wang')
                self.assertIn('Catalog maintained by', html)
                self.assertTrue((output / 'data/catalog.json').is_file())
                self.assertRegex(dataset['version'], r'^[0-9a-f]{12}$')
                self.assertIn('257 records (229 systems and 28 benchmarks)', html)
                self.assertIn('259 works (230 systems and 29 benchmarks)', html)

    def test_discovery_pages_and_fragment_links_resolve_without_javascript(self):
        from urllib.parse import unquote, urlsplit
        with tempfile.TemporaryDirectory() as directory:
            output = build_site(Path(directory) / 'public')
            pages = ['index.html', 'papers.html', 'survey.html', 'benchmarks.html']
            for filename in pages:
                page = Page((output / filename).read_text())
                for tag, attrs in page.elements:
                    if tag != 'a' or not attrs.get('href'):
                        continue
                    url = urlsplit(attrs['href'])
                    if url.scheme or url.netloc:
                        continue
                    target = output / (url.path or filename)
                    if target.is_dir():
                        target /= 'index.html'
                    self.assertTrue(target.is_file(), (filename, attrs['href']))
                    if url.fragment and target.suffix == '.html':
                        ids = [a.get('id') for t, a in Page(target.read_text()).elements]
                        self.assertIn(unquote(url.fragment), ids, (filename, attrs['href']))
