# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
from .items import ChinacwaItem
from .items import IotItem
from .items import Ny135Item


# chinacwa——中国智慧农业网
class ChinacwaPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])
        self.db = self.client[settings['MONGO_DB']]
        self.coll = self.db[settings['MONGO_COLL']]

    def process_item(self, item, spider):
        if isinstance(item, ChinacwaItem):
            if item['article_title']:
                postItem = dict(item)
                self.coll.insert(postItem)
                print("插入成功"),
                return item


# iot——国家农业物联网
class IotPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        self.db = self.client[settings['MONGO_DB']]
        self.coll = self.db[settings['MONGO_COLL1']]

    def process_item(self, item, spider):
        if isinstance(item, IotItem):
            if item['article_title']:
                postItem = dict(item)
                self.coll.insert(postItem)
                print("插入")
                return item


# ny135——中国农业物联网
class Ny135Pipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        self.db = self.client[settings['MONGO_DB']]
        self.coll = self.db[settings['MONGO_COLL2']]

    def process_item(self, item, spider):
        if isinstance(item, Ny135Item):
            if item['article_title']:
                postItem = dict(item)
                self.coll.insert(postItem)
                print("lala")
                return item
