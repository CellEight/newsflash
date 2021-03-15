import requests
from urlparser import urlparser
from itertools import cycle
# import site specific parsing methods
from sites import sites


class newsflash(nn.Module):
    """ NewsFlash is a python library to scrape articles form a variety of news sources 
        and return them in an easily parsable format for further processing """
    def __init__():
        pass

    def scrapePage(self, url):
        """  Scrape the article found at the specified url """
        raw_page = requests.get(url)
        site = self.getSite(url)
        bs_page = BeautifulSoup(raw_page.content, 'html.parser')
        page = site.parsePage(bs_page)
        return page

    def scrapeTopic(self, topic, num_articles, sources=list(site.all_sites)):
        """ Scrape specified number of articles on given topic from given sites. """ 
        pass

    def getSite(self, url):
        """ Parse the given url to get the name of the site. """
        hostname = urlparse(urlparser).hostname
        site = sites.getSite(hostname)
        return site
