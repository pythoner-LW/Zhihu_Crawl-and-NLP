
# p=re.compile(r'[^\x80-\x8f]');
import json
import re

#strs = "如何评价印度人反驳Facebook投资人å\x8f";
# print (strs);
#

# fo = open("foo.txt", "w",encoding='UTF-8')
# fo.write("沙发上")
# fo.write("zxc")
from tqdm import tqdm
import random

class test:
    def remove_punctuation(self):
        # line  ="怎,样，评：价:刘昊然16.0的资源“”为什《么》昊然弟..弟的[路人]?好æ"
        # rule = re.compile(r"[^a-zA-Z0-9\u4e00-\u9fa5.%+-《》“”：]")
        # line = rule.sub('',line)
        # print(line)
        # s = "yuyu y2"
        # s = s.split('\t')[0]
        # print(s)

        # s = "<div class=\"item\"><div class=\"blk\">\n<a target=\"_blank\" href=\"/topic/19550517\">\n<img src=\"https://pic2.zhimg.com/f07808da5625fef3607f8b75b770349f_l.jpg\" alt=\"互联网\">\n<strong>互联网</strong>\n</a>\n<p>互联网（英语：Internet），又称网际网络，或音译因特网(…</p>\n\n<a id=\"t::-99\" href=\"javascript:;\" class=\"follow meta-item zg-follow\"><i class=\"z-icon-follow\"></i>关注</a>\n\n</div></div>"
        # child_id = re.search(r'\/topic\/(\d+)', s).group()
        # id = re.search(r'(\d+)', child_id).group()
        # print(id)


        # i= 0
        # with open('train.txt', 'r', encoding='UTF-8') as f:
        #     for line in tqdm(f):
        #         i += 1
        #         lin = line.strip()
        #         if not lin:
        #             continue
        #         content, label = lin.split('\t')
        #         print(str(i) + '\t' + label)


        #l = []
        # x  =[('sd',1),('bdfds',1),('c',3),('d',5)]
        # x1  =[('a',1),('b',1),('c',3),('d',5)]
        # x2  =[('a',1),('b',1),('c',3),('d',5)]
        # random.shuffle(x2)
        # l.append(x)
        # l.append(x1)
        # l.append(x2)
        # random.shuffle(l)
        # print(l)
        # x = [1,2,3,4,5,6,7,8,9]
        # print(x[:3])
        # print(x[3:4])
        one = []
        two= []
        three = []
        four = []
        five = []
        six = []
        #serven = []
        #eigth = []
        #nine = []
        #ten  =[]
        with open('test.txt', 'r', encoding='UTF-8') as f:
            for line in tqdm(f):
                lin = line.strip()
                content, label = lin.split('\t')
                if label == '0':
                    one.append(line)
                elif label == '1':
                    two.append(line)
                elif label == '2':
                    three.append(line)
                elif label == '3':
                    four.append(line)
                elif label == '4':
                    five.append(line)
                elif label == '5':
                    six.append(line)
                # elif label == '6':
                #     serven.append(line)
                # elif label == '7':
                #     eigth.append(line)
                # elif label == '8':
                #     nine.append(line)
                # elif label == '9':
                #     ten.append(line)
            f.close()

            fo_train = open("test.txt", "w", encoding='utf-8')
            for i in one:
                fo_train.write(i)
            for i in two:
                fo_train.write(i)
            for i in three:
                fo_train.write(i)
            for i in four:
                fo_train.write(i)
            for i in five:
                fo_train.write(i)
            for i in six:
                fo_train.write(i)
            # for i in serven:
            #     fo_train.write(i)
            # for i in eigth:
            #     fo_train.write(i)
            # for i in nine:
            #     fo_train.write(i)
            # for i in ten:
            #     fo_train.write(i)
            fo_train.close()

        # i  = 0
        # with open('train.txt', 'r', encoding='UTF-8') as f:
        #     for line in tqdm(f):
        #         lin = line.strip()
        #         content,lable = lin.split('\t')
        #         if len(content) > 50 and lable is '9':
        #             i += 1
        # print(i)


d = test()
d.remove_punctuation()
