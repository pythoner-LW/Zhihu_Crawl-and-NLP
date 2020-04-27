#通过关键词来爬取

import json
import scrapy
from scrapy_redis.spiders import RedisSpider
from zhihu_question_redis.items import ZhihuQuestionRedisItem
from scrapy import Request, FormRequest
import re

class QuestionSpider(RedisSpider):
    name = "questionSpider_car-search"
    redis_key = 'questionSpider_car-search:start_urls'

    allowed_domains = ['zhihu.com']

    def parse(self,response):
        #根据需求更改
        search_url = 'https://www.zhihu.com/api/v4/search_v3?t=general&q=%E8%BD%A6&correction=1&offset=20&limit=20&lc_idx=27&show_all_topics=0&search_hash_id=42ea3e140c48b9f8a88403eb4a82b021&vertical_info=0%2C1%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C1'
        yield Request(url=search_url, callback=self.parseQuestions,)

    def parseQuestions(self,response):
        q_json = json.loads(str(response.body, 'utf-8'))  # 将网页内容转化为JSON格式
        is_end = q_json["paging"]["is_end"]  # bool值看是不是最后一个问题
        next_url = q_json["paging"]["next"]  # 后续问题的网址

        list = q_json["data"]
        for dic in list:
            if ('question' in dic['object']):
                id1 = dic['object']['question']['id']  # 网址中的id1
                url = 'https://www.zhihu.com/question/' + str(id1)
                yield Request(url=url, callback=self.parsePage)

        if not is_end:
            yield Request(url=next_url, callback=self.parseQuestions)

    def parsePage(self, response):  # 问题的浏览数和关注数不在JSON文件
        topic = "汽车" # 获取问题所属的话题
        items = ZhihuQuestionRedisItem()
        num = response.xpath('//strong[@class="NumberBoard-itemValue"]/@title').extract()  # 获取浏览数和关注数
        s = response.xpath('//span[@class="RichText ztext"]/text()').extract()  # 获取问题描述
        title = response.xpath('//h1[@class="QuestionHeader-title"]/text()').extract()  # 获取问题内容
        answer_count = response.xpath('//div[@class="List-header"]/h4/span/text()').extract()  # 获取问题的回答数(格式为100个回答)
        items['follow_count'] = num[0]  # 问题关注数
        items['broswer_count'] = num[1]  # 问题浏览数
        items['describe'] = "".join(s)  # 问题描述
        items['topic'] = topic
        items['title'] = "".join(title)
        items['answer_count'] = "".join(answer_count)

        return items
