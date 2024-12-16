from abc import ABC


class BaseManager(ABC):
    def __init__(self, repository):
        """
        Initialise le gestionnaire avec une instance de Repository.
        """
        self.repository = repository