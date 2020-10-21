# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo ,re,pymysql

class MongoPipeline(object):
    def __init__(self, Mongo_url , Mongo_DB):
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

class MySqlPipeline(object):

    def __init__(self, MYSQL_HOST, MYSQL_DB, MYSQL_PWD, MYSQL_USER ):
        self.MYSQL_HOST=MYSQL_HOST
        self.MYSQL_DB = MYSQL_DB
        self.MYSQL_PWD = MYSQL_PWD
        self.MYSQL_USER = MYSQL_USER


    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            MYSQL_HOST=crawler.settings.get('MYSQL_HOST'),
            MYSQL_DB=crawler.settings.get('MYSQL_DB'),
            MYSQL_PWD=crawler.settings.get('MYSQL_PWD'),
            MYSQL_USER=crawler.settings.get('MYSQL_USER')

        )

    def open_spider(self, spider):
        self.connection = pymysql.connect(host=self.MYSQL_HOST,
                                          user=self.MYSQL_USER,
                                          db=self.MYSQL_DB,
                                          passwd=self.MYSQL_PWD)
        self.cursor =self.connection.cursor()

    def process_item(self, item, spider):
        if spider.name == 'biqu':
            if item['mark'] == 1:
                insert_sql = "INSERT INTO novel_list(" \
                             "novel_id, " \
                             "novel_name, " \
                             "novel_author, " \
                             "novel_type, " \
                             "novel_info, " \
                             "novel_cover," \
                             " novel_uptime," \
                             " novel_source )" \
                             " VALUES( '%s','%s','%s','%s','%s','%s','%s','%s')" % \
                             (
                                 item['_id'],
                                 item['novel_name'],
                                 item['author'],
                                 item['type'],
                                 item['info'],
                                 item['cover'],
                                 item['UPtime'],
                                 item['novel_source'],
                              )
                try:
                    self.cursor.execute(insert_sql)
                    self.connection.commit()
                except:
                    self.connection.rollback()
                ...
            else:
                chapter = item['chapter']
                insert_sql_chapter ="INSERT INTO novel_chapter (" \
                                    "chapter_id," \
                                    "novel_id, " \
                                    "chapter_title, " \
                                    "chapter_url, " \
                                    "chapter_content)" \
                                    "VALUES('%s','%s','%s','%s','%s')" % \
                                    (
                                        chapter['chapter_id'],
                                        chapter['novel_id'],
                                        chapter['chapter_title'],
                                        chapter['chapter_url'],
                                        chapter['chapter_content'],
                                    )
                try:
                    self.cursor.execute(insert_sql_chapter)
                    self.connection.commit()
                except:
                    self.connection.rollback()

    def close_spider(self, spider):
        self.connection.close()


