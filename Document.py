from bs4 import BeautifulSoup
from nltk import word_tokenize

"""
Stores information for a given Document (currently only Wikipedia articles)
"""


class Document:

    def __init__(self):
        self.title = None
        self.html = None
        self.pageid = None
        self.raw_text = None
        self.words = None
        self.categories = None
        self.links = None
        self.display_title = None

    """
    Converts the given JSON into a Document object
    """
    @staticmethod
    def document_from_json(json):
        document = Document()
        document.title = json['title']
        document.pageid = json['pageid']
        # Get HTML and extract words
        document.html = json['text']['*']
        soup = BeautifulSoup(document.html, 'html.parser')
        document.text = soup.get_text()
        # Extract words from raw text
        document.words = word_tokenize(document.text)
        document.categories = json['categories']
        document.links = json['links']
        document.display_title = json['displaytitle']
        return document
