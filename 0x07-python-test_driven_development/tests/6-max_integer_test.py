#!/usr/bin/python3
"""Unittest for the max_integer module"""
import unittest
from importlib import import_module
max_integer = import_module('6-max_integer', '..').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        """Tests for empty list"""
        self.assertEqual(max_integer([]), None)

    def test_proper_case(self):
        """Test for proper working case"""
        l = [2, 4, 6, 8]
        maxnum = max_integer(l)
        self.assertEqual(maxnum, 8)

    def test_proper_case_negative(self):
        """Test for negative integers"""
        l = [-2, -4, -6]
        maxnum = max_integer(l)
        self.assertEqual(maxnum, -2)

    def test_not_ints(self):
        """Test for ints and not ints"""
        l = ["a", "b", 1]
        self.assertRaises(TypeError, max_integer, l)

    def test_floats(self):
        """Test for a float in list"""
        l = [1, 2, 2.5]
        result = max_integer(l)
        self.assertEqual(result, 2.5)

    def test_strings(self):
        """Test for string list, max returns first string"""
        l = ["hello", "World"]
        result = max_integer(l)
        self.assertEqual(result, "hello")

    def test_one_element(self):
        """list with one element"""
        l = [1]
        result = max_integer(l)
        self.assertEqual(result, 1)

    def test_no_list(self):
        """No list"""
        self.assertRaises(TypeError, max_integer, None)

    def test_same_element(self):
        """same elements in a list"""
        l = [1, 1, 1]
        result = max_integer(l)
        self.assertEqual(result, 1)
    
    def test_list_in_order(self):
        """List that's in order"""
        l = [3, 2, 1]
        result = max_integer(l)
        self.assertEqual(result, 3)

    def test_only_floats(self):
        """test only floats"""
        l = [1.5, 1.0, 4.9, 6.9]
        result = max_integer(l)
        self.assertEqual(result, 6.9)

    def test_not_list(self):
        """Test with a parameter that's not a list: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, 0)

    def test_max_middle(self):
        l = [1, 2, 10, 3, 0]
        result = max_integer(l)
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()
