# -*- coding: utf-8 -*-

# Scrapy settings for ITjuziscrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ITjuziscrapy'

SPIDER_MODULES = ['ITjuziscrapy.spiders']
NEWSPIDER_MODULE = 'ITjuziscrapy.spiders'

#USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'

COOKIE = {'session': 'ba029d56bd925fe0e8ae18bcb22665ad20c9c653', 
          'remember_code': 'T9QfC.PF93', 
          'acw_tc': 'AQAAAE15xks61wsAMSpNO6umiybawOc5', 
          '_ga': 'GA1.2.2098236307.1503732444', 
          'gr_session_id_eee5a46c52000d401f969f4535bdaa78': '3a730932-0c56-41a1-9eb4-0ad95dbef74b', 
          'Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89': '1509592890', 
          'unique_token': '362430', 'pgv_pvi': '9196131328', 
          'Hm_lvt_1c587ad486cdb6b962e94fc2002edf89': '1509524544,1509528120,1509591220,1509592845', 
          'gr_user_id': '55864615-1dfd-4525-b015-9687f38fd9d4', 
          '_hp2_id.2147584538': '%7B%22userId%22%3A%222442972849669102%22%2C%22pageviewId%22%3A%224802821570011137%22%2C%22sessionId%22%3A%220775522017040901%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%223.0%22%7D', 
          '_gat': '1', 'identity': '15659831367%40test.com', 
          '_gid': 'GA1.2.222504129.1509519026'}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ITjuziscrapy (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

#import logging
#LOG_ENABLED = True
#LOG_ENCODING = "utf-8"
#LOG_LEVEL = logging.DEBUG
#LOG_FILE = "itjuzi.log"
#LOG_STDOUT = True
#LOG_FORMAT = "%(asctime)s [%(name)s] %(levelname)s: %(message)s"
#LOG_DATEFORMAT = "%Y-%m-%d %H:%M:%S"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 15
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ITjuziscrapy.middlewares.ItjuziscrapySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    #'ITjuziscrapy.middlewares.MyCustomDownloaderMiddleware': 534,
    'ITjuziscrapy.middlewares.RandomUserAgent': 1
    #'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    #'itjuzi.middlewares.ProxyMiddleware': 100,
}

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

#PROXIES = [
    #{'ip_port': '111.11.228.75:80', 'user_pass': ''},
    #{'ip_port': '120.198.243.22:80', 'user_pass': ''},
    #{'ip_port': '111.8.60.9:8123', 'user_pass': ''},
    #{'ip_port': '101.71.27.120:80', 'user_pass': ''},
    #{'ip_port': '122.96.59.104:80', 'user_pass': ''},
    #{'ip_port': '122.224.249.122:8088', 'user_pass': ''},
#]

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'ITjuziscrapy.pipelines.ItjuziscrapyPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False
#HTTPERROR_ALLOWED_CODES = [403]
# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
