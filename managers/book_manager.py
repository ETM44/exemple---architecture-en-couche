from entities.book_entity import BookEntity

class BookManager:
    def __init__(self, repository):
        """
        Initialise le gestionnaire avec une instance de BookRepository.
        """
        self.repository = repository

    def add_book(self, book_entity: BookEntity):
        """
        Ajoute un livre via le repository et retourne l'ID généré.
        :return: ID du livre créé ou None.
        """
        return self.repository.create(book_entity)

    def get_all_books(self):
        """
        Récupère tous les livres.
        :return: Liste d'objets BookEntity.
        """
        return self.repository.read_all()

    def get_book_by_id(self, book_id):
        """
        Récupère un livre par son ID.
        :return: Instance de BookEntity ou None.
        """
        return self.repository.read_by_id(book_id)

    def update_book(self, book_entity):
        """
        Met à jour un livre et retourne l'entité mise à jour.
        :return: Instance de BookEntity mise à jour ou None.
        """
        return self.repository.update(book_entity)

    def delete_book(self, book_id):
        """
        Supprime un livre.
        :return: Booléen indiquant si la suppression a réussi.
        """
        return self.repository.delete(book_id)

