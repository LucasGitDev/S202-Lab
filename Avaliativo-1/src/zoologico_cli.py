from zoologico_dao import ZoologicoDAO
from models.animal import Animal
from models.habitat import Habitat
from models.cuidador import Cuidador


class ZoologicoCLI:
    def __init__(self, zoologico_dao: ZoologicoDAO) -> None:
        self.zoologico_dao = zoologico_dao
        self.funcs = {
            1: self.__createAnimal,
            2: self.__readAnimal,
            3: self.__readAnimals,
            4: self.__updateAnimal,
            5: self.__deleteAnimal
        }

    def __validate_option(self, prompt):
        while True:
            try:
                op = int(input(prompt))
            except ValueError:
                print("Opção inválida, tente novamente.")
                continue
            else:
                return op

    def __options(self,):
        print("1 - Cadastrar animal")
        print("2 - Pesquisar animal")
        print("3 - Listar animais")
        print("4 - Atualizar animal")
        print("5 - Remover animal")
        print("6 - Sair")

    def menu(self):
        op = 1
        while op in self.funcs:
            self.__options()
            op = self.__validate_option("Digite a opção desejada: ")
            if op in self.funcs:
                self.funcs[op]()
                print()
                print("Operação realizada com sucesso!")
                print()
                print("#" * 20)
                print()
            else:
                break

    def __createAnimal(self):
        def validate_idate():
            while True:
                try:
                    idate = int(input("Idade:"))
                    if idate < 0:
                        raise ValueError
                except ValueError:
                    print("Idade inválida, tente novamente.")
                    continue
                else:
                    return idate

        print("#" * 20)
        print("- Cadastro de animal -")

        print('Informações do Cuidador')
        nome_cuidador = input("Nome: ")
        documento_cuidador = input("Documento: ")
        id_cuidador = input("Id: ")
        cuidador = Cuidador(nome_cuidador, documento_cuidador, id_cuidador)

        print("Informações do Habitat")
        nome_habitat = input("Nome: ")
        tipo_ambiente = input("Tipo de ambiente: ")
        id_habitat = input("Id: ")
        habitat = Habitat(nome_habitat, tipo_ambiente, cuidador, id_habitat)

        print("Informações do Animal")
        nome_animal = input("Nome: ")
        especie = input("Especie: ")
        idade = validate_idate()
        animal = Animal(nome_animal, especie, idade, habitat)

        self.zoologico_dao.createAnimal(animal)

    def __readAnimal(self):
        print("#" * 20)
        print("- Pesquisar um animal -")

        animal_id = input("Digite o id do animal: ")

        animal = self.zoologico_dao.readAnimal(animal_id)

        if animal is None:
            print("Animal não encontrado.")
            return

        print("Resultado da pesquisa:")
        print("Nome:", animal.nome)
        print("Especie:", animal.especie)
        print("Idade:", animal.idade)
        print("Habitat:", animal.habitat.nome)
        print("Tipo de ambiente:", animal.habitat.tipo_ambiente)
        print("Cuidador:", animal.habitat.cuidador.nome)
        print("Documento do Cuidador:", animal.habitat.cuidador.documento)

    def __readAnimals(self):
        print("#" * 20)
        print("- Lista de animais -")
        listed = self.zoologico_dao.readAnimals()

        animais = [Animal.deserialize(animal) for animal in listed]

        if len(animais) == 0:
            print("Nenhum animal encontrado.")
            return

        print("Resultado da pesquisa:")
        print()
        for animal in animais:
            print("Id:", animal.id)
            print("Nome:", animal.nome)
            print("Especie:", animal.especie)
            print("Idade:", animal.idade)
            print("Habitat:", animal.habitat.nome)
            print("Tipo de ambiente:", animal.habitat.tipoAmbiente)
            print("Cuidador:", animal.habitat.cuidador.nome)
            print("Documento do Cuidador:", animal.habitat.cuidador.documento)
            print('-' * 20)

    def __updateAnimal(self):
        print("#" * 20)
        print("- Atualizar registro de animal -")

        id_animal = input("Digite o id do animal: ")

        animal = self.zoologico_dao.readAnimal(id_animal)

        if animal is None:
            print("Animal não encontrado.")
            return

        print("Atualize apenas os campos que deseja alterar.")

        animal['nome'] = input("Nome: ") or animal['nome']
        animal['especie'] = input("Especie: ") or animal['especie']
        animal['idade'] = input("Idade: ") or animal['idade']
        animal['habitat']['id'] = input(
            "Id do Habitat: ") or animal['habitat']['id']
        animal['habitat']['nome'] = input(
            "Habitat: ") or animal['habitat']['nome']
        animal['habitat']['tipoAmbiente'] = input(
            "Tipo de ambiente: ") or animal['habitat']['tipoAmbiente']
        animal['habitat']['cuidador']['id'] = input(
            "Id do Cuidador: ") or animal['habitat']['cuidador']['id']
        animal['habitat']['cuidador']['nome'] = input(
            "Cuidador: ") or animal['habitat']['cuidador']['nome']
        animal['habitat']['cuidador']['documento'] = input(
            "Documento do Cuidador: ") or animal['habitat']['cuidador']['documento']

        updated_animal = self.zoologico_dao.updateAnimal(id_animal, Animal.deserialize(animal))

        if updated_animal is None:
            print("Animal não encontrado.")
            return

        print("Animal atualizado com sucesso!")

    def __deleteAnimal(self):
        print("#" * 20)
        print("- Deletar animal -")

        animal_id = input("Digite o id do animal: ")

        deleted_animal = self.zoologico_dao.deleteAnimal(animal_id)

        if (deleted_animal is None):
            print("Animal não encontrado.")
            return

        if (deleted_animal.deleted_count > 0):
            print("Animal deletado com sucesso!")
        else:
            print("Animal não encontrado.")
