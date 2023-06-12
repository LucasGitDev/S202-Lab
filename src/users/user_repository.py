from database.database import Database
from devices.devices import Device
from users.users import User
from typing import List, Optional


class UserRepository:
    def __init__(self, database: Database):
        self.db = database
        self.db.createCollectionIfNotExists("users", User.get_schema())
    
    def create_user(self, user: User) -> None:
        # Salvar o usuário no banco de dados usando a instância de Database
        del user._id
        collection = self.db.get_collection("users")
        collection.insert_one(user.__dict__)

    def get_all_users(self) -> List[User]:
        collection = self.db.get_collection("users")
        users = collection.find()
        return [User(**user) for user in users]

    def get_user_by_email(self, email: str) -> Optional[User]:
        collection = self.db.get_collection("users")
        user = collection.find_one({"email": email})
        if user:
            return User(**user)
        else:
            return None

    def update_user(self, email: str, name: Optional[str] = None) -> None:
        collection = self.db.get_collection("users")
        update_fields = {}
        if name is not None:
            update_fields["name"] = name
        collection.update_one({"email": email}, {"$set": update_fields})

    def delete_user(self, email: str) -> None:
        collection = self.db.get_collection("users")
        collection.delete_one({"email": email})

    def find_all(self) -> List[User]:
        collection = self.db.get_collection("users")
        return [User(**user) for user in collection.find()]

    def find_by_email(self, email: str) -> Optional[User]:
        collection = self.db.get_collection("users")
        user = collection.find_one({"email": email})
        if user:
            return User(**user)
        else:
            return None
    

    def find_by_id(self, id: str) -> Optional[User]:
        collection = self.db.get_collection("users")
        user = collection.find_one({"_id": id})
        if user:
            return User(**user)
        else:
            return None


    def fetch_user_devices(self, email: str) -> List[Device]:
        pipeline = [
            {"$match": {"email": email}},
            {"$lookup": {
                "from": "devices",  # Nome da coleção de dispositivos
                "localField": "_id",
                "foreignField": "user_id",
                "as": "devices"
            }},
            {"$unwind": "$devices"},
            {"$replaceRoot": {"newRoot": "$devices"}}
        ]

        collection = self.db.get_collection("users")
        result = collection.aggregate(pipeline)
        return [Device.deserialize(data) for data in result]
    