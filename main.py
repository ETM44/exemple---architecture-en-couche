from dotenv import load_dotenv
import os
import sys

from controllers.interfaces.ibook_controller import IBookController
from managers.interfaces.ibook_manager import IBookManager
from repositories.interfaces.ibook_repository import IBookRepository
from utils.factories.controller_factories import ControllerFactories
from utils.factories.manager_factories import ManagerFactories
from utils.factories.repository_factories import RepositoryFactories
from utils.factories.view_factories import ViewFactories
from PyQt5.QtWidgets import QApplication

from views.intefaces.i_book_view import IBookView

if __name__ == "__main__":

    app = QApplication(sys.argv)


    load_dotenv()


    repo: IBookRepository = RepositoryFactories.get_book_repository("simple", 
                                                                    host=os.getenv("DB_HOST"), 
                                                                    database=os.getenv("DB_DATABASE"), 
                                                                    user=os.getenv("DB_USER"), 
                                                                    password=os.getenv("DB_PASSWORD"))

    manager: IBookManager = ManagerFactories.get_book_manager("simple", repo)

    view: IBookView = ViewFactories.get_book_view("simple")

    controller: IBookController = ControllerFactories.get_book_controller("simple", manager, view)

    view.show()




    repo2: IBookRepository = RepositoryFactories.get_book_repository("simple", 
                                                                        host=os.getenv("DB_HOST"), 
                                                                        database=os.getenv("DB_DATABASE"), 
                                                                        user=os.getenv("DB_USER"), 
                                                                        password=os.getenv("DB_PASSWORD"))

    manager2: IBookManager = ManagerFactories.get_book_manager("simple", repo2)

    view2: IBookView = ViewFactories.get_book_view("simple")

    controller2: IBookController = ControllerFactories.get_book_controller("simple", manager2, view2)

    view2.show()




    sys.exit(app.exec_())