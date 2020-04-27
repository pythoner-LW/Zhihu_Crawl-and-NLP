import re
from zhihui_redis.database.Mysql_db import mysql
from zhihui_redis.database.Redis_db import DataBase


# 从redis数据去读取数据并存入mysql中
class Save:
    def insert_mysql(self):
        DataBase.__init__(self,'127.0.0.1', 6379)  # 连接redis数据库
        lists = DataBase.read_list(self,'myspider:items')  # redis数据库中把一个item（即一个问题和所有回答的内容）作为一条记录，从redsis数据库中读取所有数据，返回的是一个列表
        db = mysql.connection(self)  # 连接mysql数据库
        for i in range(len(lists)):
            dic = eval(lists[i])
            q_id = dic["q_id"]  # 问题ID(int)
            title = dic["title"]  # 问题
            title = self.data_clean(title)  # 数据清洗
            follow_count = dic["follow_count"]  # 问题的关注数
            broswer_count = dic["broswer_count"]  # 问题的浏览数
            answer_count = dic["answer_count"]  # 问题的总回答数
            describe = dic["describe"]  # 问题的描述
            describe = self.data_clean(describe)  # 数据清洗
            mysql.insert_question(self, db, q_id, follow_count, broswer_count, answer_count, title, describe)

            a_id = dic["a_id"]  # 所有回答ID的列表
            answer_list = dic["answer"]  # 一个问题的所有回答的列表
            voteup_list = dic["voteup"]  # 回答的赞数的列表
            commend_count_list = dic["commend_count"]  # 回答的评论数的列表
            for j in range(len(a_id)):  # 将每个回答及相关内容入库
                answer_list[j] = self.data_clean(answer_list[j])  # 数据清洗
                mysql.insert_answer(self, db,voteup_list[j], commend_count_list[j], answer_list[j],
                                    q_id)  # 插入数据库操作
            print("插入" + str(i) + "个问题成功");
        mysql.closedb(self, db)

    def data_clean(self, s):  # 删除形式为<...>的没用的字符
        p = re.compile(r'[<](.*?)[>]')  # 匹配形式为<...>的没用的字符
        a = re.findall(p, s)
        # 出去回答中没用的字符
        for i in a:
            ss = '<' + i + '>'
            s = s.replace(ss, '')
        # s = s.replace('\n','。')
        s = s.replace('[图片]', '')  # 除去“[图片]”这样的字符
        return s


d = Save()
d.insert_mysql()

# 有些字符不能转化为utf-8，导致不能存入数据库
