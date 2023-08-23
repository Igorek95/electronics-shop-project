import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1.0
    """Коэффициент для расчета цены с учетом скидки."""

    all = []
    """Список всех созданных экземпляров товаров."""

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса Item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """Возвращает наименование товара."""
        return self.__name

    @name.setter
    def name(self, value):
        """
        Устанавливает наименование товара.

        Если длина наименования превышает 10 символов, обрезает его до 10 символов.

        :param value: Новое наименование товара.
        """
        if len(value) > 10:
            self.__name = value[:10]
        else:
            self.__name = value

    @staticmethod
    def string_to_number(value):
        """
        Преобразует строку в число.

        :param value: Строка, представляющая число.
        :return: Преобразованное число.
        """
        return int(float(value))


