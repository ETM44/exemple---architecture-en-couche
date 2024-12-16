from abc import ABC, abstractmethod

from src.entities.book_entity import BookEntity


class IBookManager(ABC):
    @abstractmethod
    def add_book(self, book_entity: BookEntity) -> BookEntity:
        pass

    @abstractmethod
    def get_all_books(self):
        pass
    
    @abstractmethod
    def get_book_by_id(self, book_id):
        pass

    @abstractmethod
    def update_book(self, book_entity):
        pass

    @abstractmethod
    def delete_book(self, book_id):
        pass