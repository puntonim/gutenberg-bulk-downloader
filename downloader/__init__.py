from os.path import exists, join, normpath
from os import mkdir
import requests

from utils.http import response_sanity_check


class FileDownloader:
    def __init__(self, urls, storage_path):
        self.urls = urls
        self.storage_path = self._init_storage_path(storage_path)

    def run(self):
        for url in self.urls:
            print('Downloading {}... '.format(url), end='')
            r = requests.get(url, stream=True)
            response_sanity_check(r)

            file_name = url.split('/')[-1]  # e.g. '8ench10.zip'
            local_path = normpath(join(self.storage_path, file_name))
            with open(local_path, 'wb') as f:
                for chunk in r.iter_content(102400):  # Read 100Kb per chunk.
                    f.write(chunk)
            print('Done.')

    def _init_storage_path(self, storage_path):
        if not exists(storage_path):
            mkdir(storage_path)
        return storage_path