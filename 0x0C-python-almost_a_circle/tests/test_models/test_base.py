#!/usr/bin/python3
"""
This is the unittest of Base Module
It contains a class for unitest
id is an integer and no need to test the type of it
"""

import unittest

from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Define unittests for Base class instantiation process"""

    def test_id_none(self):
        """test istantiontion of Base class with id attribute"""
        base1 = Base()
        base2 = Base()
        expected_id1 = base2.id - 1
        acttual_id1 = base1.id
        self.assertEqual(expected_id1, acttual_id1)

    def test_id_given(self):
        base1 = Base(15)
        self.assertEqual(base1.id, 15)

    def test_id_increm(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base3.id, 3)

    def test_multi_base_objects(self):
        base1 = Base(15)
        base2 = Base()
        base3 = Base(4)
        base4 = Base()
        self.assertEqual(base4.id, base2.id + 1)

    def test_none(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_obj_overwrite_id(self):
        base1 = Base(4)
        base1.id = 36
        self.assertEqual(36, base1.id)


if __name__ == "__main__":
    unittest.main()
