from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from schemas import Author, Genre, Book
from prepare_program import deleteDB



authors_data = [
    {"name": "Leo Tolstoy", "birth_date": "1828-09-09"},
    {"name": "Fyodor Dostoevsky", "birth_date": "1821-11-11"},
    {"name": "Jane Austen", "birth_date": "1775-12-16"},
    {"name": "Mark Twain", "birth_date": "1835-11-30"},
    {"name": "George Orwell", "birth_date": "1903-06-25"},
]
genres_data = [
    {"name": "Novel"},
    {"name": "Science Fiction"},
    {"name": "Historical"},
    {"name": "Satire"},
    {"name": "Romance"},
]
books_data = [
    {"title": "War and Peace", "publication_year": 1869, "author_id": 1, "genre_id": 3},
    {"title": "Anna Karenina", "publication_year": 1877, "author_id": 1, "genre_id": 5},
    {"title": "Crime and Punishment", "publication_year": 1866, "author_id": 2, "genre_id": 1},
    {"title": "Pride and Prejudice", "publication_year": 1813, "author_id": 5, "genre_id": 5},
    {"title": "Adventures of Huckleberry Finn", "publication_year": 1884, "author_id": 4, "genre_id": 4},
    {"title": "1984", "publication_year": 1949, "author_id": 5, "genre_id": 2},
    {"title": "Animal Farm", "publication_year": 1945, "author_id": 5, "genre_id": 4},
]
if __name__ == "__main__":
    engine = create_engine("sqlite:///library.db")

    @event.listens_for(engine, "connect")
    def enable_foreign_keys(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

    Session = sessionmaker(bind=engine)
    session = Session()
    deleteDB()

    for author_data in authors_data:
        Author.create(session, **author_data)

    for genre_data in genres_data:
        Genre.create(session, **genre_data)

    for book_data in books_data:
        try:
            Book.create(session, **book_data)
        except Exception as e:
            print(e)
            session.rollback()
    
    print(Author.get(session, id=1))
    
    books = Book.get_all(session)
    for book in books:
        print(book)
    
    print(Genre.update(session, pk=1, name='Test genre'))
    Book.delete(session, pk=1)
