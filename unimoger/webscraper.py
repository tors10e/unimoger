from html.parser import HTMLParser
import requests
from bs4 import BeautifulSoup

class WebScraper(object):

    def __init__(self, url, city):
        self.url = url
        self.city = city
        self.unimogs = {}

    def get_html_doc(self):
        response = requests.get(self.url)
        return response.text

    def parse_html(self):
        html_doc = self.get_html_doc()
        return BeautifulSoup(html_doc, 'html.parser')

    def get_urls_from_doc(self):
        parsed_doc = self.parse_html()
        urls = {}
        for link in parsed_doc.find_all('a'):
            classes = link.get('class')
            if classes:
                if classes[0] == 'result-title':
                    urls.update({link.string: link.get('href')})
        return urls

    def print_results(self):
        urls = self.get_urls_from_doc()
        for k,v in urls.items():
            print('City:{0} Title: {1} Url: {2}'.format(self.city, k, v))
