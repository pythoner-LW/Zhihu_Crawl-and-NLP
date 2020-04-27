#将字符串形式的cookies转化为字典形式
class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1].replace('"','')
            itemDict[key] = value
        return itemDict
