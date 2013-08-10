from scrapy import log
from scrapy.http import Request
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.utils.request import request_fingerprint
from bigcrawler.items import NewsWeb
from bigcrawler.middlewares.ignore import IgnoreVisitedItems


class DetikSpider(BaseSpider):
    """Crawl detik.com"""
    name = 'detik'
    allowed_domains = ['detik.com']
    start_urls = ['http://www.detik.com']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        response_news = NewsWeb()
        response_news['url'] = response.url
        title = hxs.select('//h1/text()').extract()
        if title != []:
            response_news['title'] = title.pop().strip()
        else:
            response_news['title'] = ""
        yield response_news

        # other next-crawled-news are stored in tag 'a'
        sites = hxs.select('//a')
        for site in sites:
            url = site.select('@href').extract().pop()
            if url.startswith('#'):
                continue

            yield Request(url, callback=self.parse,
                          meta={IgnoreVisitedItems.FILTER_VISITED: True})
