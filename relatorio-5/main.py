from database_service import DatabaseService
from book_service import BookService
from book_model import Book
from utils import writeAJson
from datetime import datetime


def prettyPrintBook(book: Book):
    print("----Livro----")
    print(f"Id: {book.id}")
    print(f"Titulo: {book.title}")
    print(f"Autor: {book.author}")
    print(f"Ano: {book.year}")
    print(f"Preco: {book.price}")
    print("----Fim do livro----")


def menu():
    print()
    print("-" * 20)
    print("#" * 20)
    print("-" * 20)
    print("----Menu----")
    print("1 - Inserir livro")
    print("2 - Atualizar livro")
    print("3 - Remover livro")
    print("4 - Listar livros")
    print("5 - Sair")
    return int(input("Digite a opcao desejada: "))


def insertBook(book_service: BookService):
    print("----Inserir livro----")
    print("Digite os dados do livro:")
    title = input("Titulo: ")
    author = input("Autor: ")
    year = int(input("Ano: "))
    price = float(input("Preco: "))

    book = Book(title, author, year, price)

    created_book = book_service.create(book)
    prettyPrintBook(created_book)
    writeAJson(created_book.serialize(), f'book-created-{created_book.id}')


def updateBook(book_service: BookService):
    print("----Atualizar livro----")
    print("Digite o id do livro:")
    book_id = input("Id: ")

    book = book_service.findOneById(book_id)
    if book == None:
        print("Livro nao encontrado")
        return

    print("Digite os dados do livro (deixe em branco para manter o valor atual):")
    title = input("Titulo: ")
    author = input("Autor: ")
    year = input("Ano: ")
    price = input("Preco: ")

    book.title = title if title != "" and title != None else book.title
    book.author = author if author != "" and author != None else book.author
    book.year = int(year) if year != "" and year != None else book.year
    book.price = float(
        price) if price != "" and price != None else book.price

    updated_book = book_service.update(book)
    prettyPrintBook(updated_book)
    writeAJson(updated_book.serialize(),
               f'book-updated-{updated_book.id}.{datetime.now()}')


def deleteBook(book_service: BookService):
    print("----Remover livro----")
    print("Digite o id do livro:")
    book_id = input("Id: ")

    if book_service.delete(book_id):
        print("Livro removido com sucesso")
    else:
        print("Erro ao remover livro")


def listBooks(book_service: BookService):
    print("----Listar livros----")
    books = book_service.findAll()

    writeAJson([book.serialize() for book in books],
               f'books-listed.{datetime.now()}')

    for book in books:
        prettyPrintBook(book)


def findBookById(book_service: BookService):
    print("----Buscar livro por ID----")
    print("Digite o id do livro:")
    book_id = input("Id: ")

    book = book_service.findOneById(book_id)
    prettyPrintBook(book)
    writeAJson(book.serialize(), f'book-found-{book.id}')


def main():
    db = DatabaseService("relatorio5")
    collection = db.createCollectionIfNotExists("books", Book.getSchema())
    book_service = BookService(collection)
    menu_option = 0
    while menu_option != 5:
        menu_option = menu()
        print()
        print('-'*20)
        print('-'*20)
        print()
        if menu_option == 1:
            insertBook(book_service)
        elif menu_option == 2:
            updateBook(book_service)
        elif menu_option == 3:
            deleteBook(book_service)
        elif menu_option == 4:
            listBooks(book_service)
        elif menu_option == 5:
            print("Saindo...")
        else:
            print("Opcao invalida")


if __name__ == "__main__":
    main()
