from src.controllers.Interfaces.ibook_controller import IBookController
from src.controllers.simple_book_controller import SimpleBookController
from src.managers.Interfaces.ibook_manager import IBookManager
from src.managers.simple_book_manager import SimpleBookManager
from src.repositories.Interfaces.ibook_repository import IBookRepository
from src.repositories.simple_book_repository import SimpleBookRepository
from src.utils.factories.abstract_factory import AbstractFactory
from src.views.Intefaces.i_book_view import IBookView
from src.views.simple_book_view import SimpleBookView


class SimpleFactory(AbstractFactory):
    def create_repository(self, db_params: dict) -> IBookRepository:
        return SimpleBookRepository(
            host=db_params["DB_HOST"],
            database=db_params["DB_DATABASE"],
            user=db_params["DB_USER"],
            password=db_params["DB_PASSWORD"]
        )

    def create_manager(self, repository: IBookRepository) -> IBookManager:
        return SimpleBookManager(repository)

    def create_view(self) -> IBookView:
        return SimpleBookView()

    def create_controller(self, manager: IBookManager, view: IBookView) -> IBookController:
        return SimpleBookController(manager, view)