class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages):
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages


    def __str__(self):
        return f"Бумажная книга {self.name} ({self.pages} страниц). Автор {self.author}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration):
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = new_duration

    def __str__(self):
        return f"Аудио книга {self.name} ({self._duration} продолжительность). Автор {self.author}"


if __name__ == '__main__':
    pb = PaperBook('Python', 'Lutz', 123)
    print('initial', pb)
    try:
        pb.author = 'Somebody'
    except:
        print('Setting author for PaperBook failed')
    pb._author = 'Mark Lutz'  # still able to change protected attribute
    print('changed', pb)

    ab = AudioBook('Python', 'Lutz', 123.0)
    print('initial', ab)
    try:
        pb.name = 'Something'
    except:
        print('Setting name for AudioBook failed')
    print('changed', ab)
