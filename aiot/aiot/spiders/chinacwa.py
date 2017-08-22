# -*- coding:utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from ..items import ChinacwaItem
from scrapy.selector import Selector
import re


class ChinacwaSpider(CrawlSpider):
    name = 'ChinacwaSpider'
    allowed_domains = ['chinacwa.com']
    start_urls = ['http://www.chinacwa.com']
    rules = [
        Rule(LinkExtractor(allow=('/chcontents/')),
             callback='parse_item',
             follow=True)
    ]

    # def parse_url(self, response):
    #     # print(response.body)
    #     # item = ChinacwaItem()
    #     sel = Selector(response)
    #     url = str(response.url)
    #     # print("level_url:", level1_url)
    #     # level1_name = sel.xpath('//div[@class="container"]/div[1]/a/text()').extract()
    #     # print("level1_name:", level1_name)
    #     yield scrapy.Request(url, callback=self.parse, meta={'url': url})

    def parse_item(self, response):
        item = ChinacwaItem()
        sel = Selector(response)
        # 文章标题、关键字、图片地址、摘要、内容地址、内容
        # route=sel.xpath('//div[@class="content"]/div[@class="content_left"]')
        article_title = sel.xpath(
            '//div[@class="content"]/div[@class="content_left"]/div[1]/div[1]/h3/text()').extract()
        print("article_title:", article_title)
        article_keywords = sel.xpath(
            '//div[@class="content"]/div[@class="content_left"]/div[1]/div[1]/p/text()').extract()
        print("article_keywords:", article_keywords)
        # article_imageurl = sel.xpath(
        #      '//div[@class="content"]/div[@class="content_left"]/div[1]/div[1]/div[2]/p/img/@src').extract()
        # print("article_imageurl:", article_imageurl)

        # article_abstract = sel.xpath(
        #      '//div[@class="content"]/div[@class="content_left"]/div[1]/div[1]/div[2]/p[2]').xpath('string(.)').extract()
        # print("article_abstract:", article_abstract)
        article_url = response.url

        # p = r'<div class="conten">(.+?)</div>'
        # patternr1 = re.compile(p)
        # print("aaa:", patternr1.findall(r'str(sel)'))
        article_content = sel.xpath(
            '//div[@class="content"]/div[@class="content_left"]/div[1]/div[1]/div[2]/p').xpath('string(.)').extract()
        print("article_content:", article_content)
        item['article_title'] = article_title
        item['article_keywords'] = article_keywords
        item['article_url'] = article_url
        item['article_content'] = article_content
        yield item
