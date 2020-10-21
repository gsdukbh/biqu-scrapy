# -*- coding: utf-8 -*-
import scrapy, re
import time, logging
from my.items import MyItem

logger = logging.getLogger(__name__)


class BiquSpider(scrapy.Spider):
    name = 'biqu'
    allowed_domains = ['biqiuge.com']
    paqu_urls = 'https://www.biqiuge.com'
    start_urls = ['https://www.biqiuge.com/book/1']
    max_page = 2
    start_fiction = 1

    # def start_requests(self):
    #     for page in range(1,self.max_page+1):
    #         url = '{url}/book/{num}'.format(url=self.paqu_urls, num=page)
    #         yield scrapy.Request(url=url)

    def parse(self, response):
        """
        图书章节获取
        :param response:
        :return:
        """
        try:
            self.logger.info('---爬虫开始---')
            if response.status == 200:
                cover = response.xpath('//div[@class="cover"]/img').re('.*?"(.*?)".*?alt')
                novel_name = response.xpath('//div[@class="info"]//h2/text()').get()
                author_ = response.xpath('//div[@class="small"]/span/text()').get()
                chapter_url = response.xpath('//div[@class="listmain"]//dd[position()>6]').re('.*?href="(.*?)">.*?</a>')
                type = response.xpath('//div[@class="small"]/span[2]/text()').get()
                info_ = response.xpath('//div[@class="intro"]/text()').get()
                UPtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                num = response.xpath('//div[@class="path"]/div').re('.*?k/(.*?)/')
                author = author_[3:]
                info = info_[3:]
                type = type[3:]
                self.logger.info('---正在爬取小说:' + novel_name)
                items = MyItem()

                items['_id'] = num[0]
                items['novel_name'] = novel_name
                items['author'] = author
                items['UPtime'] = UPtime
                items['type'] = type
                items['cover'] = self.paqu_urls + cover[0]
                items['info'] = info
                items['mark'] = 1
                items['novel_source'] = response.url
                yield items

                for content in range(len(chapter_url)):
                    urls = '{url}{chapter_url}'.format(url=self.paqu_urls, chapter_url=chapter_url[content])
                    items['chapter_id'] = content
                    yield scrapy.Request(url=urls,
                                         callback=self.parse_hapet,
                                         meta={'items': items, 'novelName': novel_name})

                next_url = '{url}/book/{num}'.format(url=self.paqu_urls, num=int(num[0]) + 1)
                yield scrapy.Request(url=next_url)
            else:
                self.logger.info('url访问失败，重新尝试' + response.url)
                scrapy.Request(url=response.url)
        except:
            logger.warning('*' * 10)

    def parse_hapet(self, response):
        """
        章节详情页处理
        :param response:
        :return: items
        """
        items = response.meta['items']
        chapter_contents = response.xpath('//div[@id="content"]').re('.*?showtxt">(.*?)https')
        chapter_title = response.xpath('//div[@class="content"]//h1/text()').get()
        chapter_content = re.sub('<br>', '\n', chapter_contents[0])
        items['mark'] = 0
        self.logger.info('---正在爬取：' + response.meta['novelName'] + '的章节：' + chapter_title)
        # 构造字典
        items['chapter'] = {
            'chapter_id': items['chapter_id'],
            'novel_id': items['_id'],
            'chapter_title': chapter_title,
            'chapter_url': response.url,
            'chapter_content': chapter_content
        }

        yield items
