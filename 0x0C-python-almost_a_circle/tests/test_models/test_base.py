#!/usr/bin/python3
"""
This is the unittest of Base Module
It contains a class for unitest
id is an integer and no need to test the type of it
"""

import unittest

from models.base import Base
from models.rectangle import Rectangle


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

    def test_to_json_string_method(self):
        list_of_dicts = [
            {
                "id": 1,
                "width": 25,
                "height": 15,
                "x": 25,
                "y": 25,

            },
            {
                "id": 1,
                "width": 5,
                "height": 15,
                "x": 4,
                "y": 7,
            }
        ]

        dumped = '[{"id": 1, "width": 25, "height": 5, "x": 5, "y": 5}, \
            {"id": 2, "width": 7, "height": 8, "x": 15, "y": 5}]'

        self.assertEqual(dumped, Base.to_json_string(list_of_dicts))

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        target_file = Rectangle.__name__ + ".json"
        expected_output = '[{"y": 8, "x": 2, "id": 1, "width": 10,\
            "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]'

        actual = Rectangle.save_to_file([r1, r2])

        with open(target_file, "r") as f:
            actual_out = f.read()
        self.assertEqual(expected_output, actual_out)

    if __name__ == "__main__":
        unittest.main()
