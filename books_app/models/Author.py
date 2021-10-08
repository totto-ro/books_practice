from flask.globals import request
from books_app.config.MySQLConnection import connectToMySQL

class Author:
    def __init__(self, id, name, created_at, updated_at):
        self.id = id 
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def get_all_authors( cls ):
        query = "SELECT* FROM authors;"
        results = connectToMySQL('books_db').query_db(query)

        authors = []
        for element in results:
            authors.append( Author( element['id'], element['name'], element['created_at'], element['updated_at'] ) )
        return authors

    @classmethod
    def add_author( cls, author_id ):
        query = "INSERT INTO authors( name ) VALUES ( %(name)s );"
        data = {
            "name": author_id
        }
        results = connectToMySQL('books_db').query_db(query, data)
        print(results)
        return results

