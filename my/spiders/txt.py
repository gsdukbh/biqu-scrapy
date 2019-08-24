# -*- coding: utf-8 -*-
import scrapy


class TxtSpider(scrapy.Spider):
    name = 'txt'
    allowed_domains = ['werls.top']
    start_urls = ['http://werls.top/']

    def parse(self, response):
        pass
