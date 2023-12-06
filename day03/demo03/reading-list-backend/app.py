from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_cors import CORS 
from config import DATABASE_CONNECTION_URI

app = Flask(__name__)
CORS(app) 

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Book(db.Model):

    __tablename__ = 'books_info'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
    rating = db.Column(db.Integer)

    def __init__(self, title, author, rating):
        self.title = title 
        self.author = author
        self.rating = rating


@app.route('/')
def index():
    return jsonify({'msg': "Hello!!!"})

@app.route('/api/add_book', methods=['POST'])
def add_book():

    book_data = request.get_json()
    new_book = Book(title=book_data['title'], author=book_data['author'], rating=book_data['rating'])

    db.session.add(new_book)
    db.session.commit()

    return jsonify({"msg": "Done"})

@app.route('/api/books', methods=['GET'])
def books():

        book_list = Book.query.all()
        books = []

        for book in book_list:
            books.append({'title': book.title, 'author': book.author, 'rating': book.rating})

        return jsonify({'books' : books})

# @app.route('/api/add_book', methods=['POST', 'OPTIONS'])
# def add_book():

#     if request.method == "OPTIONS": # CORS preflight
#         return _build_cors_preflight_response()

#     elif request.method == "POST": # The actual request following the preflight
#         book_data = request.get_json()
#         new_book = Book(title=book_data['title'], author=book_data['author'], rating=book_data['rating'])

#         db.session.add(new_book)
#         db.session.commit()

#         response = jsonify({"msg": "Done"})
#         return _corsify_actual_response(response)

#     else:
#         raise RuntimeError("Weird - don't know how to handle method {}".format(request.method))

# @app.route('/api/books', methods=['GET', 'OPTIONS'])
# def books():

#     if request.method == "OPTIONS": # CORS preflight
#         return _build_cors_preflight_response()
#     elif request.method == "GET":

#         book_list = Book.query.all()
#         books = []

#         for book in book_list:
#             books.append({'title': book.title, 'author': book.author, 'rating': book.rating})

#         response = jsonify({'books' : books})
#         return _corsify_actual_response(response)

# def _build_cors_preflight_response():
#     response = make_response()
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     response.headers.add('Access-Control-Allow-Headers', "*")
#     response.headers.add('Access-Control-Allow-Methods', "*")
#     return response

# def _corsify_actual_response(response):
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
