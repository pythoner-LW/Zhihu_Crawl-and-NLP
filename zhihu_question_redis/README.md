# zhihu_question_redis

## 介绍
>基于scrapy框架和redis实现了一个爬取知乎上问题的分布式爬虫<br>
>以知乎网站的话题广场为入口，以话题为单位爬取知乎上的问题(包括问题内容、关注数、浏览数、回答数等信息)，以及问题下面的回答(包括回答内容、回答点赞数、回答评论数等信息)
### 环境
>python 3.7<br>
>redis  3.2<br>
>mysql 8.0<br>
>scrapy 2.0<br>

### 使用说明
>服务端：<br>
>1、启动数据库，管理员模式运行cmd，切换到redis的根目录，输入redis-server redis.windows.conf<br>
>2、操作数据库，打开另一个cmd窗口，输入redis-cli<br>
>3、启动爬虫：redis_cli模式下输入lpush myspider:start_urls https://www.zhihu.com/topics<br>
>客户端：<br>
>1、连接服务器数据库，管理员模式运行cmd，输入redis-cli -h 主机ip地址<br>
>2、启动爬虫：pycahrm中命令行输入scrapy runspider myspider.py  <br>
>注：需要配置redis的环境变量<br><br>

>关于代理IP 项目中使用了[快代理](https://www.kuaidaili.com) 请自行购买

