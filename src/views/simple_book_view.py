from PyQt5.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
)

from src.entities.book_entity import BookEntity
from src.views.Intefaces.i_book_view import IBookView
from src.views.base_view import BaseView

class SimpleBookView(IBookView, BaseView):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion des Livres")
        self.setGeometry(100, 100, 600, 400)

        # Mise en page principale
        self.layout = QVBoxLayout()

        # Formulaire pour ajouter ou mettre à jour un livre
        self.form_layout = QVBoxLayout()
        self.title_input = self.create_input_field("Titre")
        self.author_input = self.create_input_field("Auteur")
        self.published_date_input = self.create_input_field("Date de publication (YYYY-MM-DD)")
        self.genre_input = self.create_input_field("Genre")
        self.book_id_input = self.create_input_field("ID (pour mise à jour ou suppression)")

        # Boutons d'action
        self.button_layout = QHBoxLayout()
        self.add_button = QPushButton("Ajouter")
        self.update_button = QPushButton("Mettre à jour")
        self.delete_button = QPushButton("Supprimer")
        self.view_all_button = QPushButton("Afficher tous les livres")

        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.update_button)
        self.button_layout.addWidget(self.delete_button)
        self.button_layout.addWidget(self.view_all_button)

        # Tableau pour afficher les livres
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Titre", "Auteur", "Date de publication", "Genre"])
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)

        # Assemblage des layouts
        self.layout.addLayout(self.form_layout)
        self.layout.addLayout(self.button_layout)
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

    def create_input_field(self, label_text):
        """
        Crée un champ de saisie avec une étiquette.
        :param label_text: Texte de l'étiquette.
        :return: Instance de QLineEdit.
        """
        layout = QHBoxLayout()
        label = QLabel(label_text)
        input_field = QLineEdit()
        layout.addWidget(label)
        layout.addWidget(input_field)
        self.form_layout.addLayout(layout)
        return input_field

    def get_book_input(self):
        """
        Récupère les données du formulaire pour ajouter ou mettre à jour un livre.
        Si l'ID est présent, il est inclus dans l'entité pour une mise à jour.
        :return: Instance de BookEntity.
        """
        book_id = self.book_id_input.text()
        return BookEntity(
            id=int(book_id) if book_id else None,  # Inclure l'ID si présent
            title=self.title_input.text(),
            author=self.author_input.text(),
            published_date=self.published_date_input.text(),
            genre=self.genre_input.text()
        )

    def get_book_id(self):
        """
        Récupère l'ID du livre à partir du formulaire.
        :return: ID du livre ou None si non renseigné.
        """
        book_id = self.book_id_input.text()
        return int(book_id) if book_id else None

    def display_books(self, books: list[BookEntity]):
        """
        Affiche une liste de livres dans le tableau.
        :param books: Liste d'objets BookEntity.
        """
        self.table.setRowCount(len(books))
        for row, book in enumerate(books):
            self.table.setItem(row, 0, QTableWidgetItem(str(book.id)))
            self.table.setItem(row, 1, QTableWidgetItem(book.title))
            self.table.setItem(row, 2, QTableWidgetItem(book.author))
            self.table.setItem(row, 3, QTableWidgetItem(book.published_date.strftime("%Y-%m-%d")))
            self.table.setItem(row, 4, QTableWidgetItem(book.genre))

    def display_book(self, book: BookEntity):
        """
        Affiche les détails d'un seul livre dans le formulaire.
        :param book: Instance de BookEntity.
        """
        self.book_id_input.setText(str(book.id))
        self.title_input.setText(book.title)
        self.author_input.setText(book.author)
        self.published_date_input.setText(book.published_date)
        self.genre_input.setText(book.genre)

    def show_message(self, message):
        """
        Affiche un message à l'utilisateur via une boîte de dialogue.
        :param message: Message à afficher.
        """
        QMessageBox.information(self, "Information", message)

    def connect_signals(self, controller):
        """
        Connecte les signaux des boutons aux méthodes du contrôleur.
        :param controller: Instance de BookController.
        """
        self.add_button.clicked.connect(controller.add_book)
        self.update_button.clicked.connect(controller.update_book)
        self.delete_button.clicked.connect(controller.delete_book)
        self.view_all_button.clicked.connect(controller.show_all_books)
