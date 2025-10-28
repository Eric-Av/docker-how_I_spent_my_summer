from flask import Flask, jsonify, render_template, request

import os

app = Flask(__name__)

#БД ДАДА
books = [
    {"id": 1, "title": "Первый месяц я ещё училась"},
    {"id": 2, "title": "Второй месяц я устроилась на работу"},
    {"id": 3, "title": "После работы немного занималась и обучалась новым языкам"},
    {"id": 4, "title": "Мои друзья звали меня гулять"},
    {"id": 5, "title": "Третий месяц я занималась сспортом"},
]

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/books', methods=["GET"])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=["GET"])
def get_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    return jsonify({"books":book}) 



if __name__ == "__main__":
    app.run()