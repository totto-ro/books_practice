from books_app.config.MySQLConnection import connectToMySQL

class Book:
    def __init__(self, id, title, num_of_pages, created_at, updated_at):
        self.id = id
        self.title = title
        self.num_of_pages = num_of_pages
        self.created_at = created_at
        self.updated_at = updated_at
