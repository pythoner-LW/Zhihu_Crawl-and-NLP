#运行爬虫
from scrapy import cmdline
cmdline.execute('scrapy crawl myspider'.split())