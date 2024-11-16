import pytest
from test_books_collector.BooksCollectorFile import BooksCollector


@pytest.fixture
def books_collector():
    return BooksCollector()

sample_books = [
    ("Чиполлино", "Мультфильмы"),
    ("Назад в будущее", "Фантастика"),
    ("Пила", "Ужасы"),
    ("Шерлок Холмс", "Детективы"),
    ("Укрощение строптивого", "Комедии"),
]