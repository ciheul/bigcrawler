# Scrapy settings for bigcrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'bigcrawler'

SPIDER_MODULES = ['bigcrawler.spiders']
NEWSPIDER_MODULE = 'bigcrawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the
# user-agent
#USER_AGENT = 'bigcrawler (+http://www.yourdomain.com)'

DEPTH_LIMIT = 5

SPIDER_MIDDLEWARES = {
    'bigcrawler.middlewares.ignore.IgnoreVisitedItems': 501,
}
