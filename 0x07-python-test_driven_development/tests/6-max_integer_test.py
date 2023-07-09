#!/usr/bin/python3
"""
This is the unittest of max integer of list module.
It contains a class for unitest max_integer module.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMax(unittest.TestCase):
    """Define unittests for max_integer([])"""
    def test_max_integer(self):
        list1 = [2, 3, 4, 5, 6]
        expected_max = 6
        actual_max = max_integer(list1)
        self.assertEqual(actual_max, expected_max)
        self.assertIsNotNone(max_integer(list1))

        list2 = [10]
        expected_max = 10
        actual_max = max_integer(list2)
        self.assertEqual(actual_max, expected_max)
        self.assertIsNotNone(max_integer(list2))

        list3 = [-10, -5, -1, 0]
        expected_max = 0
        actual_max = max_integer(list3)
        self.assertEqual(actual_max, expected_max)
        self.assertIsNotNone(max_integer(list3))

        list4 = [-10, -5, -10, 0, 0]
        expected_max = 0
        actual_max = max_integer(list4)
        self.assertEqual(actual_max, expected_max)
        self.assertIsNotNone(max_integer(list4))

        list5 = ["ALX", -5, -10, 0, 0]
        with self.assertRaises(TypeError):
            max_integer(list5)

        empty = []
        self.assertEqual(max_integer(empty), None)
