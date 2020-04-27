#获取关注数前百分之十的问题的关键词

from wordcloud import WordCloud
import jieba
import jieba.analyse as analyse
from os import path
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from zhihui_redis.database.Mysql_db import mysql


class Word:

    # 从数据库读取数据
    def get_date(self):
        db = mysql.connection(self)  # 连接mysql数据库
        date = mysql.select_ten_question(self, db)  # 元组数据类类型
        print(type(date[0]))
        mysql.closedb(self, db)
        fo = open("date.txt", "w", encoding='UTF-8')
        for i in date:
            fo.write(i[0])
        fo.close()

    # 绘制词云
    def draw_wordcloud(self):
        # 读入一个txt文件
        fo = open('date.txt', 'r', encoding='UTF-8')
        comment_text = fo.read()
        fo.close()
        # 结巴分词，生成字符串，如果不通过分词，无法直接生成正确的中文词云
        # cut_text = " ".join(jieba.cut(comment_text))
        tag = analyse.extract_tags(comment_text, topK=100, withWeight=False, allowPOS=())  # 得到100个关键词
        cut_text = " ".join(jieba.cut("".join(tag)))  # 分词
        d = path.dirname(__file__)  # 当前文件文件夹所在目录
        # color_mask = imread("Anne_Hathaway.png") # 读取背景图片
        cloud = WordCloud(
            # 设置字体，不指定就会出现乱码

            font_path="HYQiHei-25J.ttf",
            # font_path=path.join(d,'simsun.ttc'),
            # 设置背景色
            background_color='white',
            # 词云形状
            # mask=color_mask,
            # 允许最大词汇
            max_words=500,
            # 最大号字体
            max_font_size=40
        )
        word_cloud = cloud.generate(cut_text)  # 产生词云
        word_cloud.to_file("pjl_cloud4.jpg")  # 保存图片
        #  显示词云图片
        plt.imshow(word_cloud)
        plt.axis('off')
        plt.show()


work = Word()
work.get_date()
work.draw_wordcloud()
