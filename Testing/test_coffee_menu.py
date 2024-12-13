# Unit tests for CoffeeMenu
import unittest
from coffe_menu import CoffeeMenu

class TestCoffeeMenu(unittest.TestCase):
    # Initialize a CoffeeMenu object
    def setUp(self):
        self.menu = CoffeeMenu()

    # Deletes the object after testing
    def tearDown(self):
        self.menu = None

    # Checks the price returned for an existing item from the menu
    def test_get_price_existing_item(self):
        self.assertEqual(self.menu.get_price("latte"), 2.75)

    # Checks the behavior for a non-existing item
    def test_get_price_non_existing_item(self):
        with self.assertRaises(ValueError):
            self.menu.get_price("black")

    # Checks if the item is correctly added
    def test_add_item(self):
        self.menu.add_item("cortado", 1.55)
        self.assertIn("cortado", self.menu.menu)
        self.assertEqual(self.menu.get_price("cortado"), 1.55)

if __name__ == "__main__":
    unittest.main()