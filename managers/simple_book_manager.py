import re 
from entities.book_entity import BookEntity
from managers.Interfaces.ibook_manager import IBookManager
from managers.base_manager import BaseManager

class SimpleBookManager(IBookManager, BaseManager):
    def add_book(self, book_entity: BookEntity) -> BookEntity:
        """
        Ajoute un livre via le repository et retourne le livre avec son ID.
        :return: BookEntity.
        """
        date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')

        if (book_entity.published_date and 
            not date_pattern.match(book_entity.published_date)):
            
            return book_entity

        if (not book_entity.title == "" and
            not book_entity.author == "" and
            not book_entity.published_date == "" and
            not book_entity.genre == ""):

            book_entity.id = self.repository.create(book_entity)
        
        return book_entity

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

