from abc import ABC, abstractmethod
from src.entities.book_entity import BookEntity
from PyQt5.QtWidgets import QWidget

class IBookView(QWidget):
    @abstractmethod
    def create_input_field(self, label_text):
        pass

    @abstractmethod
    def get_book_input(self):
        pass

    @abstractmethod
    def get_book_id(self):
        pass

    @abstractmethod
    def display_books(self, books: list[BookEntity]):
        pass

    @abstractmethod
    def display_book(self, book: BookEntity):
        pass

    @abstractmethod
    def show_message(self, message):
        pass

    @abstractmethod
    def connect_signals(self, controller):
        pass

