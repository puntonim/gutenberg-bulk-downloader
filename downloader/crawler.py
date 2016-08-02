import requests
from bs4 import BeautifulSoup

from exceptions import ThresholdReached
from utils.http import response_sanity_check


class GutenbergCrawler:
    def __init__(self, file_types, n_ebooks, langs):
        self.file_types = file_types or []
        self.n_ebooks = n_ebooks
        self.langs = langs or []
        self.download_urls = []

    def run(self):
        print(' * File types: {}'.format(self.file_types))
        print(' * Number of ebooks to download: {}'.format(self.n_ebooks))
        print(' * Language: {}'.format(self.langs))

        next_url = self._build_initial_url()
        print(' * Initial url: {}\n'.format(next_url))

        while True:
            r = requests.get(next_url)
            response_sanity_check(r)
            next_url = self._parse(r.content.decode('utf-8'))

            if next_url:
                continue
            break

    def _build_initial_url(self):
        # An url with multiple file types or langs has this form:
        # http://www.gutenberg.org/robot/harvest?&filetypes[]=mp3&filetypes[]=pdf&
        # langs[]=en&langs[]=de

        file_types_arg = ''
        for i in self.file_types:
            file_types_arg += '&filetypes[]={}'.format(i)

        langs_arg = ''
        for i in self.langs:
            langs_arg += '&langs[]={}'.format(i)

        return 'http://www.gutenberg.org/robot/harvest?{}{}'.format(file_types_arg, langs_arg)

    def _parse(self, html):
        soup = BeautifulSoup(html)
        next_url = None
        for p in soup.find_all('p'):
            if p.a:
                link = p.a.get('href')
                if p.a.text.lower() == 'next page':
                    next_url = 'http://www.gutenberg.org/robot/{}'.format(link)
                    continue
                self.download_urls.append(link)
                try:
                    self._check_n_ebooks()
                except ThresholdReached:
                    return None
        return next_url

    def _check_n_ebooks(self):
        if len(self.download_urls) >= self.n_ebooks:
            raise ThresholdReached('{} ebook links haven been collected.'.format(self.n_ebooks))
