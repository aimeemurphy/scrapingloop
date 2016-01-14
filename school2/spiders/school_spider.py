# making a spider to crawl

# import the required packages and our item
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from school2.items import School2Item
from scrapy.conf import settings
from BeautifulSoup import BeautifulSoup
import re
import time


# experimenting with making the school and url functions
# name the spider - update to urn later
a = "kngs1"
# declare the website
b = "http://www.kngs.co.uk"
# from the website, construct the allowed domains *** need to consider whether is always going to be the right way to do it
c = re.search("www",b)
print c
d = "kngs.co.uk"


# start with hard coding in a school, can functionalise later to get school info from a list
class SchoolSpider(CrawlSpider): # based on inbuilt CrawlSpider class
# tells spider how deep (think: 1.com/2/3) into website to go, see documentation for more on overriding scrapy middleware settings
    #def __init__(self):
    settings.overrides['DEPTH_LIMIT'] = 1 # depth limit works
    name = a # give the instance of the class a name - would be the name/urn of each school, this is what we use to intiate the crawl from terminal
    allowed_domains = [d] # restrict to crawling on pages beginning with the schools URL, can also use setting to do this...
    start_urls = [
    b
    ] # url to start crawling from
    rules = [Rule(LinkExtractor(allow=['/+']), 'parse_page', follow=True)] 
    # only crawl urls which are the allowed domain + this, here it's just "/" so anything goes
    # follow=True tells it to scrape the links it scrapes
    # the response object from this, the urls, is passed to the "parse_page" method below
 
    def parse_page(self, response):
        page = School2Item()
        page['url'] = response.url
        page['pagetitle'] = response.xpath("//title/text()").extract() # title nodes?
        #page['soup'] = BeautifulSoup(response.body)
        #page['sometext'] = response.css("//a[contains(text(),'school')]").extract()
        #print # garbage, just chekcing something is happening
        time.sleep(0.1) #pauses between successful scrapes (not errors or ignores), to stop website being overloaded
        return page 
        # tried return page['ur'l] <-- it doesn't work!!

print c
