from flask import render_template, redirect, request
from books_app import app
from books_app.models.Book import Book
from books_app.models.Author import Author

@app.route( '/', methods=['GET'] )
def index():
    return redirect( "/authors" )

@app.route( '/authors', methods=['GET'] )
def allAuthorsPage():
    authors = Author.get_all_authors()
    return render_template( "authors.html", authors = authors )

@app.route( "/authors/add", methods=['POST'] )
def add_author():
    author_id = request.form[ 'name' ]
    result = Author.add_author( author_id )
    print( result )
    return redirect( '/authors' )


@app.route( '/author/<int:id>', methods=['GET'] )
def show_author( id ):
    idInfo = id
    results = Author.get_by_id_author( idInfo )
    print(results.books)
    unfavorited_books = Book.unfavorited_books( idInfo )
    return render_template( "authors_favorite.html", authors = results, unfavorited_books = unfavorited_books)

@app.route( '/author/fav', methods=['POST'] )
def addFavorite( ):
    authorID = request.form[ 'author_id' ]
    bookID = request.form[ 'book_id' ]
    result = Book.add_fav( authorID, bookID )
    print( result )
    return redirect(f"/book/{request.form['book_id']}")

