import datetime

class Book:
    """
    Базовый класс для представления книги.

    Атрибуты:
        title (str): Название книги
        author (str): Автор книги
        year (int): Год издания
        _price (float): Цена книги (защищенный атрибут)

    Методы:
        calculate_discount(days_owned: int) -> float: Расчет скидки на основе времени владения
        update_price(new_price: float) -> None: Обновление цены книги
    """

    def __init__(self,
                 title: str,
                 author: str,
                 year: int,
                 price: float = 0.0):
        """Инициализирует объект книги."""
        self.title = title
        self.author = author
        self.year = year
        self._price = price

    def __str__(self) -> str:
        """Возвращает читаемое строковое представление книги."""
        return f"{self.title} ({self.year}) - {self.author}"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление книги."""
        return f"{self.__class__.__name__}(title='{self.title}', author='{self.author}', year={self.year}, price={self._price})"

    def calculate_discount(self, days_owned: int) -> float:
        """Рассчитывает скидку на основе количества дней владения."""
        if days_owned < 30:
            return 0.0
        elif days_owned < 90:
            return 0.1
        else:
            return 0.2

    def _update_internal_price(self, new_price: float) -> None:
        """Обновляет внутреннюю цену книги (защищенный метод)."""
        # Инкапсуляция для контроля над обновлением цены
        if new_price >= 0:
            self._price = new_price

    def update_price(self, new_price: float) -> None:
        """Обновляет цену книги через приватный метод."""
        self._update_internal_price(new_price)


class FictionBook(Book):
    """
    Класс для художественных книг.

    Дополнительные атрибуты:
        genre (str): Жанр произведения
        rating (float): Рейтинг книги

    Перегруженные методы:
        calculate_discount(days_owned: int) -> float: Увеличенная скидка для художественной литературы
    """

    def __init__(self, title: str, author: str, year: int,
                 price: float, genre: str, rating: float):
        """Инициализирует объект художественной книги."""
        super().__init__(title, author, year, price)
        self.genre = genre
        self.rating = rating

    def __str__(self) -> str:
        """Возвращает расширенное строковое представление художественной книги."""
        base_str = super().__str__()
        return f"{base_str} [{self.genre}] - рейтинг: {self.rating}/10"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление художественной книги."""
        return (f"FictionBook(title='{self.title}', author='{self.author}', "
                f"year={self.year}, price={self._price}, genre='{self.genre}', "
                f"rating={self.rating})")

    def calculate_discount(self, days_owned: int) -> float:
        """Перегружает базовый метод расчета скидки для художественных книг."""
        # Художественная литература имеет более высокие скидки
        base_discount = super().calculate_discount(days_owned)
        return base_discount + 0.05

    def _validate_rating(self, rating: float) -> bool:
        """Проверяет корректность рейтинга (приватный метод)."""
        return 0 <= rating <= 10

    def update_rating(self, new_rating: float) -> None:
        """Обновляет рейтинг книги с валидацией."""
        if self._validate_rating(new_rating):
            self.rating = new_rating


class TechnicalBook(Book):
    """
    Класс для технических книг.

    Дополнительные атрибуты:
        edition (int): Номер издания
        _last_update (datetime): Дата последнего обновления (защищенный атрибут)

    Перегруженные методы:
        update_price(new_price: float) -> None: Особая логика обновления цены для технических книг
    """

    def __init__(self, title: str, author: str, year: int,
                 price: float, edition: int):
        """Инициализирует объект технической книги."""
        super().__init__(title, author, year, price)
        self.edition = edition
        self._last_update = datetime.datetime.now()

    def __str__(self) -> str:
        """Возвращает расширенное строковое представление технической книги."""
        base_str = super().__str__()
        return f"{base_str} (издание {self.edition})"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление технической книги."""
        return (f"TechnicalBook(title='{self.title}', author='{self.author}', "
                f"year={self.year}, price={self._price}, edition={self.edition})")

    def update_price(self, new_price: float) -> None:
        """Перегружает базовый метод обновления цены для технических книг."""
        # Технические книги имеют особую логику обновления цены
        if new_price > self._price * 1.5:
            raise ValueError("Цена не может быть больше чем в 1.5 раза выше текущей")
        super().update_price(new_price)
        self._last_update = datetime.datetime.now()


if __name__ == "__main__":
    # Создаем экземпляры разных типов книг
    book = Book("Война и мир", "Л.Н. Толстой", 1869, 1000.0)
    fiction_book = FictionBook("1984", "Дж. Оруэлл", 1949, 800.0, "Антиутопия", 8.5)
    technical_book = TechnicalBook("Python для профессионалов", "Иванов И.И.",
                                   2023, 2000.0, 3)

    # Демонстрация работы методов
    print("\nДемонстрация строковых представлений:")
    print(book)
    print(fiction_book)
    print(technical_book)

    print("\nДемонстрация расчета скидок:")
    days_owned = 60
    print(f"Скидка на обычную книгу ({days_owned} дней): {book.calculate_discount(days_owned) * 100}%")
    print(f"Скидка на художественную книгу ({days_owned} дней): {fiction_book.calculate_discount(days_owned) * 100}%")

    print("\nДемонстрация обновления цены технической книги:")
    try:
        technical_book.update_price(2500.0)
        print(f"Новая цена технической книги: {technical_book._price}")
    except ValueError as e:
        print(f"Ошибка при обновлении цены: {e}")
