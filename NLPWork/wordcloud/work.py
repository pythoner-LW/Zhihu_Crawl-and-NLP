import jieba.posseg as psg
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS


# 根据词频降序排序
def wordsort(word_list):
    word_frequency = {}
    for word in word_list:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    word_sort = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
    return word_sort


# 生成词云
def word_cloud(word_list):
    words_space_split = " ".join(word_list)

    # 设置停用词
    sw = set(STOPWORDS)
    sw.add("的")  # 停用词可以在后面设置为None
    sw.add("事情")
    sw.add("时候")
    sw.add("地方")

    # 图片模板和字体
    image = np.array(Image.open('python.jpg'))
    font = 'HYQiHei-25J.ttf'  # 字体路径设置

    # 设置词云样式
    my_wordcloud = WordCloud(scale=4, font_path=font, mask=image, stopwords=sw, background_color='white',
                             max_words=50, max_font_size=80, random_state=20).generate(words_space_split)

    # 保存生成的图片
    my_wordcloud.to_file('wordCloud.jpg')


if __name__ == "__main__":

    # 1. 打开项目文件
    with open('data.txt', 'r', encoding='utf-8') as f:
        content = (f.read())
        f.close()

    # 2. 分离名词，放在 list_words 里
    list_words = []
    for x in psg.cut(content):
        # 保留名词长度至少两个字
        if x.flag in ['n', 'nr', 'ns'] and len(x.word) > 1:
            list_words.append(x.word)

    # 3. 按照词频由大到小排序，放在 list_words_sorted 里
    list_words_sorted = wordsort(list_words)

    # 4. 词云生成
    word_cloud([x[0] for x in list_words_sorted])

    # # 5. 打印TOP10
    # print('\n序号\t名词\t词频\t柱图\n')
    # rate = 10  # 倍率，每出现rate个绘制1个单元
    # for i in range(10):
    #     print('{}\t{}\t{}\t{}\n'.format(i + 1, list_words_sorted[i][0], list_words_sorted[i][1],
    #                                     '▂' * (list_words_sorted[i][1] // rate)))