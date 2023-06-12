from database.database import Database
from devices.devices import Device
from typing import List, Optional
import re

import bson


class DeviceRepository:
    def __init__(self, database: Database):
        self.db = database
        self.db.createCollectionIfNotExists("devices", Device.get_schema())

    def create_device(self, device: Device) -> None:
        del device._id
        collection = self.db.get_collection("devices")
        collection.insert_one(device.__dict__)

    def get_all_devices(self) -> List[Device]:
        collection = self.db.get_collection("devices")
        devices = collection.find()
        return [Device(**device) for device in devices]

    def get_device_by_name(self, name: str) -> Optional[List[Device]]:
        collection = self.db.get_collection("devices")
        regex = re.compile(f".*{name}.*", re.IGNORECASE)
        devices = collection.find({"name": regex})
        if devices:
            return [Device(**device) for device in devices]
        else:
            return None

    def update_device(self, device_id: Optional[str], device: Device) -> None:
        collection = self.db.get_collection("devices")
        del device._id
        collection.update_one({"_id": bson.ObjectId(device_id)}, {
                              "$set": device.__dict__})

    def delete_device(self, id: str) -> None:
        collection = self.db.get_collection("devices")
        collection.delete_one({"_id": bson.ObjectId(id)})
        

    def find_all(self):
        collection = self.db.get_collection("devices")
        return collection.find()

    def find_by_name(self, name: str):
        collection = self.db.get_collection("devices")
        return collection.find_one({"name": name})
