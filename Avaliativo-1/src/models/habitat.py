from models.cuidador import Cuidador


class Habitat:
    def __init__(self, nome: str, tipoAmbiente: str, cuidador: Cuidador, _id: str = None) -> None:
        self.nome = nome
        self.tipoAmbiente = tipoAmbiente
        self.cuidador = cuidador
        self.id = _id

    def serialize(self):
        return {
            "nome": self.nome,
            "tipoAmbiente": self.tipoAmbiente,
            "cuidador": self.cuidador.serialize(),
            "id": self.id
        }

    def deserialize(habitat: dict):
        return Habitat(habitat['nome'], habitat['tipoAmbiente'], Cuidador.deserialize(habitat['cuidador']), habitat['id'] or None)

    def schema():
        return {
            '$jsonSchema': {
                'bsonType': 'object',
                'required': ['nome', 'tipoAmbiente', 'cuidador'],
                'properties': {
                    'nome': {
                        'bsonType': 'string',
                        'description': 'Nome do habitat deve ser uma string',
                    },
                    'tipoAmbiente': {
                        'bsonType': 'string',
                        'description': 'Tipo de ambiente do habitat deve ser uma string',
                    },
                    'cuidador': Cuidador.schema()['$jsonSchema']
                }
            }
        }
