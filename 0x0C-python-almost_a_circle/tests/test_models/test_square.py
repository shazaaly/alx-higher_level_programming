#!/usr/bin/python3
"""
This is the unittest of Square Module
It contains a class for unitest
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """test Square class inistantiation
    """
    def test_inst(self):
        """test instantation from Suare class
        """
        square = Square(5)
        self.assertEqual(square.size, 5)

    if __name__ == "__main__":
        unittest.main()
