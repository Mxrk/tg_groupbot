import pymongo
from threading import Lock


class Database(object):
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        with Database._lock:
            if Database._instance is None:
                Database._instance = super(Database, cls).__new__(cls)

        return Database._instance

    def __init__(self, ip="127.0.0.1", port=27017, dbname="groupbot", collectionname="groups"):
        self.db = pymongo.MongoClient(ip, port)
        self.db = self.db[dbname]
        self.collection = self.db[collectionname]

