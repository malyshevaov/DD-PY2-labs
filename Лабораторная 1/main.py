import doctest

class KeyBoard:
    def __init__(self, number_of_keys: int, key_height: float):
        """
        Создание и подготовка к работе объекта "Электронное пианино"
        :param number_of_keys: количество клавиш
        :param key_height: высота клавиши
        Примеры:
        >>> keyboard = KeyBoard(88, 1.2)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_keys, int):
            raise TypeError("Количество клавиш должно быть типа int")
        if number_of_keys <= 0:
            raise ValueError("Количество клавиш должно быть положительным числом")
        self.number_of_keys = number_of_keys

        if not isinstance(key_height,  float):
            raise TypeError("Высота клавиш должна быть float")
        if key_height < 0.0:
            raise ValueError("Высота клавиши не может быть отрицательным числом")
        self.key_height = key_height

    def is_piano_full_size(self) -> bool:
        """
        Функция которая проверяет является ли клавиатура пианино полноразмерной, т.е.  имеет 88 белых клавиш
        :return: Является ли клавиатура полноразмерной
        Примеры:
        >>> keyboard = KeyBoard(88, 1.5)
        >>> keyboard.is_piano_full_size()
        """
        ...

    def press_the_key(self, height: float) -> None:
        """
        Высота клавиатуры при нажатой клавише
        :param height: Высота клавиатуры при нажатой клавише
        :raise ValueError: Если высота клавиатуры при нажатой клавише превышает выоту клавиши, то вызываем ошибку
        Примеры:
        >>> keyboard = KeyBoard(88, 1.5)
        >>> keyboard.press_the_key(1.5)
        """

        if not isinstance(height, float):
            raise TypeError("Высота клавиатуры при нажатой клавише должна быть типа float")
        if height > 1.5:
            raise ValueError("Высота клавиатуры при нажатой клавише должна меньше высоты клавиши")
        ...

class Sound:
    def __init__(self, number_of_timbre: int, number_of_polyphony_sound: int):
        """
        Создание и подготовка к работе объекта "Электронное пианино"
        :param number_of_timbre: Количество тембров
        :param number_of_polyphony_sound: Полифония, количество одновременно звучащих нот
        Примеры:
        >>> sound = Sound(700, 64)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_timbre, int):
            raise TypeError("Количество тембров должно быть типа int")
        if number_of_timbre <= 0:
            raise ValueError("Количество тембров должно быть положительным числом")
        self.number_of_timbre = number_of_timbre

        if not isinstance(number_of_polyphony_sound, int):
            raise TypeError("Количество одновременно звучащих нотдолжно быть int")
        if number_of_polyphony_sound < 0:
            raise ValueError("Количество одновременно звучащих нот не может быть отрицательным числом")
        self.number_of_polyphony_sound = number_of_polyphony_sound

    def is_polyphony_high(self) -> bool:
        """
        Функция которая проверяет является ли полифония высокого уровня звучания ( высокий уровень начинается с 256 нот)при количестве от 256
        :return: Полифония высокого уровня
        Примеры:
        >>> sound = Sound(700,256)
        >>> sound.is_polyphony_high()
        """
        ...

    def new_timbres(self, downloaded_timbres: int) -> None:
        """
        Вазможность закачать новые тембры
        :param downloaded_timbres: Количество закачанных новых тембров
        :raise ValueError: Если количество закачанных новых тембров болле 100, то вызываем ошибку
        Примеры:
        >>> sound = Sound(700, 256)
        >>> sound.new_timbres(64)
        """
        if not isinstance(downloaded_timbres, int):
            raise TypeError("Количество закачанных новых тембров должно быть типа int")
        if downloaded_timbres > 100:
            raise ValueError("Новые тембры будут занимать слишком большой объем ")
        ...

class Appearance:
    def __init__(self, stand_material: str, number_of_pedals: int):
        """
        Создание и подготовка к работе объекта "Электронное пианино"
        :param stand_material: Материал, из которого изготовлена стойка
        :param number_of_pedals: Количество педалей
        Примеры:
        >>> appearance = Appearance("metal", 2)  # инициализация экземпляра класса
        """
        if not isinstance(stand_material, str):
            raise TypeError("Материал стойки должен быть типа str")
        self.stand_material = stand_material

        if not isinstance(number_of_pedals, int):
            raise TypeError("Количество педалей должно быть типа int")
        if number_of_pedals < 0:
            raise ValueError("Количество педалей не может быть отрицательным числом")
        self.number_of_pedals = number_of_pedals

    def is_stend_wooden(self) -> bool:
        """
        Функция которая проверяет является ли стoйка электронного пианино деревянной
        :return: Пианино с деревянной стойкой
        Примеры:
        >>> appearance = Appearance("wood", 2)
        >>> appearance.is_stend_wooden()
        """
        ...

    def complect_of_pedals(self, units_of_pedals: int) -> None:
        """
        Возможность добавить педали
        :param units_of_pedals: Количество педалей, которое планируется добавить
        :raise ValueError: Если общее количество педалей превысит 3, то вызываем ошибку
        :return: Количество паедалей, которое  можно установить дополнительно
        Примеры:
        >>> appearance = Appearance("wood", 2)
        >>> appearance.complect_of_pedals(1)
        """
        if not isinstance(units_of_pedals, int):
            raise TypeError(" Количество педалей, которое планируется добавить должно быть типа int")
        if units_of_pedals < 0:
            raise ValueError("Количество педалей, которое планируется добавить должно быть положительным числом")
        ...
if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
