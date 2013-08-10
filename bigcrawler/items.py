# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class NewsWeb(Item):
    visit_id = Field()
    visit_status = Field()
    title = Field()
    url = Field()
