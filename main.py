import sys

from controllers.Interfaces.ibook_controller import IBookController
from managers.Interfaces.ibook_manager import IBookManager
from repositories.Interfaces.ibook_repository import IBookRepository
from utils.Factories.controller_factories import ControllerFactories
from utils.Factories.manager_factories import ManagerFactories
from utils.Factories.repository_factories import RepositoryFactories
from utils.Factories.view_factories import ViewFactories
from PyQt5.QtWidgets import QApplication

from views.Intefaces.i_book_view import IBookView

if __name__ == "__main__":

    app = QApplication(sys.argv)




    repo: IBookRepository = RepositoryFactories.get_book_repository("simple")

    manager: IBookManager = ManagerFactories.get_book_manager("simple", repo)

    view: IBookView = ViewFactories.get_book_view("simple")
    
    controller: IBookController = ControllerFactories.get_book_controller("simple", manager, view)

    # Connecter les signaux et afficher la fenêtre
    view.connect_signals(controller)
    view.show()




    repo2: IBookRepository = RepositoryFactories.get_book_repository("simple")

    manager2: IBookManager = ManagerFactories.get_book_manager("simple", repo2)

    view2: IBookView = ViewFactories.get_book_view("simple")
    
    controller2: IBookController = ControllerFactories.get_book_controller("simple", manager2, view2)

    # Connecter les signaux et afficher la fenêtre
    view2.connect_signals(controller2)
    view2.show()




    sys.exit(app.exec_())