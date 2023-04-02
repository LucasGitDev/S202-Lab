# using pymongo to connect to MongoDB and load the data.json file into the database.
from pymongo import MongoClient

connectionString = "localhost:27017"


class DatabaseService:
    def __init__(self, database,):
        self.connect(database,)

    def connect(self, database):
        try:
            self.clusterConnection = MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            print("Database connected successfully!")
        except Exception as e:
            print(e)

    def getCollection(self, collection):
        return self.db[collection]

    def createCollectionIfNotExists(self, collection_name, validator=None):
        # if collection_name already exists, update the validator and return the collection
        if collection_name in self.db.list_collection_names():
            # update validation schema
            self.db.command(
                "collMod",
                collection_name,
                validator=validator,
                validationAction="error"
            )
            return self.db[collection_name]
        else:
            return self.db.create_collection(collection_name, validator=validator)
