# endpoints related to the users

from flask import render_template, redirect, request
from books_app import app
from books_app.models.Author import Author
from books_app.models.Book import Book

@app.route( '/', methods=['GET'] )
def indexBooks():
    return redirect( "/books" )

@app.route( '/books', methods=['GET'] )
def allBooksPage():
    books = Book.get_all_books()
    return render_template( "books.html", books = books )


@app.route( "/books/add", methods=['POST'] )
def add_book():
    book_name = request.form[ 'title' ]
    book_pages = request.form[ 'num_of_pages' ]
    result = Book.add_book( book_name, book_pages )
    print( result )
    return redirect( '/books' )


@app.route( '/book/<int:id>', methods=['GET'] )
def show_book( id ):
    dataID = id
    results = Book.get_by_id( dataID )
    print(results.authors)
    #authorID = id
    #unfavorited_authors = Author.unfavorited_authors( authorID )
    #print(unfavorited_authors)
    return render_template( "books_favorite.html", books = results)#, unfavorited_authors = unfavorited_authors )