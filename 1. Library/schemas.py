from sqlalchemy import Column, Date, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from CRUD import CRUD

Base = declarative_base()

class Book(Base, CRUD):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    publication_year = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'),nullable=False)
    genre_id = Column(Integer, ForeignKey('genres.id') ,nullable=False)

    author = relationship("Author", back_populates="books")
    genre = relationship("Genre", back_populates="books")

    def __repr__(self):
        return f"<Book(title='{self.title}', publication_year='{self.publication_year}')>"
    
class Author(Base, CRUD):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    birth_date = Column(Date(), nullable=False)
    books = relationship("Book", back_populates='author')

    def __repr__(self):
        return f"<Author(name='{self.name}', birth_date='{self.birth_date}')"
    
class Genre(Base, CRUD):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    books = relationship("Book", back_populates='genre')

    def __repr__(self):
        return f"<Genre(name='{self.name}')"