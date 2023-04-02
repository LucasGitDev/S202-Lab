from book_model import Book
from pymongo import collection
from bson.objectid import ObjectId


class BookService:

    def __init__(self, book_repository):
        self.book_repository: collection = book_repository

    def create(self, book: Book) -> Book:
        try:
            result = self.book_repository.insert_one(book.serialize())
            return self.findOneById(result.inserted_id)
        except Exception as e:
            print(f'Error: {e}')
            return None

    def update(self, book: Book) -> Book:
        try:
            result = self.book_repository.update_one(
                {'_id': book.id},
                {'$set': book.serialize()}
            )
            print(result.modified_count)
            if result.modified_count == 0:
                return None

            return self.findOneById(book.id)
        except Exception as e:
            print(f'Error: {e}')
            return None

    def findOneById(self, id) -> Book:
        try:
            result = self.book_repository.find_one({'_id': ObjectId(id)})
            if result is None:
                return None
            return Book.deserialize(result)
        except Exception as e:
            print(f'Error: {e}')
            return None

    def findAll(self) -> list:
        try:
            result = self.book_repository.find()
            return [Book.deserialize(book) for book in result]
        except Exception as e:
            print(f'Error: {e}')
            return None

    def delete(self, id) -> bool:
        try:
            result = self.book_repository.delete_one({'_id': ObjectId(id)})
            if result.deleted_count == 0:
                return False
            return True
        except Exception as e:
            print(f'Error: {e}')
            return False
