from src.item import Item


def test_calculate_total_price():
    item = Item("Книга", 10.0, 5)
    assert item.calculate_total_price() == 50.0


def test_apply_discount():
    item = Item("Книга", 10.0, 5)
    item.pay_rate = 0.9  # Устанавливаем скидку в 10%
    item.apply_discount()
    assert item.price == 9.0
