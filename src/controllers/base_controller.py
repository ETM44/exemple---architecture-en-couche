from abc import ABC


class BaseController(ABC):
    def __init__(self, manager, view):
        """
        Initialise le contrôleur avec un gestionnaire et une vue.
        :param manager: Instance de Manager.
        :param view: Instance de View.
        """
        self.manager = manager
        self.view = view

        # Connecter les signaux
        view.connect_signals(self)