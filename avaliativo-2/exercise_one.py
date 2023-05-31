from database import Database


class ExerciseOne:

    def __init__(self, db: Database):
        self.db = db

    def run(self):
        # setup database
        self.seed()
        self.menu()

    def menu(self):
        print("Quem é amigo de Bob?")
        self.who_is_bob_friends()

        print("#" * 10)

        print("Quem postou Memórias da Tarde?")
        self.who_posted_post_2()

        print("#" * 10)

        print("Quem tem mais de 35 anos e postou?")
        self.who_is_older_than_35_and_posted()

        print("#" * 10)

    def who_is_bob_friends(self):
        query = """
            MATCH (a:Usuario)<-[:AMIGO]->(b:Usuario)
            WHERE a.nome = 'Bob'
            RETURN b.nome
        """
        friends = self.db.execute_query(query)
        for friend in friends:
            print(friend[0])

    def who_posted_post_2(self):
        query = """
            MATCH (a:Usuario)-[:POSTOU]->(b:Postagem)
            WHERE b.titulo = 'Memórias da Tarde'
            RETURN a.nome
        """
        who = self.db.execute_query(query)
        print(who[0].get('a.nome'))

    # Se o cara tem 35 e não está fazendo aniversário exatamente naquele dia, ele tem mais de 35
    def who_is_older_than_35_and_posted(self):
        query = """
            MATCH (a:Usuario)-[:POSTOU]->(b:Postagem)
            WHERE a.idade >= 35
            RETURN a.nome, b.titulo
        """
        data = self.db.execute_query(query)
        for item in data:
            print(f"{item[0]} postou {item[1]}")

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
