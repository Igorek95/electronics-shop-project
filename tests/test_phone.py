from src.item import Item
from src.phone import Phone
import pytest


def test_create_phone():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert phone.name == "iPhone 14"
    assert phone.price == 120_000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2


def test_invalid_number_of_sim():
    with pytest.raises(ValueError):
        Phone("Samsung Galaxy", 100_000, 10, -1)  # Should raise ValueError


def test_add_phones():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("Samsung Galaxy", 100_000, 10, 1)
    result = phone1 + phone2
    assert result == 15  # Total quantity of phones (5 + 10)

    item = Item("Some Item", 50, 3)
    with pytest.raises(TypeError):
        phone1 + item  # Should raise TypeError
