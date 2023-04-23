
def test_phone(new_phone):
    assert new_phone.name == "Samsung"
    assert new_phone.price == 80000
    assert new_phone.quantity == 10
    assert new_phone.number_of_sim == 2


def test_str(new_phone):
    assert str(new_phone) == "Samsung"


def test_repr(new_phone):
    assert repr(new_phone) == "Phone('Samsung', 80000, 10, 2)"


def test_phone_setter(new_phone):
    assert new_phone.number_of_sim == 2
    new_phone.number_of_sim = 1
    assert new_phone.number_of_sim == 1
    new_phone.number_of_sim = 0
    assert new_phone.number_of_sim == 1
