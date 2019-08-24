# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    novel_name = scrapy.Field()
    author = scrapy.Field()
    cover = scrapy.Field()
    type = scrapy.Field()
    info = scrapy.Field()
    UPtime = scrapy.Field()
    chapter = scrapy.Field()
    mark = scrapy.Field()







