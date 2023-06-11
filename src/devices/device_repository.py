from database.database import Database
from devices.devices import Device
from typing import List, Optional
import re

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

    def update_device(self, user_id: Optional[str], name: str, status: Optional[bool], temperature: Optional[float]) -> None:
        collection = self.db.get_collection("devices")
        update_fields = {}
        if status is not None:
            update_fields["status"] = status
        if temperature is not None:
            update_fields["temperature"] = temperature
        collection.update_one({"name": name, "user_id": user_id}, {"$set": update_fields})

    def delete_device(self, name: str) -> None:
        collection = self.db.get_collection("devices")
        collection.delete_one({"name": name})

    def find_all(self):
        collection = self.db.get_collection("devices")
        return collection.find()

    def find_by_name(self, name: str):
        collection = self.db.get_collection("devices")
        return collection.find_one({"name": name})
