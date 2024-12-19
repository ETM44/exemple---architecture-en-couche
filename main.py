# Fonction pour créer une fenêtre
import os
import sys
from dotenv import load_dotenv
from src.controllers.Interfaces.ibook_controller import IBookController
from src.utils.factories.abstract_factory import AbstractFactory
from src.utils.factories.simple_factory import SimpleFactory


def create_window(factory: AbstractFactory, db_params: dict) -> IBookController:
    repo = factory.create_repository(db_params)
    manager = factory.create_manager(repo)
    view = factory.create_view()
    controller = factory.create_controller(manager, view)
    return controller

if __name__ == "__main__":
    #app = QApplication(sys.argv)

    # Charger les variables d'environnement
    load_dotenv()
    db_params = {
        "DB_HOST": os.getenv("DB_HOST"),
        "DB_DATABASE": os.getenv("DB_DATABASE"),
        "DB_USER": os.getenv("DB_USER"),
        "DB_PASSWORD": os.getenv("DB_PASSWORD")
    }

    # Utilisation du Factory Method
    factory = SimpleFactory()

    # Création et affichage des deux fenêtres
    controller1 = create_window(factory, db_params)
    controller2 = create_window(factory, db_params)

    #sys.exit(app.exec_())