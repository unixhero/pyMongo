from pymongo import MongoClient


class Connection:
    client = None

    def __init__(self, server='localhost', port=27017, dbname='Putin'):
        self.dbServer = server
        self.dbPort = port
        self.client = MongoClient(self.dbServer, self.dbPort)
        self.currentDB = self.client[dbname]

    # Laden aller Dokumente in der angegebenen Collection
    # Durchlaufen/Ausgeben aller Dokumente
    # Optional kann als JSON ein Filter angegeben werden
    def getdocuments(self, collection):
        for documents in self.currentDB[collection].find():
            print(documents)

    def insertdocument(self, collection, data={}):
        print('Die neue ID lautet: ' + str(self.currentDB[collection].insert_one(data).inserted_id))

    def deltedocument(self, collection, kriterium={}):
        result = self.currentDB[collection].delete_one(kriterium)
        print(result.deleted_count)

    def updatedocument(self, collection, search={}, update={}):
        resultupdate = self.currentDB[collection].update_one(search, update)
        print(resultupdate.modified_count)
