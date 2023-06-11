from devices.devices import Device

class User:
    def __init__(self, name, email, devices=None,  _id: str = None):
        self._id = _id
        self.name = name
        self.email = email
        self.devices = devices if devices is not None else []

    def add_device(self, device):
        self.devices.append(device)

    def remove_device(self, device):
        self.devices.remove(device)

    def get_devices(self):
        return self.devices

    def serialize(self):
        return {
            "name": self.name,
            "email": self.email,
            "devices": [device.serialize() for device in self.devices]
        }

    @staticmethod
    def deserialize(data):
        devices = [Device.deserialize(device_data) for device_data in data.get("devices", [])]
        return User(data["name"], data["email"], devices)

    @staticmethod
    def get_schema():
        schema = {
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["name", "email"],
                "properties": {
                    "name": {
                        "bsonType": "string",
                        "description": "Nome do usuário"
                    },
                    "email": {
                        "bsonType": "string",
                        "description": "Email do usuário"
                    }
                }
            }
        }

        return schema
