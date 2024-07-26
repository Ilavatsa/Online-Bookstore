import React from 'react';
import BookDetail from './BookDetail';

const BookList = ({ books }) => {
  return (
    <div>
      {books.map(book => (
        <BookDetail key={book.id} book={book} />
      ))}
    </div>
  );
};

export default BookList;
