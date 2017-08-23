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
        item = IotItem()
        sel = Selector(response)
        article_title = sel.xpath('//div[@class="m"]/div[1]/div[@class="left_box"]/h1[@id="title"]/text()').extract()
        article_keywords = sel.xpath(
            '//div[@class="m"]/div[1]/div[@class="left_box"]/div[@class="keytags"]/a/text()').extract()
        article_abstract = sel.xpath(
            '//div[@class="m"]/div[1]/div[@class="left_box"]/div[@class="introduce"]/text()').extract()
        article_url = response.url
        article_content = sel.xpath(
            '//div[@class="m"]/div[1]/div[@class="left_box"]/div[@id="content"]/div').xpath('string(.)').extract()

        item['article_title'] = article_title
        item['article_keywords'] = article_keywords
        item['article_abstract'] = article_abstract
        item['article_url'] = article_url
        item['article_content'] = article_content

        print("article_title:", article_title)
        print("article_keywords:", article_keywords)
        print("article_abstract:", article_abstract)
        print("article_url:", article_url)
        print("article_content:", article_content)

        yield item
