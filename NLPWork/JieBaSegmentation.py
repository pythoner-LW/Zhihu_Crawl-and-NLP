#结巴分词工具

import jieba.analyse

def cut_word(file_path):
    res = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            content, label = line.split('\t')
            s = ' '.join(jieba.cut(content))
            l = []
            l.append(s)
            l.append(label)
            res.append(l)
        f.close()
    return res

def wirte_file(data,file_path):
    fo = open(file_path, "w", encoding='utf-8')
    for i in data:
        content = i[0]
        label = i[1]
        fo.write(content + '\t' + label)
    fo.close()


if __name__ == "__main__":
    val_res = cut_word('THUCNews/data/dev.txt')
    train_res = cut_word('THUCNews/data/train.txt')
    test_res = cut_word('THUCNews/data/test.txt')

    wirte_file(train_res,'THUCNews/data/train.txt')
    wirte_file(val_res,'THUCNews/data/dev.txt')
    wirte_file(test_res,'THUCNews/data/test.txt')
