class Animal:
    def __init__(self, nome: str, idade: int, especie: str, cor: str, som: str):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.cor = cor
        self.som = som

    def emitir_som(self):
        print(self.som)

    def mudar_cor(self, nova_cor):
        self.cor = nova_cor

    def set_som(self, novo_som):
        self.som = novo_som


class Elefante(Animal):
    def __init__(self, nome, idade, especie, cor, som, tamanho):
        super().__init__(nome, idade, especie, cor, som)
        self.tamanho = tamanho

    def trombar(self):
        print(self.som)

    def mudar_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho


def change(elefante: Elefante):
    if elefante.especie == 'Africano' and elefante.idade < 10:
        elefante.mudar_tamanho('pequeno')
        elefante.set_som("Paaah")
        print(f'Novo som: {elefante.som}')
        print(f'Novo tamanho: {elefante.tamanho}')
    elif elefante.especie == 'Africano' and elefante.idade >= 10:
        elefante.mudar_tamanho('grande')
        elefante.set_som("PAHHHHHH")
        print(f'Novo som: {elefante.som}')
        print(f'Novo tamanho: {elefante.tamanho}')


def main():
    nome = input("Digite o nome do elefante: ")
    idade = int(input("Digite a idade do elefante: "))
    especie = input("Digite a especie do elefante: ")
    cor = input("Digite a cor do elefante: ")
    tamanho = input("Digite o tamanho do elefante: ")

    eleph = Elefante(nome, idade, especie, cor, "Pah", tamanho)

    eleph.trombar()  # ou eleph.emitir_som()

    change(eleph)


if __name__ == '__main__':
    main()
