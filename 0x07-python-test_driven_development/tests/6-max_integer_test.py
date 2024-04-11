#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test when the list is not empty
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

        # Test when the list is empty
        self.assertIsNone(max_integer([]))

        # Test with negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

        # Test with mixed integers
        self.assertEqual(max_integer([1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-1, -3, 4, -2]), 4)

        # Test with a single element
        self.assertEqual(max_integer([5]), 5)

        # Test with a large list
        self.assertEqual(max_integer(list(range(10000))), 9999)

if __name__ == '__main__':
    unittest.main()

