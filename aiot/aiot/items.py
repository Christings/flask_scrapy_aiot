# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# chinacwa——中国智慧农业网
class ChinacwaItem(scrapy.Item):
    # 文章标题、关键字、图片地址、摘要、内容地址、内容
    article_title = scrapy.Field()
    article_keywords = scrapy.Field()
    article_imageurl = scrapy.Field()
    article_abstract = scrapy.Field()
    article_url = scrapy.Field()
    article_content = scrapy.Field()


# iot——国家农业物联网
class IotItem(scrapy.Item):
    article_title = scrapy.Field()
    article_keywords = scrapy.Field()
    article_url = scrapy.Field()
    article_content = scrapy.Field()
