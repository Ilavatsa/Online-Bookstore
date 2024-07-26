Online Bookstore
A simple online bookstore application built with Flask, SQLAlchemy, and Flask-Migrate. This project provides RESTful APIs to manage books and authors.

Table of Contents
Features
Installation
Usage
Configuration
Database Migration
API Endpoints
Contributing
License
Features
Books Management: Add, list books.
Authors Management: Add a list authors
Installation
Prerequisites
Python 3.8+
Pipenv (for managing Python packages)
Clone the Repository
bash
Copy code
git clone https://github.com/Ilavatsa/online-bookstore.git
cd online-bookstore
Install Dependencies
bash
Copy code
pipenv install
Activate the Virtual Environment
bash
Copy code
pipenv shell
Usage
Running the Application
Start the Flask application with:

bash
Copy code
flask run
Initialize the Database
Initialize the migration directory with:

bash
Copy code
flask db init
Create an initial migration with:

bash
Copy code
flask db migrate -m "Initial migration"
Apply the migration with:

bash
Copy code
flask db upgrade
Configuration
Configure the application by setting up config.py. The default configuration uses SQLite.

config.py:

python
Copy code
class Config:
SQLALCHEMY_DATABASE_URI = 'sqlite:///yourdatabase.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
Update SQLALCHEMY_DATABASE_URI with the desired database URI.

API Endpoints
Books
GET /books - List all books
POST /books - Add a new book
Authors
GET /authors - List all authors
POST /authors - Add a new author
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

Fork the repository
Create a feature branch (git checkout -b feature/YourFeature)
Commit your changes (git commit -am 'Add new feature')
Push to the branch (git push origin feature/YourFeature)
Create a new Pull Request
License
This project is licensed under the MIT License. See the LICENSE file for details.
