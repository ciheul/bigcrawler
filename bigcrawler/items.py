# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class NewsItem(Item):
    visit_id = Field()
    visit_status = Field()
    url = Field()
    html = Field()
    content = Field()
    #title = Field()
