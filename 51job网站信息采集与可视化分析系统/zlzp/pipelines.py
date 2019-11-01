import pymongo
from scrapy.conf import settings
import json
import codecs

class ZlzpPipeline(object):
    def __init__(self):
        self.filename = codecs.open("zlzp.csv","wb")
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = settings["MONGODB_SHEETNAME"]
        # 创建MONGODB数据库链接
        client = pymongo.MongoClient(host=host, port=port)
        # 指定数据库
        mydb = client[dbname]
        # 存放数据的数据库表名
        self.post = mydb[sheetname]

    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.filename.write(content.encode("utf-8"))
        return item


    def  close_spider(self):
        self.filename.close()

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item