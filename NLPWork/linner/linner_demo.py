
#关注数与回答数线性关系

import matplotlib.pyplot as plt
from pandas import DataFrame,Series
from sklearn.model_selection  import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing

follow = []
answer = []
broswer = []

with open('followNum.txt', 'r') as f:
    for line in f:
        follow.append(int(line))

with open('answerNum.txt', 'r') as f:
    for line in f:
        answer.append(int(line))

with open('broswerNum.txt', 'r') as f:
    for line in f:
        broswer.append(int(line))

#需对数据进行特征缩放
#
# follow = preprocessing.minmax_scale(follow, feature_range=(0,100))
# answer = preprocessing.minmax_scale(answer, feature_range=(0,50))
# broswer = preprocessing.minmax_scale(broswer, feature_range=(0,1000))


#examDict = {'关注数':follow, '回答数': answer}
#examDict = {'浏览数':broswer, '关注数': follow}
examDict = {'浏览数':broswer, '回答数': answer}

# 转换为DataFrame的数据格式
examDf = DataFrame(examDict)

plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
# # 绘制散点图
plt.scatter(examDf.浏览数, examDf.回答数, color='b', label="Exam Data")

# 添加图的标签（x轴，y轴）
plt.xlabel("浏览数")
plt.ylabel("回答数")
# 显示图像
plt.show()

# 相关性强度来说的化有以下的关系：
# 0~0.3 弱相关
# 0.3~0.6  中等程度相关
# 0.6~1  强相关

rDf = examDf.corr()
print(rDf)

# 将原数据集拆分训练集和测试集

exam_X  =  examDf.loc[:,'浏览数']
exam_Y  =  examDf.loc[:,'回答数']
X_train, X_test, Y_train, Y_test = train_test_split(exam_X, exam_Y, train_size=.8)
# X_train为训练数据标签,X_test为测试数据标签,exam_X为样本特征,exam_y为样本标签，train_size 训练数据占比

print("原始数据特征:", exam_X.shape,
      ",训练数据特征:", X_train.shape,
      ",测试数据特征:", X_test.shape)

print("原始数据标签:", exam_Y.shape,
      ",训练数据标签:", Y_train.shape,
      ",测试数据标签:", Y_test.shape)

# 散点图

plt.scatter(X_train, Y_train, color="blue", label="train data")
plt.scatter(X_test, Y_test, color="red", label="test data")
# 添加图标标签
plt.legend(loc=2)
plt.xlabel("浏览数")
plt.ylabel("回答数")
plt.title("浏览数-回答数")
# 显示图像
plt.savefig("tests.jpg")
plt.show()


model = LinearRegression()

# 对于模型错误我们需要把我们的训练集进行reshape操作来达到函数所需要的要求
# model.fit(X_train,Y_train)

# reshape如果行数=-1的话可以使我们的数组所改的列数自动按照数组的大小形成新的数组
# 因为model需要二维的数组来进行拟合但是这里只有一个特征所以需要reshape来转换为二维数组
X_train = X_train.values.reshape(-1, 1)
X_test = X_test.values.reshape(-1, 1)

model.fit(X_train, Y_train)

a = model.intercept_  # 截距

b = model.coef_  # 回归系数

print("最佳拟合线:截距", a, ",回归系数：", b)

# 训练数据的预测值
y_train_pred = model.predict(X_train)
# 绘制最佳拟合线：标签用的是训练数据的预测值y_train_pred
plt.plot(X_train, y_train_pred, color='black', linewidth=3, label="best line")

# 测试数据散点图
plt.scatter(X_test, Y_test, color='red', label="test data")

# 添加图标标签
plt.legend(loc=2)
plt.xlabel("浏览数")
plt.ylabel("回答数")
plt.title("浏览数-回答数")
# 显示图像
plt.savefig("b-a-lines.jpg")
plt.show()

score = model.score(X_test, Y_test)

print(score)

