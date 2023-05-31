from database import Database
from teacher_crud import TeacherCRUD


class ExerciseThree:

    def __init__(self, db: Database):
        self.db = db
        self.teacher_crud = TeacherCRUD(db)

    def run(self):
        # setup database
        self.db.drop_all()

        while True:
            self.menu_options()
            op = self.validate_option()

            if op == 1:
                self.register_teacher()
            elif op == 2:
                self.update_teacher()
            elif op == 3:
                self.delete_teacher()
            elif op == 4:
                self.read_teacher()
            elif op == 5:
                break
            elif op == 6:
                self.preset()

    def menu_options(self):
        print("1. Cadastrar professor")
        print("2. Atualizar professor")
        print("3. Deletar professor")
        print("4. Buscar professor")
        print("5. Sair")
        print("6. Preset")
        print()

    def validate_option(self):
        op = int(input("Digite a opção: "))
        while op < 1 or op > 6:
            print("Opção inválida")
            op = int(input("Digite a opção: "))
        return op

    def register_teacher(self):
        name = input("Digite o nome do professor: ")
        year = int(input("Digite o ano de nascimento do professor: "))
        cpf = input("Digite o CPF do professor: ")
        self.teacher_crud.create(name, year, cpf)

    def update_teacher(self):
        name = input("Digite o nome do professor que será atualizado: ")
        cpf = input("Digite o CPF do professor que para ser atualizado: ")

        self.teacher_crud.update(name, cpf)

    def delete_teacher(self):
        name = input("Digite o nome do professor que será deletado: ")

        self.teacher_crud.delete(name)

    def read_teacher(self):
        name = input("Digite o nome do professor que será buscado: ")

        teacher = self.teacher_crud.read(name)

        print(teacher[0].data()['t']['name'])
        print(teacher[0].data()['t']['ano_nasc'])
        print(teacher[0].data()['t']['cpf'])

    def preset(self):
        # criar um professor
        print("Criando um professor...")
        self.teacher_crud.create("Chris Lima", 1956, "189.052.396.66")

        print('\n')
        # buscar um professor
        print("Buscando um professor...")
        t = self.teacher_crud.read("Chris Lima")

        print(t[0].data()['t']['name'])
        print(t[0].data()['t']['ano_nasc'])
        print(t[0].data()['t']['cpf'])

        print('\n'*2)

        # atualizar um professor
        print("Atualizando um professor...")
        self.teacher_crud.update("Chris Lima", "162.052.777-77")
        t = self.teacher_crud.read("Chris Lima")
        print(t[0].data()['t']['name'])
        print(t[0].data()['t']['ano_nasc'])
        print(t[0].data()['t']['cpf'])
