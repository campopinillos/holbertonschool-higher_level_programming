#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    This is the class unittest for the max integer function
    """
    def test_sorted_list(self):
        sorted_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(sorted_list), 4)

    def test_float_list(self):
        f_l = [1.11, 2.22, 3.33, 4.44]
        self.assertEqual(max_integer(f_l), 4.44)


if __name__ == '__main__':
    unittest.main()
