# -*- coding:utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from scrapy_aiot.aiot.aiot.items import AProductsPriceItem
from scrapy.selector import Selector
import re


# 全国农产品价格数据
class AProductsPriceSpider(CrawlSpider):
    name = 'AProductsPriceSpider'
    allowed_domains = ['mofcom.gov.cn']
    start_urls = ['http://nc.mofcom.gov.cn/channel/gxdj/jghq/jg_list.shtml']
    rules = [
        Rule(LinkExtractor(allow=('/par_craft_index/')),
             callback='parse_item',
             follow=True)
    ]

    def parse_item(self, response):
        all = response.xpath('//table[@class="s_table03"/tr]')
        for each in all:
            product_name = each.xpath('td[1]/text()').extract()[0]
            product_price = each.xpath('td[2]/text()').extract()[0]
            product_market = each.xpath('td[3]/a/text()').extract()[0]
            product_releasedate = each.xpath('td[4]/text()').extract()[0]

            print("product_name:", product_name)
            print("product_price:", product_price)
            print("product_market:", product_market)
            print("product_releasedate:", product_releasedate)


