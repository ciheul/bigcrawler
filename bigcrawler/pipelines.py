# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy import log
from scrapy.http import Request
from scrapy.item import BaseItem
from scrapy.exceptions import DropItem

from HTMLParser import HTMLParser


##### Pipeline classes #####

class NoHTMLPipeline(object):
    """Drop any item that has unnecessary data."""
    def process_item(self, item, spider):
        if not 'html' in item or not 'content' in item:
            raise DropItem("Drop item that has no HTML")
        return item


class WordCounterPipeline(object):
    """WordCounter will proceed after crawled pages stored in repository."""
    def process_item(self, item, spider):
        if len(item['content'].split()) < 50:
            raise DropItem("Drop item that has number of words less than 30: %s" \
                    % item['url'])
        return item


class ItemCleanserPipeline(object):
    """Drop a part of information in an item."""
    def process_item(self, item, spider):
        del item['visit_status']
        del item['content']
        return item


class HTMLCleanserPipeline(object):
    """Parsing will proceed after crawled pages stored in repository."""
    def process_item(self, item, spider):
        if item['content'] != "":
            temp = strip_tags(item['content'])
            item['content'] = " ".join(temp.split())
            # TODO remove page with no content
            #log.msg("item content: %s" % item['content'])
            return item
        else:
            log.msg("DropRaise. url: %s" % item['url'])
            raise DropItem("Drop item with no content: %s " % item['url'])

         
##### Additional classes & methods ##### 

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
