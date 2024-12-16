from src.repositories.simple_book_repository import SimpleBookRepository

class RepositoryFactories:
    @staticmethod
    def get_book_repository(repository_type, **kwargs):
        if repository_type == 'simple':
            return SimpleBookRepository(
                host=kwargs.get("host"),
                database=kwargs.get("database"),
                user=kwargs.get("user"),
                password=kwargs.get("password")
            )
        else:
            raise ValueError(f"Unknown manager type: {repository_type}")