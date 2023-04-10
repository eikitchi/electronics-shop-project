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
