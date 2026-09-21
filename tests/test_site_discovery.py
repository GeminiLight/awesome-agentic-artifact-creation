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
from site_metadata import normalize_site_url, paper_html


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

    def test_custom_base_url_is_consistent_across_metadata_and_sitemap(self):
        with tempfile.TemporaryDirectory() as directory:
            url = 'https://example.org/research/'
            output = build_site(Path(directory) / 'public', url)
            for file in ['index.html', 'papers.html']:
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
            self.assertEqual([url, url + 'papers.html'], locations)
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
