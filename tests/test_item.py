"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def new_item():
    yield Item("item1", 100.0, 5)


def test_calculate_total_price(new_item):
    assert new_item.calculate_total_price() == 500.0


def test_apply_discount(new_item):
    new_item.pay_rate = 0.9
    new_item.apply_discount()
    assert new_item.price == 90.0


def test_name(new_item):
    assert new_item.name == "item1"


def test_price(new_item):
    assert new_item.price == 100.0


def test_quantity(new_item):
    assert new_item.quantity == 5


def test_item_creation():
    item = Item("Карандаш", 25.0, 50)
    assert item.name == "Карандаш"
    assert item.price == 25.0
    assert item.quantity == 50


def test_item_name_length():
    try:
        item = Item("Ноутбук Lenovo", 50000.0, 5)
    except ValueError as e:
        assert str(e) == "Наименование товара не может быть больше 10 символов"


def test_item_total_price():
    item = Item("Чайник", 2000.0, 10)
    assert item.calculate_total_price() == 20000.0


def test_item_discount():
    Item.pay_rate = 0.9
    item = Item("Кофеварка", 5000.0, 3)
    item.apply_discount()
    assert item.price == 4500.0


def test_item_instantiation_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert Item.all[0].name == "Смартфон"
    assert Item.all[0].price == 100
    assert Item.all[0].quantity == 1
    assert Item.all[1].name == "Ноутбук"
    assert Item.all[1].price == 1000
    assert Item.all[1].quantity == 3


def test_string_to_number():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('10.0') == 10.0


def test_repr():
    item = Item('Test Item', 10, 2)
    assert repr(item) == "Item('Test Item', 10, 2)"


def test_str():
    item = Item('Test Item', 10, 2)
    assert str(item) == "Test Item"
