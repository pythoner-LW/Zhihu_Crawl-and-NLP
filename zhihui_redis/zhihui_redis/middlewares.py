# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from zhihui_redis.settings import USER_AGENTS
import base64
import logging
from zhihui_redis.util import fetch_proxy

# 代理服务器ip和端口 <开放代理或其他代理已添加白名单>
# from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
# 非开放代理且未添加白名单，需用户名密码认证
username = "353630400"
password = "31luwhyz"
proxy = fetch_proxy()  # 获取一次代理
one_proxy = ''  # 单个代理
# THRESHOLD = 2  # 换ip阈值
# fail_time = 0  # 此ip异常次数
logger = logging.getLogger(__name__)  # 日志


class RandomUserAgent(object):
    """Randomly rotate user agents based on a list of predefined ones"""

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(USER_AGENTS))


# 代理中间件
class ProxyMiddleware(object):

    def process_request(self, request, spider):
        global one_proxy
        one_proxy = random.choice(proxy)
        proxy_url = 'http://%s:%s@%s' % (username, password, one_proxy)
        request.meta['proxy'] = proxy_url
        # logger.debug("using proxy: {}".format(request.meta['proxy']))
        # logger.debug("fail_time: {}".format(fail_time))
        logger.debug("ip: {}".format(one_proxy))
        auth = "Basic %s" % (base64.b64encode(('%s:%s' % (username, password)).encode('utf-8'))).decode('utf-8')
        request.headers['Proxy-Authorization'] = auth

    def process_response(self, request, response, spider):
        global proxy, one_proxy
        logger.debug("ip_list: {}".format(proxy))
        if not (200 <= response.status < 303):  # IP失效
            # fail_time += 1
            # if fail_time >= THRESHOLD:
            proxy.remove(one_proxy)
            if not proxy:
                proxy = fetch_proxy()  # 重新生成IP
                logger.debug("new_ip_list: {}".format(proxy))

        return response


class ZhihuiRedisSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ZhihuiRedisDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called

        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
