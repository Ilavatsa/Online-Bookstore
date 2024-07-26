from app import app
from models import db
from models.book import Book
from models.author import Author

def seed_data():
    # Create sample authors
    author1 = Author(name='George Orwell')
    author2 = Author(name='J.K. Rowling')

    # Add authors to the session
    db.session.add(author1)
    db.session.add(author2)
    db.session.commit()

    # Create sample books
    book1 = Book(title='1984', author_id=author1.id)
    book2 = Book(title='Animal Farm', author_id=author1.id)
    book3 = Book(title='Harry Potter and the Sorcerer\'s Stone', author_id=author2.id)
    book4 = Book(title='Harry Potter and the Chamber of Secrets', author_id=author2.id)

    # Add books to the session
    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)
    db.session.add(book4)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
        seed_data()  # Seed the database
