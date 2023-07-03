#!/usr/bin/python3
"""
This is the unittest of max integer of list module.
It contains a class for unitest max_integer module.
"""

from max_integer_source import max_integer
import unittest


class TestMax(unittest.TestCase):
    def test_max_integer(self):
        list = [2, 3, 4, 5, 6]
        expected_max = 6
        actual_max = max_integer(list)
        self.assertEqual(actual_max, expected_max)
