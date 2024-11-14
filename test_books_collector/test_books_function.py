import pytest
from BooksCollectorFile import BooksCollector


@pytest.fixture
def books_collector():
    return BooksCollector()


sample_books = [["Чиполлино", "Мультфильмы"], ["Назад в будущее", "Фантастика"], ["Пила", "Ужасы"],
                ["Шерлок Холмс", "Детективы"], ["Укрощение строптивого", "Комедии"]]


class TestClassBooksCollector:

    def test_genre_return_correct_list(self, books_collector):
        assert books_collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_genre_age_rating_return_correct_list(self, books_collector):
        assert books_collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_books_genre_is_dict(self, books_collector):
        assert isinstance(books_collector.books_genre, dict)

    def test_favorites_is_list(self, books_collector):
        assert isinstance(books_collector.favorites, list)

    def test_add_new_book_successfully_adds_book(self, books_collector, name="Чиполлино"):
        books_collector.add_new_book(name)
        assert name in books_collector.books_genre

    def test_add_new_book_len_symbols_more_than_40(self, books_collector,name="Алиса в стране чудес Алиса в стране чудеc"):
        books_collector.add_new_book(name)
        assert name not in books_collector.books_genre

    def test_add_new_book_re_adding_a_book(self, books_collector, name="Чиполлино"):
        books_collector.add_new_book(name)
        books_collector.add_new_book(name)
        assert len(books_collector.books_genre) == 1

    @pytest.mark.parametrize("name,genre", sample_books)
    def test_set_book_genre_return_correct_genre(self, books_collector, name, genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.books_genre[name] == genre

    @pytest.mark.parametrize("name,genre", sample_books)
    def test_get_book_genre_return_book_genre(self, books_collector, name, genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.books_genre.get(name) == genre

    @pytest.mark.parametrize("name,genre", sample_books)
    def test_get_books_with_specific_genre_return_specific_genre_list(self, books_collector, name, genre):
        list_for_check = []
        list_for_check.append(name)
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.get_books_with_specific_genre(genre) == list_for_check and len(
            books_collector.get_books_with_specific_genre(genre)) == 1

    @pytest.mark.parametrize("name,genre", sample_books)
    def test_get_books_for_children_return_books_for_children_list(self, books_collector, name, genre):
        if genre not in books_collector.genre_age_rating:
            list_for_check = []
            list_for_check.append(name)
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, genre)
            assert books_collector.get_books_for_children() == list_for_check

    @pytest.mark.parametrize("name,genre", sample_books)
    def test_get_books_for_children_genre_age_rating_not_set_in_get_books_for_children(self, books_collector, name, genre):
        if genre in books_collector.genre_age_rating:
            list_for_check = []
            list_for_check.append(name)
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, genre)
            assert books_collector.get_books_for_children() != list_for_check

    @pytest.mark.parametrize("name,genre",sample_books)
    def test_add_book_in_favorites_added_books_to_favorite(self,books_collector, name, genre):
        list_for_check = []
        list_for_check.append(name)
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        books_collector.add_book_in_favorites(name)
        assert books_collector.favorites == list_for_check

    @pytest.mark.parametrize("name,genre",sample_books)
    def test_delete_book_from_favorites_remove_books(self,books_collector, name, genre):
        list_for_check = []
        list_for_check.append(name)
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        books_collector.add_book_in_favorites(name)
        books_collector.delete_book_from_favorites(name)
        assert list_for_check not in books_collector.favorites

    @pytest.mark.parametrize("name,genre",sample_books)
    def test_get_list_of_favorites_books_return_correct_list(self,books_collector, name, genre):
        list_for_check = ["Властелин Колец"]
        list_for_check.append(name)
        books_collector.add_new_book(name="Властелин Колец")
        books_collector.set_book_genre(name="Властелин Колец", genre="Фантастика")
        books_collector.add_book_in_favorites(name="Властелин Колец")
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        books_collector.add_book_in_favorites(name)
        assert books_collector.favorites == list_for_check
