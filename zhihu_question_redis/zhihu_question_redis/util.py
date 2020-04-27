# -*- coding: utf-8 -*-
#这里购买了快代理的IP

import logging
import requests
import json

orderid = ''  # 订单号
logger = logging.getLogger(__name__)  # 日志
api_url_one = "http://dps.kdlapi.com/api/getdps/?orderid=958571997467779&num=1&pt=1&format=json&sep=1"  # 生成单个代理ip的链接
api_url = "http://dps.kdlapi.com/api/getdps/?orderid=958571997467779&num=10&pt=1&format=json&sep=1"  # 生成多个代理ip的链接
headers = {
    'Connection': 'close',
}

def fetch_proxy():
    fetch_url = api_url.format(orderid)
    r = requests.get(fetch_url)
    if r.status_code != 200:
        logger.error("fail to fetch proxy")
        return False
    content = json.loads(r.content.decode('utf-8'))
    ips = content['data']['proxy_list']
    return ips


def fetch_one_proxy():
    s = requests.session()
    s.keep_alive = False  # 关闭多余连接
    fetch_url = api_url_one.format(orderid)
    r = s.get(url=fetch_url)
    if r.status_code != 200:
        logger.error("fail to fetch proxy")
        return False
    content = json.loads(r.content.decode('utf-8'))
    ips = content['data']['proxy_list']

    ips = ''.join(ips)
    check_url = 'https://dps.kdlapi.com/api/checkdpsvalid?orderid=958571997467779&signature=kienaibtazzhopwefohpuwmkq5o4r3zz&proxy=' + ips
    re = requests.get(check_url)
    check_content = json.loads(str(re.content,'utf-8'))
    vailed = check_content['data'][ips]
    if not vailed:
        print("ip无效，正在重新获取.....")
        fetch_one_proxy()
    return ips



def check_ip(ip):
    url = 'https://dps.kdlapi.com/api/checkdpsvalid?orderid=958571997467779&signature=kienaibtazzhopwefohpuwmkq5o4r3zz&proxy=' + ip
    r = requests.get(url)
    print(r.content)
    content = json.loads(str(r.content,'utf-8'))
    vailed = content['data'][ip]
    return vailed
