import pytest

from src.phone import Phone
from src.item import Item


@pytest.fixture
def new_item():
    return Item("item1", 100.0, 5)


@pytest.fixture
def new_phone():
    return Phone("Samsung", 80000, 10, 2)