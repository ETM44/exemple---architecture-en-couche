class BookEntity:
    def __init__(self, id=None, title=None, author=None, published_date=None, genre=None):
        self.id = id
        self.title = title
        self.author = author
        self.published_date = published_date
        self.genre = genre

    def __str__(self):
        return f"BookEntity(id={self.id}, title={self.title}, author={self.author}, " \
               f"published_date={self.published_date}, genre={self.genre})"
