from Document import *
import requests

"""
Performs all necessary networking operations within the application
"""


class Networking:

    """
    Initialises the class with the basic information necessary for the Wikipedia API
    """
    def __init__(self):
        self.base_url = "https://en.wikipedia.org/w/api.php?"

    """
    Fetches the Wikipedia article with the given title.
    Uses action=parse in the Wikipedia API in order to obtain a parsed form of the article
    Returns a Document object holding the parsed information
    """
    def fetch_parsed_article(self, title):
        end_point = self.base_url + "action=parse&" + "page=" + title + "&format=json"
        result = requests.get(end_point)
        json = result.json()
        return Document.document_from_json(json['parse'])
