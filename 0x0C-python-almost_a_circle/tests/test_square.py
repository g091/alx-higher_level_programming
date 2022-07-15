#!/usr/bin/python3
"""Unit tests for the `Square` class"""
import unittest
import json
import sys
import os

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """Unit tests for the `Square` class"""
    def setUp(self):
        """Hook that runs before each unit test"""
        Base._Base__nb_objects = 0

    def test_docstring(self):
        """Docstring test"""
        self.assertIsNotNone(Base.__doc__)

    def test_is_instance(self):
        """Is instance test"""
        self.assertTrue(isinstance(Square(1, 1), Square))

    def test_is_subclass(self):
        """Is subclass test"""
        self.assertTrue(issubclass(type(Square(1, 1)), Base))

    def test_empty_init(self):
        """Empty init"""
        self.assertRaises(TypeError, Square, ())

    def test_init_with_width_less_or_equal_0(self):
        """Init with width <= 0"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 1)

    def test_width_is_not_int(self):
        """Width is not int"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1", 1)

    def test_x_is_not_int(self):
        """x is not int"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "1", -1)

    def test_x_is_less_than_0(self):
        """x is < 0"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -1, -1)

    def test_y_is_not_int(self):
        """y is not int"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "1")

    def test_y_is_less_than_0(self):
        """x is < 0"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 0, -1)

    def test__str__(self):
        """ __str__"""
        self.assertEqual(Square(1, 0, 0, 1).__str__(), "[Square] (1) 0/0 - 1")

    def test_area(self):
        """Area test"""
        self.assertEqual(Square(2, 2, 0, 0).area(), 4)

    def test_update_args(self):
        """Update with args"""
        r = Square(1, 1, 0, 0)
        r.update(2, 2, 2, 2, 2)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)

    def test_update_kwargs(self):
        """Update with kwargs"""
        r = Square(1, 1, 0, 0)
        r.update(id=2, size=2, x=2, y=2)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.size, 2)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)

    def test_to_dictionary(self):
        """to_dictionary"""
        temp = Square(1, 1, 1, 1)
        r1 = temp.to_dictionary()
        r2 = {"id": 1,  "size": 1, "x": 1, "y": 1}
        self.assertEqual(r1, r2)

    def test_json_string_to_file(self):
        """From json file"""
        temp1 = Square(1, 1, 1, 1)
        temp2 = Square(5, 6, 7, 8)
        Square.save_to_file([temp1, temp2])
        with open("Square.json") as file:
            r1 = file.read()
            r2 = [temp1.to_dictionary(), temp2.to_dictionary()]
            self.assertEqual(json.dumps(r2), r1)

    def test_json_string_to_file_empty(self):
        """From json file empty"""
        Square.save_to_file([])
        with open("Square.json") as a_file:
            self.assertEqual(json.loads(a_file.read()), [])

    def test_from_json(self):
        """From json"""
        temp1 = Square(1, 1, 1, 1)
        temp2 = Square(5, 6, 7, 8)
        r1 = [temp1.to_dictionary(), temp2.to_dictionary()]
        self.assertTrue(isinstance(r1, list))
        r2 = Square.to_json_string(r1)
        self.assertTrue(isinstance(r2, str))
        r3 = Square.from_json_string(r2)
        self.assertTrue(isinstance(r3, list))

    def test_create(self):
        """Create method"""
        r1 = Square(1, 1, 1)
        dict1 = r1.to_dictionary()
        r2 = Square.create(**dict1)
        self.assertFalse(r1 == r2)
        self.assertFalse(r1 is r2)

    def test_load_from_file(self):
        """Loading from json file"""
        r1 = Square(1, 1, 1, 1)
        r2 = Square(5, 6, 7, 8)
        lists = [r1, r2]
        Square.save_to_file(lists)

        out = Square.load_from_file()
        self.assertTrue(isinstance(out, list))

        self.assertTrue(isinstance(out[0], Square))
        self.assertTrue(isinstance(out[1], Square))
        self.assertEqual(str(r1), str(out[0]))
        self.assertEqual(str(r2), str(out[1]))

    def test_return_empty(self):
        """json_to_string returns none"""
        output = Square.to_json_string(None)
        self.assertEqual(output, "[]")
        output = Square.to_json_string([])
        self.assertEqual(output, "[]")

    def test_save_empty(self):
        """Empty list input"""
        lists = []
        Square.save_to_file(lists)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_None(self):
        """Input is none"""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_load_no_file(self):
        """File doesnt exist"""
        try:
            Square.save_to_file(None)
            os.remove("Square.json")
        except BaseException:
            pass

        self.assertEqual(Square.load_from_file(), [])

    def test_load_empty_file(self):
        """File is empty"""
        try:
            Square.save_to_file(None)
            os.remove("Square.json")
        except BaseException:
            pass

        open("Square.json", 'a').close()
        self.assertEqual(Square.load_from_file(), [])

    def test_class_basic_init(self):
        """Ids"""
        self.assertEqual(Square(1).size, 1)
        self.assertEqual(Square(1, 2).x, 2)
