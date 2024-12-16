from src.managers.simple_book_manager import SimpleBookManager


class ManagerFactories:
    @staticmethod
    def get_book_manager(manager_type, repo):
        if manager_type == 'simple':
            return SimpleBookManager(repo)
        else:
            raise ValueError(f"Unknown manager type: {manager_type}")