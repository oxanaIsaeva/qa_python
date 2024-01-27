import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_genre(self, collector):

        collector.add_new_book('Ревизор')
        collector.set_book_genre('Ревизор', 'Комедии')

        assert collector.get_book_genre('Ревизор') == 'Комедии'

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Ревизор', 'Комедии'],
            ['Дракула', 'Ужасы'],
            ['Трудно быть богом', 'Фантастика'],
            ['Шерлок Холмс', 'Детективы'],
            ['Винни-Пух', 'Мультфильмы']
        ]
    )

    def test_get_book_genre(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Ревизор', 'Комедии'],
            ['Дракула', 'Ужасы'],
            ['Трудно быть богом', 'Фантастика'],
            ['Шерлок Холмс', 'Детективы'],
            ['Винни-Пух', 'Мультфильмы']
        ]
    )
    def test_get_books_with_specific_genre(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert len(collector.get_books_with_specific_genre(genre)) == 1

    def test_get_books_genre(self, collector_with_5_books):

        assert collector_with_5_books.get_books_genre() == {'Ревизор': 'Комедии', 'Чиполлино': 'Мультфильмы', 'Шерлок Холмс': 'Детективы', 'Дракула': 'Ужасы', 'Винни-Пух': 'Мультфильмы'}

    def test_get_books_for_children(self, collector_with_5_books):

        assert collector_with_5_books.get_books_for_children() == ['Ревизор', 'Чиполлино', 'Винни-Пух']

    def test_add_book_in_favorites(self, collector_with_5_books):
        collector_with_5_books.add_book_in_favorites('Ревизор')
        collector_with_5_books.add_book_in_favorites('Винни-Пух')

        assert collector_with_5_books.get_list_of_favorites_books() == ['Ревизор', 'Винни-Пух']

    def test_delete_book_from_favorites(self, collector_with_5_books):
        collector_with_5_books.add_book_in_favorites('Ревизор')
        collector_with_5_books.add_book_in_favorites('Винни-Пух')
        collector_with_5_books.delete_book_from_favorites('Винни-Пух')

        assert collector_with_5_books.get_list_of_favorites_books() == ['Ревизор']

    def test_add_new_book_new_book_wo_genre(self, collector):
        collector.add_book_in_favorites('Горе от ума')

        assert collector.get_book_genre('Горе от ума') == None

    def test_get_books_for_children_doesnt_have_books_with_age_rating(self, collector_with_5_books):

        assert 'Дракула' not in collector_with_5_books.get_books_for_children()


    def test_set_book_genre_negative(self, collector):

        collector.add_new_book('Ревизор')
        collector.set_book_genre('Ревизор', 'Новогодние')

        assert collector.get_book_genre('Ревизор') == ''

    def test_add_new_book_twice(self, collector):
        collector.add_new_book('Ревизор')
        collector.add_new_book('Горе от ума')
        collector.add_new_book('Ревизор')

        assert collector.get_books_genre() == {'Ревизор': '', 'Горе от ума': ''}




