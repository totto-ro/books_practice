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