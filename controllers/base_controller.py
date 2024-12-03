class BaseController:
    def __init__(self, manager, view):
        """
        Initialise le contrôleur avec un gestionnaire et une vue.
        :param manager: Instance de Manager.
        :param view: Instance de View.
        """
        self.manager = manager
        self.view = view