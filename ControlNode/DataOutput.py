#coding:utf-8
import pymongo

class DataOutput(object):
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client['mydb']
        self.collection = self.db['baike_entry']
        self.datas = []


    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)
        if len(self.datas)>10:
            self.output_db()


    def output_db(self):
        for data in self.datas:
            self.collection.insert(data)
            self.datas.remove(data)

    def output_end(self):
        if len(self.datas)>0:
            self.output_db()
        self.client.close()