# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from scrapy.conf import settings
from pymongo.errors import DuplicateKeyError


class LyrikerPipeline(object):

    def __init__(self):

        mongo_credentials = settings['MONGODB']
        client = MongoClient(mongo_credentials)
        db = client.dsr
        self.lyrics_collection = db.lyrics

    def process_item(self, item, spider):
        try:
            self.lyrics_collection.insert({
                "artist": item["artist"],
                "song_name": item["song_name"],
                "lyrics": item["lyrics"],
                })
        except DuplicateKeyError:
            pass
        return item
