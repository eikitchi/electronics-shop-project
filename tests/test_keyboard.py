import pytest
from src.keyboard import KeyBoard


@pytest.fixture
def key_board():
    return KeyBoard('Dark Project KD87A', 9600, 5)


def test_KeyBoard(key_board):
    assert str(key_board) == "Dark Project KD87A"


def test_change_lang(key_board):
    assert str(KeyBoard.language) == "EN"

    key_board.change_lang()
    assert str(key_board.language) == "RU"

    key_board.change_lang().change_lang()
    assert str(key_board.language) == "RU"
