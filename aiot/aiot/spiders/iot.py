# -*- coding:utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import IotItem
from scrapy.selector import Selector


# 国家农业物联网
class IotSpider(CrawlSpider):
    name = "IotSpider"
    allowed_domains = ['iot-cn.org']
    start_urls = ['http://www.iot-cn.org']
    rules = [
        Rule(LinkExtractor(allow=('/news/show.php')),
             callback='parse_article',
             follow=True)
    ]

    def parse_article(self, response):
        # print(response.body)
        print(response.url)

