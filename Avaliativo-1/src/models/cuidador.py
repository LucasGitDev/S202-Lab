
class Cuidador:
    def __init__(self, nome: str, documento: str, _id: str = None) -> None:
        self.nome = nome
        self.documento = documento
        self.id = _id

    def serialize(self):
        return {
            "nome": self.nome,
            "documento": self.documento,
            "id": self.id
        }

    def deserialize(cuidador: dict):
        return Cuidador(cuidador['nome'], cuidador['documento'], cuidador['id'] or None)

    def schema():
        return {
            '$jsonSchema': {
                'bsonType': 'object',
                'required': ['nome', 'documento'],
                'properties': {
                    'nome': {
                        'bsonType': 'string',
                        'description': 'Nome do cuidador deve ser uma string'
                    },
                    'documento': {
                        'bsonType': 'string',
                        'description': 'Documento do cuidador deve ser uma string'
                    }
                }
            }
        }
