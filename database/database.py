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

    def connectGroups(self, maingroup, admingroup):
        print("creating document")
        # TODO sanitize here
        if self.collection.count_documents({"maingroup": maingroup, "admingroup": str(admingroup)}, limit=1):
            # TODO different checks -> if maingroup already linked with a group
            print("The document exists")
            return False
        else:
            ins = {"admingroup": str(admingroup), "maingroup": maingroup}
            x = self.collection.insert_one(ins)
            return True

    def cancel(self, id):
        print("Test")
