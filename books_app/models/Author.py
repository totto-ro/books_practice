from flask.globals import request
from books_app.config.MySQLConnection import connectToMySQL
from books_app.models import Book

class Author:
    def __init__(self, id, name, created_at, updated_at):
        self.id = id 
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
        self.books = []


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

    # @classmethod
    # def unfavorited_authors( cls, authorsByID ):
    #     query = "SELECT* FROM authors WHERE authors.id NOT IN ( SELECT author_id FROM favorites WHERE book_id = %( id )s );"
    #     data = {
    #         "id": authorsByID
    #     }
    #     print(data)

    #     results = connectToMySQL('books_db').query_db(query, data)
    #     print(results)
    #     print('hello')

    #     authors = []
    #     for element in results:
    #         authors.append( Author( element['id'], element['name'], element['created_at'], element['updated_at'] ) )
    #     return authors

    @classmethod 
    def get_by_id_author( cls, idInfo ):
        query = "SELECT* FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;"
        data = {
            "id": idInfo
        }
        results = connectToMySQL('books_db').query_db(query, data)

        authors = Author( results[0]['id'], results[0]['name'], results[0]['created_at'], results[0]['updated_at'] )

        for row in results:
            authors.books.append( Book.Book( row['id'], row['title'], row['num_of_pages'], row['created_at'], row['updated_at'] ) )
        return authors
