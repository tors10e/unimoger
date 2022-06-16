from unimoger.webscraper import WebScraper
from unimoger import config

vehicle = 'unimog'
max_price = '150001'

for city in config.cities:
    query_string = 'https://{0}.craigslist.org/search/cta?query={1}&srchType=T&max_price={2}'.format(city, vehicle, max_price)
    scraper = WebScraper(query_string, city)
    scraper.print_results()

print('***** Report Complete *****')
