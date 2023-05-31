from database import Database


class TeacherCRUD:

    def __init__(self, db: Database):
        self.db = db

    def create(self, name, ano_nasc, cpf):
        query = """
                CREATE (t:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})
                RETURN t
            """

        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)

    def read(self, name):  # retorna apenas um Teacher
        query = """
                MATCH (t:Teacher)
                WHERE t.name = $name
                RETURN t
            """

        parameters = {"name": name}

        return self.db.execute_query(query, parameters)

    def delete(self, name):  # deleta Teacher com base no name
        query = """
                MATCH (t:Teacher)
                WHERE t.name = $name
                DELETE t
            """

        parameters = {"name": name}

        self.db.execute_query(query, parameters)

    def update(self, name, newCpf):  # atualiza cpf com base no name
        query = """
                MATCH (t:Teacher)
                WHERE t.name = $name
                SET t.cpf = $newCpf
            """

        parameters = {"name": name, "newCpf": newCpf}

        self.db.execute_query(query, parameters)
