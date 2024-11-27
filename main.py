import sys

from managers.book_manager import BookManager
from repositories.book_repository import BookRepository
from views.book_view import BookView
from controllers.book_controller import BookController
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":

    app = QApplication(sys.argv)

    repo = BookRepository(host="localhost", database="library", user="myuser", password="mypassword")
    
    manager = BookManager(repo)

    view = BookView()
    
    controller = BookController(manager, view)

    # Connecter les signaux et afficher la fenêtre
    view.connect_signals(controller)
    view.show()

    sys.exit(app.exec_())