# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
#数据处理，使用分布式爬虫时不需要此部分
class ZhihuiRedisPipeline(object):
    def __init__(self):
        self.file = open('zhihu1.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        list_a = item['answer']
        self.file.write("\n\n话wl题:" + str(item['title']) + '\n\n')
        for i in range(len(list_a)):
            a = ''.join(list_a[i])
            p = re.compile(r'[<](.*?)[>]')  # 匹配回答中的没用的字符
            s = re.findall(p, a)
            # 出去回答中没用的字符
            for i in s:
                ss = '<' + i + '>'
                a = a.replace(ss, '')
            self.file.write("回wl答:" + a + '\n')
        return item