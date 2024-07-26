from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Book, Author

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route('/books', methods=['GET'])
    def get_books():
        books = Book.query.all()
        return jsonify([book.to_dict() for book in books])

    @app.route('/books', methods=['POST'])
    def add_book():
        data = request.get_json()
        new_book = Book(title=data['title'], author_id=data['author_id'])
        db.session.add(new_book)
        db.session.commit()
        return jsonify(new_book.to_dict()), 201

    @app.route('/authors', methods=['GET'])
    def get_authors():
        authors = Author.query.all()
        return jsonify([author.to_dict() for author in authors])

    @app.route('/authors', methods=['POST'])
    def add_author():
        data = request.get_json()
        new_author = Author(name=data['name'])
        db.session.add(new_author)
        db.session.commit()
        return jsonify(new_author.to_dict()), 201

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
