
#从mysql数据库中读取问题文本并存入TXT文件

from zhihu_question_redis.data_operate.Mysql_db import mysql
import random
class DatabaseToFile:
    def __init__(self):
        self.db = mysql.connection(self)  # 连接mysql数据库

    def saveToFile(self):
        #问题的分类
        #classification = {'生活方式': 0, '金融': 1, '运动': 2, '科技': 3, '艺术': 4, '文化': 5, '自然科学': 6, '汽车':7, '游戏':8, '法律':9}
        classification = {'运动': 0, '文化': 1, '自然科学': 2, '汽车':3, '游戏':4, '法律':5}
        #训练集，测试集，验证集分别写入三个文件
        fo_train = open("train.txt", "w", encoding='utf-8')
        fo_dev = open("dev.txt", "w", encoding='utf-8')
        fo_test = open("test.txt", "w", encoding='utf-8')
        lists = []
        culture = list(mysql.select_que_type(self,self.db,'文化')) #元组数据类型
        lists.append(culture)

        #lifestyle = list(mysql.select_que_type(self,self.db,'生活方式'))
        #lists.append(lifestyle)

        #finance = list(mysql.select_que_type(self,self.db,'金融'))
        #lists.append(finance)

        #technology = list(mysql.select_que_type(self,self.db,'科技'))
        #lists.append(technology)

        #art = list(mysql.select_que_type(self,self.db,'艺术'))
        #lists.append(art)

        nature = list(mysql.select_que_type(self,self.db,'自然科学'))
        lists.append(nature)

        sport = list(mysql.select_que_type(self,self.db,'运动'))
        lists.append(sport)

        car = list(mysql.select_que_type(self,self.db,'汽车'))
        lists.append(car)

        game = list(mysql.select_que_type(self,self.db,'游戏'))
        lists.append(game)

        law = list(mysql.select_que_type(self,self.db,'法律'))
        lists.append(law)

        list_train = []
        list_val = []
        list_test = []

        for i in lists:#每个类别中一共2万条数据训练集，测试集，验证集分别取18000，1000，1000条
            list_val += i[:1000]
            list_test += i[1000:2000]
            list_train += i[2000:20000]
        #打乱顺序，便于训练
        random.shuffle(list_train)
        random.shuffle(list_test)
        random.shuffle(list_val)
        #写入文件
        self.writeToFile(list_train,fo_train,classification)
        self.writeToFile(list_val,fo_dev,classification)
        self.writeToFile(list_test,fo_test,classification)

        #关闭文件
        fo_train.close()
        fo_test.close()
        fo_dev.close()
        mysql.closedb(self, self.db)

    #生成训练集文本
    def writeToFile(self,data,fo,classification):
        for i in data:
            content = i[0]
            type = classification.get(i[1])
            fo.write(content+ '\t' + str(type) + '\n')
        #fo.close()


    #得到关注数大于2000的问题
    def fun(self):
        data = mysql.select_question_more(self,self.db)
        fo = open("data.txt", "a+", encoding='utf-8')
        for i in range(len(data)):
            fo.write(data[i][0] + '\n')
        mysql.closedb(self,self.db)

    #得到问题的关注数
    def get_follow_num(self):
        data = mysql.select_follow_num(self,self.db)
        fo = open("followNum.txt", "a+", encoding='utf-8')
        for i in range(len(data)):
            fo.write(str(data[i][0]) + '\n')
        mysql.closedb(self, self.db)

    #得到问题的回答数
    def get_answer_num(self):
        data = mysql.select_answer_num(self,self.db)
        fo = open("answerNum.txt", "a+", encoding='utf-8')
        for i in range(len(data)):
            fo.write(str(data[i][0]) + '\n')
        mysql.closedb(self, self.db)

    # 得到问题的回答数
    def get_broswer_num(self):
        data = mysql.select_broswer_num(self, self.db)
        fo = open("broswerNum.txt", "a+", encoding='utf-8')
        for i in range(len(data)):
            fo.write(str(data[i][0]) + '\n')
        mysql.closedb(self, self.db)

    def dea(self,l1,l2):
        for i in range(len(l2)):
            l1.extend(l2[i])
        return l1



dbf = DatabaseToFile()
dbf.saveToFile()
