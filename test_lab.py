import unittest
from lab_code import (
    is_strong_password,
    classify_number,
    is_anagram,
    Inventory
)

class TestPasswordValidator(unittest.TestCase):
    def test_strong_password(self):
        self.assertTrue(is_strong_password("Abcd@123"))
        self.assertFalse(is_strong_password("abcd123"))
        self.assertFalse(is_strong_password("Abcdefg"))

class TestNumberClassification(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(classify_number(10), "Positive")

    def test_negative(self):
        self.assertEqual(classify_number(-5), "Negative")

    def test_zero(self):
        self.assertEqual(classify_number(0), "Zero")

    def test_invalid(self):
        self.assertEqual(classify_number("abc"), "Invalid input")

class TestAnagram(unittest.TestCase):
    def test_anagram_true(self):
        self.assertTrue(is_anagram("listen", "silent"))

    def test_anagram_false(self):
        self.assertFalse(is_anagram("hello", "world"))

class TestInventory(unittest.TestCase):
    def test_inventory_operations(self):
        inv = Inventory()
        inv.add_item("Pen", 10)
        self.assertEqual(inv.get_stock("Pen"), 10)

        inv.remove_item("Pen", 5)
        self.assertEqual(inv.get_stock("Pen"), 5)

        with self.assertRaises(ValueError):
            inv.remove_item("Pen", 10)

if __name__ == "__main__":
    unittest.main()