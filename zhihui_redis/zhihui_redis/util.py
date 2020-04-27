# -*- coding: utf-8 -*-
import logging
import requests
import json

orderid = '917507886106620'  # 订单号
api_url = "http://dps.kdlapi.com/api/getdps/?orderid=917507886106620&num=20&pt=1&format=json&sep=1"  # 生成代理ip的链接

logger = logging.getLogger(__name__)  # 日志


def fetch_proxy():
    fetch_url = api_url.format(orderid)
    r = requests.get(fetch_url)
    if r.status_code != 200:
        logger.error("fail to fetch proxy")
        return False
    content = json.loads(r.content.decode('utf-8'))
    ips = content['data']['proxy_list']
    return ips


if __name__ == '__main__':
    print("proxy: ", fetch_proxy())
