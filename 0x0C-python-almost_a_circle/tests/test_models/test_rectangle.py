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
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle("3", 2, 2, 2)

    def test_str_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(2, "3")

    def test_str_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(3, 2, "sghv")

    def test_str_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(3, 2, 0, "45")

    def test_zero_attrs(self):
        with self.assertRaises(ValueError, msg="width must be greater than zero!"):
            Rectangle(-3, 2, 0, 5)
        with self.assertRaises(ValueError, msg="height must be greater than zero!"):
            Rectangle(3, -3, 4, 45)
        with self.assertRaises(ValueError, msg="x must be greater than zero!"):
            Rectangle(3, 2, -10, 45)
        with self.assertRaises(ValueError, msg="y must be greater than zero!"):
            Rectangle(3, 2, 10, -5)

    def test_to_dictionary(self):
        """test to_dictionary function
        """
        rect = Rectangle(1, 3, 15, 4, 4)
        dict = rect.to_dictionary()
        expected_dict = {
            "width": 1,
            "height": 3,
            "x": 15,
            "y": 4,
            "id": 4,

        }

        self.assertEqual(expected_dict, dict)

    def test_update(self):
        rec = Rectangle(3, 4, 5, 9, 8)
        rec.update(20, 15, 3, 6, 40)
        self.assertEqual(rec.width, 15)
        self.assertEqual(rec.height, 3)
        self.assertEqual(rec.x, 6)
        self.assertEqual(rec.y, 40)
        self.assertEqual(rec.id, 20)

    if __name__ == "__main__":
        unittest.main()
