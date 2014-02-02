import os
import os.path

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

DEPTH_LIMIT = 2

SPIDER_MIDDLEWARES = {
    'bigcrawler.middlewares.spider.ignore.IgnoreVisitedItems': 100,
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 100, 
    'bigcrawler.middlewares.downloader.dump.HTMLDumper': 200,
}

ITEM_PIPELINES = {
    #'bigcrawler.pipelines.HTMLCleanserPipeline' : 100,
    'bigcrawler.pipelines.NoHTMLPipeline' : 100,
    'bigcrawler.pipelines.WordCounterPipeline' : 200,
    'bigcrawler.pipelines.ItemCleanserPipeline' : 300,
    'scrapy_mongodb.MongoDBPipeline' : 999,
}

REDIRECT_ENABLED = False

MONGODB_URI = 'mongodb://localhost:27017'
#MONGODB_URI = 'mongodb://167.205.65.104:27017'
MONGODB_DATABASE = 'crawl_repository'
MONGODB_COLLECTION = 'articles'

#LOG_LEVEL = 'INFO'
if not os.path.exists('log'):
    os.mkdir('log')    
LOG_FILE = 'log/log_bigcrawler'
