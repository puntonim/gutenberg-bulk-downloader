from os import listdir, remove
from os.path import join, normpath
from utils.zip import unzip


class FolderItemsUnzipper:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def run(self):
        for file in listdir(self.folder_path):
            if not file[-4:].lower() == '.zip':
                continue
            zip_file_path = normpath(join(self.folder_path, file))
            print('Unzipping {}... '.format(file), end='')
            unzip(zip_file_path, self.folder_path)
            remove(zip_file_path)
            print('Done.')