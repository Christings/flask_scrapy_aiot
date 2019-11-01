# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
# from scrapy.conf import settings
from .items import ChinacwaItem
from .items import IotItem
from .items import Ny135Item
from scrapy_aiot.aiot.aiot.items import ProductpriceItem
from scrapy_aiot.aiot.aiot.items import AllProductsPriceItem
from scrapy.utils.project import get_project_settings
settings = get_project_settings()


# 农业物联网
class AiotPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        self.db = self.client[settings['MONGO_DB']]
        # self.coll = self.db[settings['MONGO_COLL2']]
        self.chinacwa = self.db['chinacwa']
        self.iot = self.db['iot']
        self.ny135 = self.db['ny135']
        self.productprice = self.db['productprice']
        self.allproductprice = self.db['allproductprice']

    def process_item(self, item, spider):
        if isinstance(item, ChinacwaItem):
            try:
                if item['article_title']:
                    item = dict(item)
                    self.chinacwa.insert(item)
                    print("插入成功")
                    return item
            except Exception as e:
                spider.logger.exceptionn("")
        elif isinstance(item, IotItem):
            try:
                if item['article_title']:
                    item = dict(item)
                    self.iot.insert(item)
                    print("成功")
                    return item
            except Exception as e:
                spider.logger.exceptionn("")
        elif isinstance(item, Ny135Item):
            try:
                if item['article_title']:
                    item = dict(item)
                    self.ny135.insert(item)
                    print("插入")
                    return item
            except Exception as e:
                spider.logger.exceptionn("ny135存储失败")
        elif isinstance(item, ProductpriceItem):
            try:
                if item["product_name"]:
                    item = dict(item)
                    self.productprice.insert(item)
                    print("农产品价格数据")
                    return item
            except Exception as e:
                spider.logger.exceptionn("农产品价格数据存储失败")
        elif isinstance(item, AllProductsPriceItem):
            try:
                if item["product_name"]:
                    item = dict(item)
                    self.allproductprice.insert(item)
                    print("全国农产品价格数据")
                    return item
            except Exception as e:
                spider.logger.exceptionn("全国农产品价格数据存储失败")
