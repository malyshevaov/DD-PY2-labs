import doctest

class SubjectForRhythmicGymnastic:
    """
        Создание и подготовка к работе  базового класса "Предмет для художественной гимнастики"
    :param brand: производитель предмета для художественной гимнастики
    :param model: вид предмета для художественной гимнастики
    :param weiht: вес предмета для художественной гимнастики
    """
    def __init__(self, brand: str, model: str, weight: int):
        self.brand = brand
        self.model = model
        self.weight = weight

    def __str__(self)->str:
        return f"Производитель {self.brand}. Вид предмета {self.model}. Вес предмета {self.weight}"

    def __repr__(self) ->str:
        return f"{self.__class__.__name__} brand={self.brand!r}, model={self.model!r}, weight={self.weight}"

    def weight_suitable(self, weight: int):
        """
        Функция, которая проверяет, что вес предмета для художественной гимнастики типа int
        :param height: Вес предмета
        :raise ValueError: Если вес указан тип не int, то вызываем ошибку
        Примеры:
        >>> subject = SubjectForRhythmicGymnastic("Pastorelli","скакалка", 200)
        >>> subject.weight_suitable(200)
        """
        if not isinstance(weight, int):
            raise TypeError("Вес предмета для художественной гимнастики  должен быть типа int")

    def weight_total(self, weight:int):
        """
        Функция weight_total проверяет, не превышает ли вес предмета для художественной гимнастики 500 гр
        :param height: Вес предмета
        :raise ValueError: Если вес больше предельно-допустимого, то вызываем ошибку ValueError
        """
        if self.weight >= 500:
            raise ValueError("Вес предмета не может быть более 500 граммов")

class Ball(SubjectForRhythmicGymnastic):
    """
    Создание дочернего класса "Мяч".
    :param brand: производитель предмета для художественной гимнастики
    :param model: вид предмета для художественной гимнастики
    :param weight: вес предмета для художественной гимнастики
    :param diameter_of_ball: диаметр мяча
     """
    def __init__(self, brand: str, model: str, weight: int, diameter_of_ball: int):
        """
        Расширяем конструктор базового класса, так как у мяча есть дополнительный атрибут - диаметр (diameter_of_ball).
        """
        super().__init__(brand, model, weight)
        self.diameter_of_ball = diameter_of_ball

    def __str__(self)->str:
        """
        Перегружаем  str, так как у мяча есть дополнительный атрибут - диаметр, и это надо отобразить в str
        """
        return f"Производитель {self.brand}. Вид предмета {self.model}. Вес предмета {self.weight}. Диаметр мяча {self.diameter_of_ball}"

    def __repr__(self) -> str:
        """
        Перегружаем  repr так как у мяча есть дополнительный атрибут - диаметр, и это надо отобразить в repr
        """
        return f"{self.__class__.__name__} brand={self.brand!r}, model={self.model!r}, weight={self.weight}, diameter_of_ball={self.diameter_of_ball}"

    def weight_total(self, weight: int):
        """
        Перегружаем функцию weight_total, так как у мяча вес не может быть больше 350 гр
        """
        if self.weight >= 350:
            raise ValueError ("Вес мяча не может быть более 350 граммов")

    @property
    def diameter_of_ball(self):
        """Возвращает диаметр мяча"""
        return self._diameter_of_ball

    @diameter_of_ball.setter
    def diameter_of_ball (self, new_diameter_of_ball: int) -> None:
        """Устанавливает диаметр мяча."""
        if not isinstance(new_diameter_of_ball, int):
            raise TypeError ("Диаметр мяча должн быть типа int")
        if not new_diameter_of_ball >= 1:
            raise ValueError ("Диаметр мяча должн быть положительным числом")
        self._diameter_of_ball = new_diameter_of_ball


class Clubs(SubjectForRhythmicGymnastic):
    """
    Дочерний класс "Булавы"
    :param brand: производитель предмета для художественной гимнастики
    :param model: вид предмета для художественной гимнастики
    :param weight: вес предмета для художественной гимнастики
    :param lenght: длина булав
    """

    def __init__(self, brand: str, model: str, weight: int, length_of_clubs: int):
        """Расширяем  конструктор базового класса, так как у булав есть дополнительный атрибут - длина (lenght_of_clubs)
        """
        super().__init__(brand, model, weight)
        self.length_of_clubs = length_of_clubs

    def __str__(self)->str:
        """
        Перегружаем  str, так как у булав есть дополнительный атрибут lenght_of_clubs, и его надо прописать в str
        """
        return f"Производитель {self.brand}. Вид предмета {self.model}. Вес предмета {self.weight}. Длина булав {self.length_of_clubs}"

    def __repr__(self) -> str:
        """
        Перегружаем  repr, так как у булав есть дополнительный атрибут lenght_of_clubs, и его надо прописать в repr
        """
        return f"{self.__class__.__name__} brand={self.brand!r}, model={self.model!r}, weight={self.weight}, length_of_clubs={self.length_of_clubs}"

    def weight_total(self, weight: int):
        """
        Перегружаем  weight_total так как вес булавы не должен быть более 150 гр.
        """
        if self.weight >= 150:
            raise ValueError("Вес одной булавы не может быть более 150 граммов")

    def suitable_age(self):
        """
        Метод suitable_age определяет, на какой возраст расчитаны данные булавы
        30-36 см -  от 5 до 7 лет
        37-41 см - от 8 до 11 лет
        42-45 см - от 11 до 16 лет
        46 см и более -  гимнастки старше 16 лет
        """

        if 30 <= self.length_of_clubs <= 36:
            print("Булавы для гимнасток от 5 до 7 лет ")
        if 37 <= self.length_of_clubs <= 41:
            print("Булавы для гимнасток от 8 до 11 лет ")
        if 42 <= self.length_of_clubs <= 45:
            print("Булавы для гимнасток от 11 до 16 лет ")
        if self.length_of_clubs >= 46:
            print("Булавы для гимнасток от 16 лет и старше ")


print(Ball("Pastorelli","мяч GLITTER HIGH VISION", 300, 18))
print(Clubs("Chacott","булавы FIG", 150, 41))
print(repr(Ball("Pastorelli","GLITTER HIGH VISION", 300, 18)))
print(repr(Clubs("Chacott","булавы FIG", 150, 41)))
clubs_ = Clubs("Chacott","булавы FIG", 150, 41)
clubs_.suitable_age()

ball = Ball("Pastorelli","мяч GLITTER HIGH VISION", 300, 18)
print(ball.diameter_of_ball)  # вызываем как атрибут, но срабатывает метод
ball.diameter_of_ball = 20  # присваиваем значение атрибуту, но срабатывает метод
print(ball.diameter_of_ball)

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
