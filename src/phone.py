from src.item import Item


class Phone(Item):
    """Класс для мобильных телефонов"""

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Конструктор класса Phone

        :param name: название мобильного телефона
        :param price: цена мобильного телефона
        :param quantity: количество мобильных телефонов в магазине
        :param number_of_sim: количество поддерживаемых сим-карт
        """
        super().__init__(name, price, quantity)

        if number_of_sim <= 0 and isinstance(number_of_sim, int):
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        """
        Возвращает количество поддерживаемых сим-карт
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """
        Устанавливает количество поддерживаемых сим-карт

        :param value: новое значение количества сим-карт
        """
        if value <= 0 and isinstance(value, int):
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.__number_of_sim = value

    def __str__(self):
        """
        Возвращает строковое представление мобильного телефона
        """
        return self.name

    def __repr__(self):
        """
        Возвращает строковое представление мобильного телефона в формате repr
        """
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        """
        Переопределение оператора сложения для класса Phone

        :param other: другой объект для сложения
        :return: суммарное количество товаров (количество мобильных телефонов и сим-карт)
        """
        if isinstance(other, Phone):
            return self.quantity + other.quantity
        else:
            return NotImplemented
