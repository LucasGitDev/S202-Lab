class Device:
    def __init__(self, user_id, name, status, temperature,  _id: str = None):
        self._id = _id
        self.user_id = user_id
        self.name = name
        self.status = status
        self.temperature = temperature

    def serialize(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "status": self.status,
            "temperature": float(self.temperature)
        }

    @staticmethod
    def deserialize(data):
        return Device(data["user_id"], data["name"], data["status"], data["temperature"])

    @staticmethod
    def get_schema():
        schema = {
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["user_id", "name", "status", "temperature"],
                "properties": {
                    "user_id": {
                        "bsonType": "objectId",
                        "description": "ID do usuário ao qual o dispositivo pertence"
                    },
                    "name": {
                        "bsonType": "string",
                        "description": "Nome do dispositivo"
                    },
                    "status": {
                        "bsonType": "bool",
                        "description": "Status do dispositivo"
                    },
                    "temperature": {
                        "bsonType": "double",
                        "description": "Valor de temperatura do dispositivo"
                    }
                }
            }
        }

        return schema
