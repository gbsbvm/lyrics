# -*- coding: utf-8 -*-



# Scrapy settings for airbnb project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#import time
BOT_NAME = 'lyriker'

SPIDER_MODULES = ['lyriker.spiders']
NEWSPIDER_MODULE = 'lyriker.spiders'
MONGODB = [
    'mongodb://complus:DUotto618@adriana:27018',
    'mongodb://complus:DUotto618@annika:27018',
    'mongodb://complus:DUotto618@jasmina:27018',
    'mongodb://complus:DUotto618@laura:27018',
    'mongodb://complus:DUotto618@sarah:27018',
    'mongodb://complus:DUotto618@silke:27018', ]
#MONGODB_CLIENT = pymongo.MongoClient(MONGODB)
# DB=MONGODB_CLIENT.airbnb
# RENTALS_COLLECTION=DB.rentals
# CONTROL_COLLECTION=DB.control

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'airbnb (+http://www.yourdomain.com)'
#USER_AGENT= 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7'

# USER_AGENT_LIST = [
#   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
#  'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0',
# 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10',
#]
USER_AGENT_LIST_FILE = 'user_agents.txt'
# with open('user_agents.txt', 'r') as user_agents_list:
# USER_AGENT_LIST = [line.strip() for line in user_agents_list if
# line.strip() if not line.startswith('#')]

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
DOWNLOAD_TIMEOUT = 200

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_DEBUG = False
RANDOMIZE_DOWNLOAD_DELAY = True


# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED=False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'airbnb.middlewares.SpiderMiddleware': 543,
# }
# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'airbnb.middlewares.MyCustomDownloaderMiddleware': 543,
# }
# DOWNLOADER_CLIENTCONTEXTFACTORY = 'airbnb.middlewares.CustomContextFactory'

DOWNLOADER_MIDDLEWARES = {
    'airbnb.middlewares.RandomUserAgentMiddleware': 400,
    #  'airbnb.middlewares.ProxyMiddleware': 410,
    'airbnb.middlewares.LimitHandlerMiddleware': 650,

}
# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'airbnb.pipelines.SomePipeline': 300,
#}
ITEM_PIPELINES = {
    'airbnb.pipelines.MongoDBPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED = False

# The initial download delay
# AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED=True
# HTTPCACHE_EXPIRATION_SECS=0
# HTTPCACHE_DIR='httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES=[]
# HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
# LOG_FILE = str(time.strftime("%Y%m%d_"))+'intruder.log'
# 403 and 408 were not default here
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 403, 408]
CLOSESPIDER_ERRORCOUNT = 1
RETRY_TIMES = 10
