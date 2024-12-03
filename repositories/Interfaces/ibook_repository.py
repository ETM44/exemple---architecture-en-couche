from abc import ABC, abstractmethod
from repositories.base_repository import BaseRepository

class IBookRepository(ABC):
    @abstractmethod
    def create(self, book_entity) -> int:
        pass

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def read_by_id(self, book_id):
        pass

    @abstractmethod
    def update(self, book_entity):
        pass

    @abstractmethod
    def delete(self, book_id):
        pass
