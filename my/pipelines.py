# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo ,re

class MongoPipeline(object):
    def __init__(self, Mongo_url, Mongo_DB):
        self.Mongo_url= Mongo_url
        self.Mongo_DB= Mongo_DB

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            Mongo_url = crawler.settings.get('MONGO_URL'),
            Mongo_DB= crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client =pymongo.MongoClient(self.Mongo_url)
        self.db=self.client[self.Mongo_DB]

    def process_item(self, item, spider):
        """
         数据清理
        :param item:
        :param spider:
        :return:
        """
        if spider.name == 'biqu':
            if item['mark'] == 1:
                self.db['novel_list'].insert(dict(item))
            else:
                self.db['novel_chapter'].insert(dict(item['chapter']))
        return item

    def close_spider(self, spider):
        self.client.close()