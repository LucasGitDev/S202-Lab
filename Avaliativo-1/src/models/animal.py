from models.habitat import Habitat


class Animal:
    def __init__(self, nome: str, especie: str, idade: int, habitat: Habitat, _id: str = None):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.habitat = habitat
        self.id = _id

    def serialize(self):
        return {
            "nome": self.nome,
            "especie": self.especie,
            "idade": self.idade,
            "habitat": self.habitat.serialize()
        }

    def deserialize(animal: dict):
        return Animal(animal['nome'], animal['especie'], int(animal['idade']), Habitat.deserialize(animal['habitat']), animal['_id'])

    def schema():
        return {
            '$jsonSchema': {
                'bsonType': 'object',
                'required': ['nome', 'especie', 'idade', 'habitat'],
                'properties': {
                    'nome': {
                        'bsonType': 'string',
                        'description': 'Nome do animal deve ser uma string',
                    },
                    'especie': {
                        'bsonType': 'string',
                        'description': 'Especie do animal deve ser uma string',
                    },
                    'idade': {
                        'bsonType': 'int',
                        'description': 'Idade do animal deve ser um inteiro',
                        'minimum': 0
                    },
                    'habitat': Habitat.schema()['$jsonSchema']
                }
            }
        }
