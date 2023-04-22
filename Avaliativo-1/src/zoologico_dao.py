from database import Database
from models.animal import Animal
from bson.objectid import ObjectId


class ZoologicoDAO:
    def __init__(self, database: Database):
        self.database = database
        self.collection = self.database.createCollectionIfNotExists(
            "animais", Animal.schema())

    def createAnimal(self, animal: Animal):
        return self.collection.insert_one(animal.serialize())

    def readAnimal(self, id: str)-> Animal:
        return self.collection.find_one({"_id": ObjectId(id)})
    
    def readAnimals(self):
        return self.collection.find()

    def updateAnimal(self, id: str, animal: Animal):
        return self.collection.update_one({"_id": ObjectId(id)}, {"$set": animal.serialize()})

    def deleteAnimal(self, id: str):
        return self.collection.delete_one({"_id": ObjectId(id)})
