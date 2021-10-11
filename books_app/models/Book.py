from books_app.config.MySQLConnection import connectToMySQL
from books_app.models.Author import Author

class Book:
    def __init__(self, id, title, num_of_pages, created_at, updated_at):
        self.id = id
        self.title = title
        self.num_of_pages = num_of_pages
        self.created_at = created_at
        self.updated_at = updated_at
        self.authors = []



    @classmethod
    def get_all_books( cls ):
        query = "SELECT* FROM books;"
        results = connectToMySQL('books_db').query_db(query)

        books = []
        for element in results:
            books.append( Book( element['id'], element['title'], element['num_of_pages'], element['created_at'], element['updated_at'] ) )
        return books


    @classmethod
    def add_book( cls, book_name, book_pages ):
        query = "INSERT INTO books( title, num_of_pages ) VALUES ( %(title)s, %(num_of_pages)s );"
        data = {
            "title": book_name,
            "num_of_pages": book_pages
        }
        results = connectToMySQL('books_db').query_db(query, data)
        print(results)
        return results


    @classmethod 
    def get_by_id( cls, dataID ):
        query = "SELECT* FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON authors.id = favorites.author_id  WHERE books.id = %(id)s;"
        data = {
            "id": dataID
        }
        results = connectToMySQL('books_db').query_db(query, data)

        books = Book( results[0]['id'], results[0]['title'], results[0]['num_of_pages'], results[0]['created_at'], results[0]['updated_at'] )

        for row in results:
            if Author( row['id'], row['name'], row['created_at'], row['updated_at'] ) == None:
                break
            books.authors.append( Author( row['id'], row['name'], row['created_at'], row['updated_at'] ) )
        return books

    @classmethod
    def add_fav(cls, authorID, bookID):
        query = "INSERT INTO favorites( author_id, book_id ) VALUES ( %(author_id)s, %(book_id)s );"
        data ={
            "author_id" : authorID,
            "book_id" : bookID
        }
        results = connectToMySQL('books_db').query_db(query, data)
        return results

    @classmethod
    def unfavorited_books(cls, infoID):
        query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM favorites WHERE author_id = %(id)s );"
        data = {
            "id": infoID
        }
        results = connectToMySQL('books_db').query_db(query, data)
        print(results)
        print('hello')
        books = []
        for element in results:
            books.append( Book( element['id'], element['title'], element['num_of_pages'], element['created_at'], element['updated_at'] ) )
        return books
        