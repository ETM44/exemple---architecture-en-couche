from controllers.simple_book_controller import SimpleBookController


class ControllerFactories:
    @staticmethod
    def get_book_controller(controller_type, manager, view):
        if controller_type == 'simple':
            return SimpleBookController(manager, view)
        else:
            raise ValueError(f"Unknown manager type: {controller_type}")