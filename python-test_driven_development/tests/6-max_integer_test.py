#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class to test the function max_integer"""

    def test_normal_list(self):
        """Test for a normal list"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_reverse_order(self):
        """Test in a reverse order list"""
        result = max_integer([4, 3, 2, 1])
        self.assertEqual(result, 4)

    def test_single_element(self):
        """Test in a single element list"""
        result = max_integer([10])
        self.assertEqual(result, 10)

    def test_empty_list(self):
        """Test in an empty list"""
        result = max_integer([])
        self.assertIsNone(result)

    def test_negative_numbers(self):
        """Test in a list of negative number"""
        result = max_integer([-1, -2, -3, -4])
        self.assertEqual(result, -1)

    def test_large_numbers(self):
        """Test with large numbers"""
        result = max_integer([100000000, 8000000000000, 4440000000])
        self.assertEqual(result, 8000000000000)

    def test_mixed_numbers(self):
        """Test with integers and floats"""
        result = max_integer([5, 3.5, 6, 7.5])
        self.assertEqual(result, 7.5)

if __name__ == '__main__':
    unittest.main()
