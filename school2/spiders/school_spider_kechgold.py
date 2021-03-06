# making a spider to crawl

# import the required packages and our item
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from school2.items import School2Item
from scrapy.conf import settings


# start with hard coding in a school, can functionalise later to get school info from a list
class SchoolSpider(CrawlSpider): # based on inbuilt CrawlSpider class
# tells spider how deep (think: 1.com/2/3) into website to go, see documentation for more on overriding scrapy middleware settings
    def __init__(self):
        settings.overrides['DEPTH_LIMIT'] = 6
    name = "kechg" # give the instance of the class a name - would be the name/urn of each school, this is what we use to intiate the crawl from terminal
    allowed_domains = ["kechg.org.uk"] # restrict to crawling on pages beginning with the schools URL, can also use setting to do this...
    start_urls = [
    "http://www.kechg.org.uk",
    "http://www.kechg.org.uk/departments"
    ] # url to start crawling from
 
    rules = [Rule(LinkExtractor(allow=['/+']), 'parse_page')] # only crawl urls which are the allowed domain + this, here it's just "/" so anything goes
# the response object from this, the urls, is passed to the "parse_page" method below
 
    def parse_page(self, response):
        page = School2Item()
        page['url'] = response.url
        page['pagetitle'] = response.xpath("//title/text()").extract() # title nodes?
        #page['sometext'] = response.css("//a[contains(text(),'school')]").extract()
        #print # garbage, just chekcing something is happening
        return page 
        # tried return page['ur'l] <-- it doesn't work!!


