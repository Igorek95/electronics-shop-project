from src.item import Item


class MixinLang:
    """
    Класс-миксин для хранения и изменения раскладки клавиатуры.
    """

    def __init__(self, *args, default_language="EN", **kwargs):
        super().__init__(*args, **kwargs)
        self.language = default_language

    def change_lang(self):
        """
        Изменяет язык клавиатуры.
        """
        if self.language == "EN":
            self.language = "RU"
        else:
            self.language = "EN"
        return self


class Keyboard(MixinLang, Item):
    """
    Класс для представления клавиатуры в магазине.
    """

    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        super().__init__(name, price, quantity)
        self.__language = language

    def __str__(self):
        return self.name

    @property
    def language(self):
        """
        Возвращает текущую раскладку клавиатуры.
        """
        return self.__language

    @language.setter
    def language(self, value):
        """
        Устанавливает новую раскладку клавиатуры.

        :param value: Новая раскладка клавиатуры.
        """
        if value in ["EN", "RU"]:
            self.__language = value
        else:
            raise ValueError("Доступны только языки раскладки 'EN' и 'RU'")
