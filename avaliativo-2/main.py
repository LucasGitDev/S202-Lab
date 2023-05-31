from database import Database

from exercise_one import ExerciseOne
from exercise_two import ExerciseTwo
from exercise_three import ExerciseThree


def show_menu_exercises():
    print('Escolha um exercício para executar: ')
    print('1 - Exercício 1')
    print('2 - Exercício 2')
    print('3 - Exercício 3')
    print('4 - Sair')


def validate_exercise_option():
    op = int(input("Digite a opção: "))
    while op < 1 or op > 4:
        print("Opção inválida")
        op = int(input("Digite a opção: "))
    return op


def exercise_1(db: Database):
    ExerciseOne(db).run()


def exercise_2(db: Database):
    ExerciseTwo(db).run()


def exercise_3(db: Database):
    ExerciseThree(db).run()


def main():
    db = Database("bolt://44.193.5.126:7687", "neo4j",
                  "restraints-cheeses-hunk")

    while True:
        show_menu_exercises()
        option = validate_exercise_option()
        if option == 1:
            exercise_1(db)
        elif option == 2:
            exercise_2(db)
        elif option == 3:
            exercise_3(db)
        else:
            break

    db.close()


if __name__ == "__main__":
    main()
