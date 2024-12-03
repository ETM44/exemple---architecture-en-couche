from abc import ABC, abstractmethod
from entities.book_entity import BookEntity

class IBookController(ABC):
    @abstractmethod
    def add_book(self):
        pass

    @abstractmethod
    def update_book(self):
        pass

    @abstractmethod
    def delete_book(self):
        pass

    @abstractmethod
    def show_all_books(self):
        pass

    @abstractmethod
    def show_book_by_id(self):
        pass

