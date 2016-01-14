# -*- coding: utf-8 -*-
# 15/12/2015
# items.py file for school2 scraping project 
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


import scrapy

from scrapy.item import Item, Field


class School2Item(scrapy.Item):
	sometext = scrapy.Field()
	pagetitle = scrapy.Field()
	url = scrapy.Field()
	soup = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
	pass

