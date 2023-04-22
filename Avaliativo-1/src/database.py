from pymongo import MongoClient

connectionString = "mongodb+srv://user123:senha123@cluster0.mib3au9.mongodb.net/"

class Database:
    def __init__(self, database,):
        self.connect(database,)

    def connect(self, database):
        try:
            self.clusterConnection = MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.dbConnection = self.clusterConnection[database]
            print("Database connected successfully!")
        except Exception as e:
            print(e)

    def disconnect(self):
        self.clusterConnection.close()

    def getCollection(self, collection):
        return self.dbConnection[collection]

    def createCollectionIfNotExists(self, collection_name, validator=None):
        # if collection_name already exists, update the validator and return the collection
        if collection_name in self.dbConnection.list_collection_names():
            # update validation schema
            self.dbConnection.command(
                "collMod",
                collection_name,
                validator=validator,
                validationAction="error"
            )
            return self.dbConnection[collection_name]
        else:
            return self.dbConnection.create_collection(collection_name, validator=validator)
