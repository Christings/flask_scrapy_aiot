# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# chinacwa——中国智慧农业网
class ChinacwaItem(scrapy.Item):
    # 文章标题、关键字、图片地址、摘要、内容地址、内容
    article_id = scrapy.Field()
    article_title = scrapy.Field()
    article_keywords = scrapy.Field()
    article_imageurl = scrapy.Field()
    article_abstract = scrapy.Field()
    article_url = scrapy.Field()
    article_content = scrapy.Field()


# iot——国家农业物联网
class IotItem(scrapy.Item):
    article_id = scrapy.Field()
    article_title = scrapy.Field()
    article_keywords = scrapy.Field()
    article_abstract = scrapy.Field()
    article_url = scrapy.Field()
    article_content = scrapy.Field()


# ny135——中国农业物联网
class Ny135Item(scrapy.Item):
    article_id = scrapy.Field()
    article_title = scrapy.Field()
    article_keywords = scrapy.Field()
    article_abstract = scrapy.Field()
    article_url = scrapy.Field()
    article_content = scrapy.Field()


# productprice——农产品价格
class ProductpriceItem(scrapy.Item):
    product_name = scrapy.Field()
    product_lowestprice = scrapy.Field()
    product_averageprice = scrapy.Field()
    product_highestprice = scrapy.Field()
    product_specification = scrapy.Field()
    product_unit = scrapy.Field()
    product_releasedate = scrapy.Field()
