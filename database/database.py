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
        admingroup = int(admingroup)
        maingroup = int(maingroup)

        print("creating document")
        # TODO sanitize here
        # admingroup as NumberLong
        if self.collection.count_documents({"maingroup": maingroup, "admingroup": admingroup}, limit=1):
            # TODO different checks -> if maingroup already linked with a group
            print("The document exists")
            return False
        else:
            ins = {"admingroup": admingroup, "maingroup": maingroup, "rules": ""}
            x = self.collection.insert_one(ins)
            return True

    def cancel(self, id):
        print("Test")

    def showRulesAdmin(self, id):
        id = id
        return self.collection.find_one({"admingroup": id})["rules"]

    def showRulesMain(self, id):
       # id = int(id)
        return self.collection.find_one({"maingroup": id})["rules"]

    def createRules(self, admingroup, rules):
        print(admingroup)
        print(rules)
        self.collection.update({'admingroup': admingroup}, {"$set":{"rules": rules}}, upsert=True)

    def checkIfAdmin(self, group):
        if self.collection.count_documents({"admingroup": group },limit=1):
            return True
        else:
            return False

    def checkIfMain(self, group):
        if self.collection.count_documents({"maingroup": group}, limit=1):
            return True
        else:
            return False

