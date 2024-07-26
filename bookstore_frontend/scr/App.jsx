import React, { useState, useEffect } from 'react';
import axios from 'axios';
import BookList from './components/BookList';
import BookForm from './components/BookForm';

const App = () => {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/books')
      .then(response => setBooks(response.data))
      .catch(error => console.error(error));
  }, []);

  const addBook = (book) => {
    setBooks([...books, book]);
  };

  return (
    <div className="container">
      <header className="header">
        <h1>Online Bookstore</h1>
      </header>
      <BookForm addBook={addBook} />
      <BookList books={books} />
    </div>
  );
};

export default App;
