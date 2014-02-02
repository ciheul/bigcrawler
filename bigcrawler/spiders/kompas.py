from scrapy import log
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.selector import HtmlXPathSelector
from bigcrawler.items import NewsItem
from bigcrawler.middlewares.spider.ignore import IgnoreVisitedItems
#from readability.readability import Document
from boilerpipe.extract import Extractor
import zlib
from bson.binary import Binary

class KompasSpider(CrawlSpider):
    name = "news"

    allowed_domains = [
        'kompas.com',
    ]

    start_urls = [
        'http://www.kompas.com',
    ]

    rules = (Rule(SgmlLinkExtractor(
                      deny_domains=['login.kompas.com',],
                      deny=['logins.php', 'reg.php', 'next',],
                      restrict_xpaths=('*')),
                  callback='parse_item',
                  follow=True),)

    def parse_item(self, response):
        response_news = NewsItem()
        response_news['url'] = response.url
        response_news['html'] = Binary(zlib.compress(response.body, 9))
        extractor = Extractor(extractor='ArticleExtractor', html=response.body)
        response_news['content'] = extractor.getText()
        return response_news


    #def parse(self, response):
    #    sel = Selector(response)

    #    # 'return-like' an item to generator
    #    response_news = NewsItem()
    #    response_news['url'] = response.url
    #    response_news['html'] = Binary(zlib.compress(response.body, 9))
    #    #response_news['title'] = Document(response.body).short_title()
    #    extractor = Extractor(extractor='ArticleExtractor', html=response.body)
    #    response_news['content'] = extractor.getText()
    #    #response_news['html'] = extractor.getHTML()
    #    yield response_news

    #    # other 'next-crawled-news' are stored in tag <a>
    #    urls = set(sel.xpath('//a/@href').extract())
    #    for url in urls:
    #        if url.startswith('#') or 'javascript' in url:
    #            continue
    #        elif url.lower().endswith(('.jpeg', 'jpg', 'png', '.pdf')):
    #            continue

    #        # crawl recursively
    #        try:
    #            yield Request(url, callback=self.parse,
    #                          meta={IgnoreVisitedItems.FILTER_VISITED: True})
    #        except ValueError:
    #            log.msg("root     : " + response.url,  level=log.DEBUG);
    #            #log.msg("url      : " + url,  level=log.DEBUG);
    #            #fixed_url = response.url.strip('/') + "/" + url.strip('/')
    #            #log.msg("fixed url: " + fixed_url, level=log.DEBUG);

    #            #yield Request(fixed_url, callback=self.parse,
    #            #              meta={IgnoreVisitedItems.FILTER_VISITED: True})
