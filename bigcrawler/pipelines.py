# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy import log
from scrapy.http import Request
from scrapy.item import BaseItem


class BigcrawlerPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, Request):
            log.msg('Pipeline: Request', level=log.DEBUG)
        elif isinstance(item, BaseItem):
            log.msg('Pipeline: BaseItem', level=log.DEBUG)
        return item
