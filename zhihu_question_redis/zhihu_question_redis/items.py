# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuQuestionRedisItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()  # 问题内容
    follow_count = scrapy.Field()  # 问题关注数
    broswer_count = scrapy.Field()  # 问题浏览数
    describe = scrapy.Field()  # 问题描述
    topic = scrapy.Field()  # 问题所属的话题
    answer_count = scrapy.Field()  # 问题的总回答数

