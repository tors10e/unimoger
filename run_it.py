from unimoger.webscraper import WebScraper
from unimoger import config

vehicle = 'unimog'
max_price = '15001'

for city in config.cities:
    scraper = WebScraper('https://{0}.craigslist.org/search/cta?query={1}&max_price={2}'.format(city, vehicle, max_price))
    scraper.print_results()
