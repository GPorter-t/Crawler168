# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter

from Crawler168.items import Mp3Item


class Crawler168Pipeline:
    def process_item(self, item, spider):
        return item


class Mp3Pipeline:
    def process_item(self, item, spider):
        if isinstance(item, Mp3Item):
            spider.redis.sadd("crawler168:recreator:bgm_url", json.dumps(dict(item), ensure_ascii=False))
            return item