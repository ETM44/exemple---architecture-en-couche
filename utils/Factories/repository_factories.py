from repositories.simple_book_repository import SimpleBookRepository

class RepositoryFactories:
    @staticmethod
    def get_book_repository(repository_type, host="localhost", database="library", user="myuser", password="mypassword"):
        if repository_type == 'simple':
            return SimpleBookRepository(host, database, user, password)
        else:
            raise ValueError(f"Unknown manager type: {repository_type}")