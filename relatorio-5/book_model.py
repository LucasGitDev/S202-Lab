

class Book:

    def __init__(self, title, author, year, price, id=None):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.price = price

    def serialize(self):
        return {
            'titulo': self.title,
            'autor': self.author,
            'ano': self.year,
            'preco': self.price
        }

    def deserialize(data):
        return Book(data['titulo'], data['autor'], data['ano'], data['preco'], data['_id'])

    def getSchema():
        schema = {
            '$jsonSchema': {
                'bsonType': 'object',
                'description': 'Livro',
                'required': ['titulo', 'autor', 'ano', 'preco'],
                'properties': {
                    'titulo': {
                        'bsonType': 'string',
                        'description': 'Titulo do livro'
                    },
                    'autor': {
                        'bsonType': 'string',
                        'description': 'Autor do livro',
                    },
                    'ano': {
                        'bsonType': 'int',
                        'description': 'Ano de publicacao do livro',
                        # sabe-se lá quando se escreveu o primeiro livro a.C.
                        'minimum': -10000,
                        'maximum': 2023,
                    },
                    'preco': {
                        'bsonType': 'double',
                        'description': 'Preco do livro',
                        'minimum': 0,
                    }
                }
            }
        }

        return schema
