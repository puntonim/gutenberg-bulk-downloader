GUTENBERG-BULK-DOWNLOADER
=========================

Bulk downloader for free ebooks hosted at [Project Gutenberg](http://www.gutenberg.org/).

Follow the steps in order to create a *local development* copy in a Linux/Mac OS machine.

1. Create a project folder in your workspace
--------------------------------------------
    $ mkdir gutenberg-bulk-downloader
    $ cd gutenberg-bulk-downloader
We will refer to this folder as *repository root*.

2. Clone the reposiotry
-----------------------
    $ git clone https://github.com/nimiq/gutenberg-bulk-downloader.git .

3. Create a virtual environment
-------------------------------
You can create virtual environments using Virtualenvwrapper or Virtualenv.
I usually use Virtualenvwrapper in development and Virtualenv in production.

### 3.1. Using Virtualenvwrapper
    $ mkvirtualenv gutenberg-bulk-downloader

### 3.2. Using plain Virtualenv
    $ virtualenv ve

5. Install the requirements
---------------------------
    $ pip install -r requirements.txt

6. Run a download session
-------------------------
    $ python manage.py --f pdf --lang en --n 100

Appendix A. Command line parameters
-----------------------------------
    $ python manage.py --help
    usage: manage.py [-h]
                     [--file-type {txt,pdf,html,epub.images,epub.noimages,kindle.images,kindle.noimages,mp3}]
                     [--lang LANG] [--n-ebooks N_EBOOKS]

    Downloads free ebooks from Project Gutenberg.

    optional arguments:
      -h, --help            show this help message and exit
      --file-type {txt,pdf,html,epub.images,epub.noimages,kindle.images,kindle.noimages,mp3}
                            Filter by file types.
      --lang LANG           Ebook language.
      --n-ebooks N_EBOOKS   Number of ebooks to download (default: 100).

E.g. download .txt and .pdf files, English and German language, max 500 files:
    $ python manage.py --file-type pdf --file-type txt --lang en --lang de --n-ebooks 500