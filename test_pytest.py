import pytest
from lab_code import (
    is_strong_password,
    classify_number,
    is_anagram,
    Inventory
)

def test_password():
    assert is_strong_password("Abcd@123")
    assert not is_strong_password("abcd123")
    assert not is_strong_password("Abcdefg")

def test_classify_number():
    assert classify_number(10) == "Positive"
    assert classify_number(-5) == "Negative"
    assert classify_number(0) == "Zero"
    assert classify_number("abc") == "Invalid input"

def test_anagram():
    assert is_anagram("listen", "silent")
    assert not is_anagram("hello", "world")

def test_inventory():
    inv = Inventory()
    inv.add_item("Pen", 10)
    assert inv.get_stock("Pen") == 10

    inv.remove_item("Pen", 5)
    assert inv.get_stock("Pen") == 5

    with pytest.raises(ValueError):
        inv.remove_item("Pen", 10)