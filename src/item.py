import csv
import os


class InstantiateCSVError(Exception):
    """Исключение для ошибок при чтении CSV файла."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


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

    @classmethod
    def instantiate_from_csv(cls):
        """
                Создает экземпляры класса Item из данных CSV-файла.

                :return: Список экземпляров товаров.
                :raises FileNotFoundError: Если файл item.csv не найден.
                :raises InstantiateCSVError: Если файл item.csv поврежден.
        """
        items = []
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(current_dir, '..', 'src', 'items.csv')

        try:
            with open(csv_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    name = row.get('name')
                    price = cls.string_to_number(row.get('price'))
                    quantity = int(row.get('quantity'))
                    if not name or price is None or quantity is None:
                        raise InstantiateCSVError("Файл item.csv поврежден")
                    item = cls(name, price, quantity)
                    items.append(item)
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")
        return items
