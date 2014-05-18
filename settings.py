from os.path import join, normpath, dirname


BASE_DIR = normpath(dirname(__file__))
STORAGE_PATH = normpath(join(BASE_DIR, '_storage'))