# -*- coding:utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy_aiot.aiot.aiot.items import ProductpriceItem
from scrapy.selector import Selector


class ProductpriceSpider(CrawlSpider):
    name = 'ProductpriceSpider'
    allowed_domain = ['xinfadi.com.cn']
    start_urls = ['http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml']

    def parse_item(self, response):
        sel = Selector(response)

        all = sel.xpath('//table[@class="hq_table"]/tbody/tr')
        for each in all:
            product_name = each.xpath('td[1]/text()').extract()
            product_lowestprice = each.xpath('td[2]/text()').extract()
            product_averageprice = each.xpath('td[3]/text()').extract()
            product_highestprice = each.xpath('td[4]/text()').extract()
            product_specification = each.xpath('td[5]/text()').extract()
            product_unit = each.xpath('td[6]/text()').extract()
            product_releasedate = each.xpath('td[7]/text()').extract()

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
