from app import app, db
from model import book
from flask import render_template, request, url_for

@app.route('/books')
def books():
    books = Book.query.all()
    returnrender_template('books.html', books = books)