#!/usr/bin/python3
"""
This is the unittest of Rectangle Module
It contains a class for unitest
"""

import unittest

from models.rectangle import Rectangle


class TestRectangleSubclass(unittest.TestCase):
    """Define unittests for Rectangle class"""
    def test_id_value(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def test_id_given(self):
        r1 = Rectangle(10, 2, 0, 0, 50)
        self.assertEqual(r1.id, 50)

    def test_priv_width(self):
        r1 = Rectangle(10, 2)
        with self.assertRaises(AttributeError):
            print(r1.__width)

        width = r1.width
        self.assertEqual(width, 10)

    def test_priv_height(self):
        r1 = Rectangle(10, 2)
        with self.assertRaises(AttributeError):
            print(r1.__height)

        height = r1.height
        self.assertEqual(height, 2)

    def test_priv_x(self):
        r1 = Rectangle(10, 2, 3)
        with self.assertRaises(AttributeError):
            print(r1.__x)

        x = r1.x
        self.assertEqual(x, 3)

    def test_priv_y(self):
        r1 = Rectangle(10, 2, 3, 6)
        with self.assertRaises(AttributeError):
            print(r1.__y)

        y = r1.y
        self.assertEqual(y, 6)

    def test_str_width(self):
        with self.assertRaises(TypeError, "width must be an integer"):
            Rectangle("3", 2)

    def test_str_height(self):
        with self.assertRaises(TypeError, "height must be an integer"):
            Rectangle(3, "2")

    def test_str_x(self):
        with self.assertRaises(TypeError, "x must be an integer"):
            Rectangle(3, 2, "sghv")

    def test_str_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(3, 2, 0, "45")

    if __name__ == "__main__":
        unittest.main()
