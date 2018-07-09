# Standard Library Imports
# -----------------------------------------------------------------------------
import requests
from collections import Counter
import json
# Related Libraries Imports
# ----------------------------------------------------------------------------
from bs4 import BeautifulSoup
# Local Imports
# -----------------------------------------------------------------------------


class Panel:
    """Abstract class for panel.
    """
    def __init__(self):
        self.url = None
        self.url_content = None

    @staticmethod
    def get_url_content(url):
        """Request lib Validates url and returns GET request text content
        """
        r = requests.get(url)
        if r.status_code is 200:
            return r.text
        else:
            print("Unable to retrieve data. Following error occurred: {}".format(r.status_code))

    def calculate_price(self):
        """Base-class method for calculating price.
        Raises
        ------
        NotImplementedError
            This methods must be implemented in child classes
        """
        raise NotImplementedError("Subclasses should implement this!")


class PanelOne(Panel):
    """First panel implementation.

    Attributes
    ----------
    url: str
        Resources from WWW
    url_content: str
        Text returned by GET request.
    """
    def __init__(self):
        self.url = 'http://time.com'
        self.url_content = ''

    def calculate_price(self):
        """Calculate price for PanelOne. It depends on how many letters "a" can be found on class url site and divided by 100.
        """
        soup = BeautifulSoup(self.url_content)
        c = Counter(soup.p.text)
        price = c['a']/100.0
        return price

class PanelTwo(Panel):
    """PanelTwo implementation
    """
    def __init__(self):
        self.url = 'http://openlibrary.org/earch.json?q=the+lord+of+the+rings'
        self.url_content = ''

    def calculate_price(self):
        """Calculate price for PanelTwo. It depends on how many arrays with more than 10 elements can be found in class URL. LOTR link was brokem, so I decided just ot count elements equal, larger than 3.
        """
        # lists_in_json = []
        # _data = json.loads(self.url_content)

        price = 0# self.extract_lists()
        return price

    def extract_lists(self):
        # TODO Recursive dictionary walk and lists len extraction
        pass


class PanelThree(Panel):
    """PanelThree implementation
    """
    def __init__(self):
        self.url = 'http://time.com'
        self.url_content = ''

    def calculate_price(self):
        """Calculates price for PanelThree. It depends on amount of html nodes found int the class url divided by 100
        """

        soup = BeautifulSoup(self.url_content)
        price = len(soup.find_all('html'))/100.0
        return price

