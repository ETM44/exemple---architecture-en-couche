from abc import ABC, abstractmethod

from src.controllers.Interfaces.ibook_controller import IBookController
from src.managers.Interfaces.ibook_manager import IBookManager
from src.repositories.Interfaces.ibook_repository import IBookRepository
from src.views.Intefaces.i_book_view import IBookView


class AbstractFactory(ABC):
    @abstractmethod
    def create_repository(self, db_params: dict) -> IBookRepository:
        pass

    @abstractmethod
    def create_manager(self, repository: IBookRepository) -> IBookManager:
        pass

    @abstractmethod
    def create_view(self) -> IBookView:
        pass

    @abstractmethod
    def create_controller(self, manager: IBookManager, view: IBookView) -> IBookController:
        pass
