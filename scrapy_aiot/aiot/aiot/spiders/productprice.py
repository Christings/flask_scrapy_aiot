# -*- coding:utf-8 -*-

import scrapy
from scrapy.spiders import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy_aiot.aiot.aiot.items import ProductpriceItem
from scrapy.selector import Selector


class ProductpriceSpider(Spider):
    name = 'ProductpriceSpider'
    allowed_domain = ['xinfadi.com.cn']
    start_urls = ['http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml']

    page_link = set()  # 保存下一页页面的url

    def parse(self, response):


        all = response.xpath('//table[@class="hq_table"]/tr[@class="tr_color"]')
        for each in all:
            product_name = each.xpath('td[1]/text()').extract()[0]
            product_lowestprice = each.xpath('td[2]/text()').extract()[0]
            product_averageprice = each.xpath('td[3]/text()').extract()[0]
            product_highestprice = each.xpath('td[4]/text()').extract()[0]
            product_specification = each.xpath('td[5]/text()').extract()[0]
            product_unit = each.xpath('td[6]/text()').extract()[0]
            product_releasedate = each.xpath('td[7]/text()').extract()[0]

            print("product_name:", product_name)
            print("product_lowestprice:", product_lowestprice)
            print("product_averageprice:", product_averageprice)
            print("product_highestprice:", product_highestprice)
            print("product_specification:", product_specification)
            print("product_unit:", product_unit)
            print("product_releasedate:", product_releasedate)

            item = ProductpriceItem(product_name=product_name, product_lowestprice=product_lowestprice,
                                    product_averageprice=product_averageprice,
                                    product_highestprice=product_highestprice,
                                    product_specification=product_specification,
                                    product_unit=product_unit, product_releasedate=product_releasedate)
            yield item
        next_page = response.xpath('//div[@class="manu"]/a/@href').extract()[-2]
        print(next_page)
        if next_page:
            next_page="http://www.xinfadi.com.cn/"+next_page
            self.page_link.add(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)
