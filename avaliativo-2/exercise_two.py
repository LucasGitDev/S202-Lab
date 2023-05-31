from database import Database


class ExerciseTwo:

    def __init__(self, db: Database):
        self.db = db

    def run(self):
        # setup database
        self.seed()
        self.menu()

    def menu(self):
        print("Encontre o usuário mais velho")
        self.who_is_oldest()

        print("#" * 10)

        print("Quantos usuários têm mais de 30 anos?")
        self.how_many_users_are_older_than_30()

        print("#" * 10)

        print("Qual é a média de idade dos usuários?")
        self.average_age()

        print("#" * 10)

        print()

    def who_is_oldest(self):
        query = """
            MATCH (u:Usuario)
            RETURN u
            ORDER BY u.idade DESC
            LIMIT 1
        """

        oldest = self.db.execute_query(query)
        print(oldest[0]['u']['nome'])

    def how_many_users_are_older_than_30(self):
        query = """
            MATCH (u:Usuario)
            WHERE u.idade >= 30
            RETURN count(u)
        """

        older_than_30 = self.db.execute_query(query)
        print(older_than_30[0]['count(u)'])

    def average_age(self):
        query = """
            MATCH (u:Usuario)
            RETURN avg(u.idade)
        """
        average = self.db.execute_query(query)
        print(average[0]['avg(u.idade)'])

    def seed(self):
        self.db.drop_all()

        query = """
            CREATE (a:Usuario {nome: 'Alice', idade: 25})
            CREATE (b:Usuario {nome: 'Bob', idade: 30})
            CREATE (c:Usuario {nome: 'Charlie', idade: 35})
            CREATE (d:Usuario {nome: 'David', idade: 40})
            CREATE (e:Usuario {nome: 'Eve', idade: 45})

            // Criação de postagens
            CREATE (p1:Postagem {titulo: 'Observações do Amanhecer', conteudo: 'Conteúdo da Observações do Amanhecer'})
            CREATE (p2:Postagem {titulo: 'Memórias da Tarde', conteudo: 'Conteúdo da Memórias da Tarde'})
            CREATE (p3:Postagem {titulo: 'Segredos da Noite', conteudo: 'Segredos da Noite'})

            // Definindo relações de amizade
            CREATE (a)-[:AMIGO]->(b)
            CREATE (b)-[:AMIGO]->(c)
            CREATE (c)-[:AMIGO]->(d)
            CREATE (d)-[:AMIGO]->(e)

            // Definindo quem fez as postagens
            CREATE (a)-[:POSTOU]->(p1)
            CREATE (b)-[:POSTOU]->(p2)
            CREATE (c)-[:POSTOU]->(p3)
        """

        self.db.execute_query(query)
