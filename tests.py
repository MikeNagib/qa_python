from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2, 'Проверка добавления книг'


    def test_add_new_book_dublicat_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_rating()) == 1, 'Проверяем что нельзя добавить одну и ту же книгу дважды'


    def test_set_book_rating_rating_none_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 9)
        assert collector.get_book_rating('Что делать, если ваш кот хочет вас убить') is None, 'Нельзя выставить рейтинг книге, которой нет в списке'


    def test_set_book_rating_rating_min_1(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', -2)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1, 'Нельзя выставить рейтинг меньше'


    def test_set_book_rating_rating_max_10(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 12)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1, 'Нельзя выставить рейтинг больше 10'


    def test_set_book_rating_none_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 10)
        assert collector.get_book_rating('Что делать, если ваш кот хочет вас убить') is None, 'У не добавленной книги нет рейтинга'


    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби'], 'Добавление книги в избранное'


    def test_add_book_in_favorites_no_books_rating(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.get_list_of_favorites_books() == [] , 'Нельзя добавить книгу в избранное, если её нет в словаре books_rating'

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Что делать, если ваш кот хочет вас убить'], 'Проверка удаления книги из избранного'


    def test_get_books_with_specific_rating_list(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_rating('Гордость и предубеждение и зомби', 10)
        assert collector.get_books_with_specific_rating(10) == ['Гордость и предубеждение и зомби'], 'Проверка списка книг с определенным рейтингом'

