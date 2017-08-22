# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings

# 中国智慧农业网
class ChinacwaPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])
        self.db = self.client[settings['MONGO_DB']]
        self.coll = self.db[settings['MONGO_COLL']]

    def process_item(self, item, spider):
        if item['article_title']:
            postItem = dict(item)
            self.coll.insert(postItem)
            print("插入成功")
            return item
