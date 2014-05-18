"""
The protocol is described here:
http://www.gutenberg.org/wiki/Gutenberg:Information_About_Robot_Access_to_our_Pages
"""
import argparse

from downloader.crawler import GutenbergCrawler


def main(args):
    print('START.')
    crawler = GutenbergCrawler(args.file_type, args.n_ebooks, args.lang)
    crawler.run()
    print('END.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Downloads free ebooks from Project Gutenberg.")
    parser.add_argument('--file-type',
                        choices=['txt', 'pdf', 'html', 'epub.images', 'epub.noimages',
                                 'kindle.images', 'kindle.noimages', 'mp3'],
                        help='Filter by file types.', action='append')
    parser.add_argument('--lang', type=str,
                        help='Ebook language.', action='append')
    parser.add_argument('--n-ebooks', type=int, default=100,
                        help='Number of ebooks to download (default: 100).')
    args = parser.parse_args()
    main(args)