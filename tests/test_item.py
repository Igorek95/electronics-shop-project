from src.item import Item
import pytest


def test_calculate_total_price():
    item = Item("Книга", 10.0, 5)
    assert item.calculate_total_price() == 50.0


def test_apply_discount():
    item = Item("Книга", 10.0, 5)
    item.pay_rate = 0.9  # Устанавливаем скидку в 10%
    item.apply_discount()
    assert item.price == 9.0


def test_name_setter():
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'


def test_name_setter_too_long():
    item = Item('Телефон', 10000, 5)
    item.name = 'СуперСмартфон'
    assert item.name == 'СуперСмарт'


def test_instantiate_from_csv():
    items = Item.instantiate_from_csv()
    assert len(items) == 5


def test_item_creation_from_csv():
    items = Item.instantiate_from_csv()
    assert items[0].name == 'Смартфон'
    assert items[1].name == 'Ноутбук'
    assert items[2].name == 'Кабель'
    assert items[3].name == 'Мышка'
    assert items[4].name == 'Клавиатура'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr_and_str():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'


def test_add_items():
    item1 = Item("Item 1", 100, 5)
    item2 = Item("Item 2", 200, 10)
    result = item1 + item2
    assert result == 15  # Total quantity of items (5 + 10)

    with pytest.raises(TypeError):
        item1 + "not_an_item"  # Should raise TypeError
