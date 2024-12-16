from src.entities.book_entity import BookEntity

class BookController:
    def __init__(self, manager, view):
        """
        Initialise le contrôleur avec un gestionnaire et une vue.
        :param manager: Instance de BookManager.
        :param view: Instance de BookView.
        """
        self.manager = manager
        self.view = view

        # Connecter les signaux
        self.view.connect_signals(self)

    def add_book(self):
        """
        Ajoute un livre via les données saisies dans la vue.
        """
        book_entity: BookEntity = self.view.get_book_input()

        book_entity = self.manager.add_book(book_entity)

        if book_entity.id:
            self.view.display_book(book_entity)
            self.view.show_message(f"Livre ajouté avec succès avec l'ID : {book_entity.id}")
        else:
            self.view.show_message(f"Echec de l'ajout du Livre")

    def update_book(self):
        """
        Met à jour un livre via les données saisies dans la vue.
        """
        book_entity = self.view.get_book_input()
        updated_book = self.manager.update_book(book_entity)
        if updated_book:
            self.view.show_message(f"Livre mis à jour avec succès : {updated_book}")
        else:
            self.view.show_message("Mise à jour échouée : Livre non trouvé.")

    def delete_book(self):
        """
        Supprime un livre via son ID saisi dans la vue.
        """
        book_id = self.view.get_book_id()
        is_deleted = self.manager.delete_book(book_id)
        if is_deleted:
            self.view.show_message(f"Livre avec l'ID {book_id} supprimé avec succès.")
        else:
            self.view.show_message("Échec de la suppression : Livre non trouvé.")

    def show_all_books(self):
        """
        Affiche tous les livres disponibles.
        """
        books = self.manager.get_all_books()
        self.view.display_books(books)

    def show_book_by_id(self):
        """
        Affiche un livre spécifique via son ID.
        """
        book_id = self.view.get_book_id()
        book = self.manager.get_book_by_id(book_id)
        if book:
            self.view.display_book(book)
        else:
            self.view.show_message("Livre non trouvé.")

