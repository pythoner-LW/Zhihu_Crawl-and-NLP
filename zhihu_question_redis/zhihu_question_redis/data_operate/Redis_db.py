import redis


# redis数据库操作
class DataBase:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    # 读取单个字符串
    def read_string(self, key):
        try:
            r = redis.StrictRedis(host=self.host, port=self.port, decode_responses=True, charset='UTF8')
            result = r.get(key).decode('utf-8')
            return result
        except Exception as exception:
            print(exception)

    # 读取整个列表
    def read_list(self, key):
        try:
            r = redis.StrictRedis(host=self.host, port=self.port, decode_responses=True, charset='UTF8')
            n = r.llen(key)
            result = r.lrange(key, 0, n)

            return result
        except Exception as exception:
            print(exception)
