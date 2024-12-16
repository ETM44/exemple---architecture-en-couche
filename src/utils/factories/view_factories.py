from src.views.simple_book_view import SimpleBookView


class ViewFactories:
    @staticmethod
    def get_book_view(view_type):
        if view_type == 'simple':
            return SimpleBookView()
        else:
            raise ValueError(f"Unknown manager type: {view_type}")