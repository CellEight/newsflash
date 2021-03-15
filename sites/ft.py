from sites.siteParser import *

class ftParser(siteParser):
    """ Class to facilitate scraping of ft.come the website of the London 
        based financial news paper"""
    def __init__(self):
        super().__init__()
        self.domain = "ft.com"

    def parsePage(self, bs_page):
        """ div, class ="article__content-body"
            all <p> tags
            get rid of hyperlinks and unicode chars """
        body = bs_page.find('div',class_='article__content-body')
        p_tags = body.find_all('p')
        page = ""
        for p in p_tags:
            page += self.clean(p.text) + "\n"
        return page

