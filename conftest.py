import pytest
from main import BooksCollector
@pytest.fixture
def collector():
    collector = BooksCollector()

    return collector

@pytest.fixture
def collector_with_5_books():
    collector_with_5_books = BooksCollector()
    collector_with_5_books.add_new_book('Ревизор')
    collector_with_5_books.add_new_book('Чиполлино')
    collector_with_5_books.add_new_book('Шерлок Холмс')
    collector_with_5_books.add_new_book('Дракула')
    collector_with_5_books.add_new_book('Винни-Пух')
    collector_with_5_books.set_book_genre('Ревизор', 'Комедии')
    collector_with_5_books.set_book_genre('Чиполлино', 'Мультфильмы')
    collector_with_5_books.set_book_genre('Шерлок Холмс', 'Детективы')
    collector_with_5_books.set_book_genre('Дракула', 'Ужасы')
    collector_with_5_books.set_book_genre('Винни-Пух', 'Мультфильмы')

    return collector_with_5_books