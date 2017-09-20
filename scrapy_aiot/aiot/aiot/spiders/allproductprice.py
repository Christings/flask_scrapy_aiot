# -*- coding:utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from scrapy_aiot.aiot.aiot.items import AllProductsPriceItem
from scrapy.selector import Selector
import re


# 全国农产品价格数据
class AllProductsPriceSpider(CrawlSpider):
    name = 'AllProductsPriceSpider'
    # allowed_domains = ['nc.mofcom.gov.cn/channel/']
    start_urls = [
        'http://nc.mofcom.gov.cn/channel/gxdj/jghq/jg_list.shtml']

    # start_urls = [
    #     'http://nc.mofcom.gov.cn/channel/gxdj/jghq/jg_list.shtml?craft_index=13196&par_craft_index=13080']

    # rules = [
    #     Rule(LinkExtractor(allow=('/')),
    #          callback='parse_item',
    #          follow=True)
    # ]

    # 提取出全国所有农产品的url
    def parse(self, response):
        urls = response.xpath('//div[@class="s_Lmain clearfix"]/script/text()').extract()
        for url in urls:
            url = url.split('|')
            for each in url:
                product_url_tmp1 = re.findall(r"href=(.*?)>", str(each))
                product_url2 = str(product_url_tmp1).replace('[', '').replace(']', '').replace('\'', '')
                # print(product_url)
                product_url = 'http://nc.mofcom.gov.cn' + product_url2
                if product_url or product_url != "":
                    yield scrapy.Request(url=product_url, callback=self.parse_item)

    def parse_item(self, response):
        products = response.xpath('//div[@class="pmCon"]/table/tbody/tr')
        for each in products:
            product_name = each.xpath('td[1]/text()').extract()[0]
            product_price = each.xpath('td[2]/text()').extract()[0]
            product_market = each.xpath('td[3]/a/text()').extract()[0]
            product_releasedate = each.xpath('td[4]/text()').extract()[0]

            print("product_name:", product_name)
            print("product_price:", product_price)
            print("product_market:", product_market)
            print("product_releasedate:", product_releasedate)
            item = AllProductsPriceItem(product_name=product_name, product_price=product_price,
                                        product_market=product_market, product_releasedate=product_releasedate)
            yield item
        next_page_string = response.xpath('//div[@class="pmCon"]/script/text()').extract()
        next_page_temp = re.findall(r"v_PageCount = (.*?);", str(next_page_string))
        next_page = str(next_page_temp).replace('[', '').replace(']', '').replace('\'', '')
        print("next_page:", next_page)
        for i in range(2,int(next_page)):
            print(response.url)
            url = response.url + "&page=" + str(i)
            print("url:", url)
            yield scrapy.Request(url=url, callback=self.parse_item)
