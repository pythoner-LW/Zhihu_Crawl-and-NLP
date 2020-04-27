# 从redis数据去读取数据并存入mysql中

import re
from zhihu_question_redis.data_operate.Mysql_db import mysql
from zhihu_question_redis.data_operate.Redis_db import DataBase

null = ''
class Save:
    def __init__(self):
        DataBase.__init__(self, '127.0.0.1', 6379)  # 连接redis数据库
        self.lists = DataBase.read_list(self,'questionSpider:items')  # redis数据库中把一个item（即一个问题和所有回答的内容）作为一条记录，从redsis数据库中读取所有数据，返回的是一个列表
        self.db = mysql.connection(self)  # 连接mysql数据库

    def insert_mysql(self):

        for i in range(len(self.lists)): #law 5547 top 3091 un 9693
            global null
            null = ''
            dic = eval(self.lists[i]) #转化位字典格式
            title = dic["title"]  # 问题
            title = self.data_clean(title)  # 数据清洗
            title = self.deal_illeagel_title(title)
            follow_count = dic["follow_count"]  # 问题的关注数
            broswer_count = dic["broswer_count"]  # 问题的浏览数
            answer_count = 0
            if dic["answer_count"]:
                answer_count = self.deal_answer_count(dic["answer_count"])  # 问题的总回答数
            describe = dic["describe"]  # 问题的描述
            describe = self.data_clean(describe)  # 数据清洗
            topic = "" #问题所属的话题
            flag = mysql.insert_question(self, self.db, follow_count, broswer_count, answer_count, title, describe,topic)
            if flag:
                print("插入第" + str(i+1) + "个问题成功");
            else:
                print("插入第" + str(i + 1) + "个问题失败");
        mysql.closedb(self, self.db)

    def data_clean(self, s):  # 删除形式为<...>的没用的字符
        p = re.compile(r'[<](.*?)[>]')  # 匹配形式为<...>的没用的字符
        a = re.findall(p, s)
        # 出去回答中没用的字符
        for i in a:
            ss = '<' + i + '>'
            s = s.replace(ss, '')
        s = s.replace('[图片]', '')  # 除去“[图片]”这样的字符

        return s

    def deal_answer_count(self,s):# 处理格式为1,234的回答数，提取数字
        temp = s.split(" ")[0] #1,234
        num = temp.split(",") #1234列表
        res = "".join(num)
        return int(res)

    def deal_illeagel_title(self,s):#处理问题中的非法字符
        rule = re.compile(r"[^a-zA-Z0-9\u4e00-\u9fa5.%+-《》《》“”：]")
        line = rule.sub('', s)
        return line



save = Save()
save.insert_mysql()
#save.get_questionAndTopic()

#tips
# 有些字符不能转化为utf-8，导致不能存入数据库
# 13行 转化为字典格式时 可能会出现键对应的值位空的情况 采用自定义null的方法
#问题的总回答数的格式为1,122 个回答
