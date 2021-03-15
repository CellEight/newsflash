class siteParser:
    """ Abstract site data type that all specific site parsers will inherit 
        defines the key methods all these child classes must implement """
    def __init__(self):
        self.domain = None

    def parsePage(self, bs_page):
        """ This function when implemented by child classes will take a beautiful soup 
            object derived form a web page of the associated site and attempt to extract 
            the text of the article present on the page"""
        raise NotImplementedError

    def getTopicLinks(self, topic):
        """ This function when implemented by child classes will take a topic and scrape 
            the associated website to generate a list of articles related to that topic"""
        raise NotImplementedError

    def clean(self, text):
        return BeautifulSoup(text, 'lxml').text
