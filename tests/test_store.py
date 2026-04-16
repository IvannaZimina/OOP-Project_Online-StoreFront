"""
tests/test_store.py — Unit tests for the Online Storefront project.

Run from the project root:
        py -m unittest discover tests -v
"""

import sys
import os
import unittest

# Ensure the src folder is on the path when running from the tests/ folder
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_path = os.path.join(project_root, "src")
sys.path.insert(0, src_path)

from core.product import PhysicalProduct, DigitalProduct
from core.cart import Cart


# ===================================================================== #
#  Product tests                                                          #
# ===================================================================== #

class TestProduct(unittest.TestCase):

    # Set up common test data for product tests.
    def setUp(self):
        self.laptop = PhysicalProduct("P001", "Laptop", 999.99, 5, 2.5)
        self.ebook = DigitalProduct("D001", "Python Guide", 19.99, 100,
                                    "http://example.com/guide")

    # Verify that the product attributes are set correctly.
    def test_physical_shipping_cost(self):
        # check the function: shipping cost = weight * 2.50
        # assertAlmostEqual: compare floats with a small tolerance for rounding.
        self.assertAlmostEqual(self.laptop.calculate_shipping(), 6.25)

    def test_digital_no_shipping(self):
        # Verify that a digital product has zero shipping.
        # assertEqual: check exact equality of two values.
        self.assertEqual(self.ebook.calculate_shipping(), 0.0)

    def test_price_setter_rejects_negative(self):
        # Verify that a negative price is rejected.
        # assertRaises: expects the code inside to raise the given exception.
        with self.assertRaises(ValueError):
            self.laptop.price = -1


# ===================================================================== #
#  Cart tests                                                             #
# ===================================================================== #

class TestCart(unittest.TestCase):

    def setUp(self):
        self.product = PhysicalProduct("P001", "Widget", 10.00, 20, 1.0)
        self.cart = Cart()

    def test_add_product_appears_in_cart(self):
        # Verify that the product is added with the correct quantity.
        self.cart.add_product(self.product, 3)

        # assertEqual: check exact equality of two values.
        self.assertEqual(len(self.cart.items), 1)

        # assertEqual: check exact equality of two values.
        self.assertEqual(self.cart.items[0].quantity, 3)

    def test_subtotal_calculation(self):
        # Verify the subtotal without shipping.
        self.cart.add_product(self.product, 4)
        
        # assertAlmostEqual: compare floats with a small tolerance for rounding.
        self.assertAlmostEqual(self.cart.get_total(), 40.00)

    def test_shipping_total_calculation(self):
        """Shipping total = weight * 2.50 * quantity."""
        self.cart.add_product(self.product, 2)

        # 1.0 kg * 2.50 * 2 = 5.00
        # assertAlmostEqual: compare floats with a small tolerance for rounding.
        self.assertAlmostEqual(self.cart.get_shipping_total(), 5.00)

    def test_grand_total_includes_shipping(self):
        # Verify the grand total includes shipping.
        self.cart.add_product(self.product, 1)
        expected = 10.00 + 2.50  # price + shipping (1 kg)

        # assertAlmostEqual: compare floats with a small tolerance for rounding.
        self.assertAlmostEqual(self.cart.get_grand_total(), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
