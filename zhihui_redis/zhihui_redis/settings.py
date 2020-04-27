# -*- coding: utf-8 -*-

# Scrapy settings for zhihui_redis project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihui_redis'

SPIDER_MODULES = ['zhihui_redis.spiders']
NEWSPIDER_MODULE = 'zhihui_redis.spiders'

USER_AGENTS = [
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6"
    ]





# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihui_redis (+http://www.yourdomain.com)'

# Obey robots.txt rules
#ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
    'Cookie':'_zap=9802933d-4c8c-4052-a7aa-0acbd9fd3181; d_c0="ALCsu7pEeQ-PTnqII30FzN6bpOa2pK09Xx8=|1558616227"; _xsrf=anaUqgXhz0GbjNTjnykooNIwJJuQz0CY; __gads=ID=b1d8da2151976746:T=1561039288:S=ALNI_MZMnN_LyTP8W_yBV6WF-EZ4Jqyk7Q; __utmv=51854390.100--|2=registration_date=20180328=1^3=entry_date=20180328=1; z_c0="2|1:0|10:1570613781|4:z_c0|92:Mi4xb3JwdUNBQUFBQUFBc0t5N3VrUjVEeVlBQUFCZ0FsVk5GZmlLWGdCbGxmelBqcHlrR1E4ZGZVME81Vmc2N3JEQ0t3|753ef713d76b03ae14941006404f5bf8040fb1474170a2cb9a03b48e587ef565"; q_c1=d63660902ec44c388c55200fa1f457c6|1573114107000|1558616230000; __utmz=51854390.1573925543.34.22.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; tst=h; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1574770930,1574845618,1574846109,1574846251; tgw_l7_route=d9073c2db8fd446afafd830a80e5db8c; __utma=51854390.1559590702.1569030516.1573925543.1574867956.35; __utmb=51854390.0.10.1574867956; __utmc=51854390; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1574868662; tshl=fashion'

}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#     'zhihui_redis.middlewares.ZhihuiRedisSpiderMiddleware': 543,
#     'scrapy.spidermiddlewares.depth.DepthMiddleware' : -10
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    #'zhihui_redis.middlewares.ZhihuiRedisDownloaderMiddleware': 543,
    'zhihui_redis.middlewares.RandomUserAgent': 1,
    'zhihui_redis.middlewares.ProxyMiddleware': 100,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    #'zhihui_redis.pipelines.ZhihuiRedisPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 300
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#redis配置

SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 指定使用scrapy-redis的去重
DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'

# 指定排序爬取地址时使用的队列，
# 默认的 按优先级排序(Scrapy默认)，由sorted set实现的一种非FIFO、LIFO方式。
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'


# 可选的 按先进先出排序（FIFO）
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'
# 可选的 按后进先出排序（LIFO）
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderStack'

# 在redis中保持scrapy-redis用到的各个队列，从而允许暂停和暂停后恢复，也就是不清理redis queues
SCHEDULER_PERSIST = True

# 只在使用SpiderQueue或者SpiderStack是有效的参数，指定爬虫关闭的最大间隔时间
# SCHEDULER_IDLE_BEFORE_CLOSE = 10

# 指定redis数据库的连接参数
# REDIS_PASS是我自己加上的redis连接密码（默认不做）
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
#REDIS_PASS = 'redisP@ssw0rd'

#默认情况下,RFPDupeFilter只记录第一个重复请求。将DUPEFILTER_DEBUG设置为True会记录所有重复的请求。
DUPEFILTER_DEBUG =True


