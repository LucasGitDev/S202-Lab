from typing import Collection
import pymongo
import json
from os import path

dataJson = path.join(path.dirname(__file__), 'data.json')

with open(dataJson, encoding='utf8') as f:
    dataset = json.load(f)
    print("Dataset loaded successfully!")
    print(f"Dataset length: {len(dataset)}")


class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "localhost:27017"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Database connected successfully!")
        except Exception as e:
            print(e)

    def resetDatabase(self):
        try:
            self.db.drop_collection(self.collection)
            self.collection.insert_many(dataset)
            print("Database reseted successfully!")
        except Exception as e:
            print(e)