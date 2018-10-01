import pymongo


class Database:
    def __init__(self, ip="127.0.0.1", port=27017, dbname="groupbot", collectionname="user"):
        self.db = pymongo.MongoClient(ip, port)
        self.db = self.db[dbname]
        self.collection = self.db[collectionname]

