class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__} name={self.name!r}, author={self.author!r}"

class PaperBook(Book):
    """ Класс бумажной книги. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} name={self.name!r}, author={self.author!r}, pages={self.pages}"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError
        if not pages >= 1:
            raise ValueError
        self._pages = pages

class AudioBook(Book):
    """ Класс  аудиокниги. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} name={self.name!r}, author={self.author!r}, duration={self.duration}"

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError
        if not duration >= 0.00:
            raise ValueError
        self._duration = duration

print(PaperBook("Паруса Эспады", "В.Крапивин", 225))
print(AudioBook("Паруса Эспады", "В.Крапивин", 100.00))
print(repr(PaperBook("Паруса Эспады", "В.Крапивин", 225)))
print(repr(AudioBook("Паруса Эспады", "В.Крапивин", 100.00)))
