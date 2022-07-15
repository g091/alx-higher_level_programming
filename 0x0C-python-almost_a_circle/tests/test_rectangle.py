#!/usr/bin/python3
"""Tests for the `Rectangle` class"""
import unittest
import json
import sys
from contextlib import contextmanager
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Unit tests for the `Rectangle` class"""
    def setUp(self):
        """Hook that runs before each unit test"""
        Base._Base__nb_objects = 0

    @contextmanager
    def captured_output(self):
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err

    def test_docstring(self):
        """Docstring test"""
        self.assertIsNotNone(Base.__doc__)

    def test_is_instance(self):
        """Is instance test"""
        self.assertTrue(isinstance(Rectangle(1, 1), Rectangle))

    def test_is_subclass(self):
        """Is subclass test"""
        self.assertTrue(issubclass(type(Rectangle(1, 1)), Base))

    def test_empty_init(self):
        """Empty init test"""
        self.assertRaises(TypeError, Rectangle, ())
        self.assertRaises(TypeError, Rectangle, (1))

    def test_init_with_width_less_or_equal_0(self):
        """Init with width <= 0"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 1)

    def test_init_with_height_less_or_equal_0(self):
        """Init with height <= 0"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

    def test_width_is_not_int(self):
        """Width is not int"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 1)

    def test_height_is_not_int(self):
        """Height is not int"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "1")

    def test_x_is_not_int(self):
        """x is not int"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, "1", -1)

    def test_x_is_less_than_0(self):
        """x is < 0"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 1, -1, -1)

    def test_y_is_not_int(self):
        """y is not int"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, "1")

    def test_y_is_less_than_0(self):
        """x is < 0"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 0, -1)

    def test__str__(self):
        """ __str__"""
        self.assertEqual(Rectangle(1, 1, 0, 0).__str__(),
                         "[Rectangle] (1) 0/0 - 1/1")

    def test_area(self):
        """Area test"""
        self.assertEqual(Rectangle(2, 2, 0, 0).area(), 4)

    def test_update_args(self):
        """Update with args"""
        r = Rectangle(1, 1, 0, 0)
        r.update(2, 2, 2, 2, 2)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)

    def test_update_kwargs(self):
        """Update with kwargs"""
        r = Rectangle(1, 1, 0, 0)
        r.update(id=2, width=2, height=2, x=2, y=2)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)

    def test_to_dictionary(self):
        """to_dictionary"""
        temp = Rectangle(1, 1, 1, 1)
        r1 = temp.to_dictionary()
        r2 = {"id": 1,  "height": 1, "width": 1, "x": 1, "y": 1}
        self.assertEqual(r1, r2)

    def test_to_json_string(self):
        """JSON string"""
        temp = Rectangle(1, 1, 1, 1, 1)
        r1 = temp.to_dictionary()
        r2 = temp.to_json_string(r1)
        self.assertEqual(r2, json.dumps(r1))

    def test_json_string_to_file(self):
        """From json file"""
        temp1 = Rectangle(1, 1, 1, 1, 1)
        temp2 = Rectangle(5, 6, 7, 8, 9)
        Rectangle.save_to_file([temp1, temp2])
        with open("Rectangle.json") as file:
            r1 = file.read()
            r2 = [temp1.to_dictionary(), temp2.to_dictionary()]
            self.assertEqual(r1, json.dumps(r2))

    def test_json_string_to_file_empty(self):
        """From json file empty"""
        Rectangle.save_to_file([])
        with open("Rectangle.json") as a_file:
            self.assertEqual(json.loads(a_file.read()), [])

    def test_from_json(self):
        """From json"""
        temp1 = Rectangle(1, 1, 1, 1, 1)
        temp2 = Rectangle(5, 6, 7, 8, 9)
        r1 = [temp1.to_dictionary(), temp2.to_dictionary()]
        self.assertTrue(isinstance(r1, list))
        r2 = Rectangle.to_json_string(r1)
        self.assertTrue(isinstance(r2, str))
        r3 = Rectangle.from_json_string(r2)
        self.assertTrue(isinstance(r3, list))

    def test_create(self):
        """Create method"""
        r1 = Rectangle(1, 1, 1)
        dict1 = r1.to_dictionary()
        r2 = Rectangle.create(**dict1)
        self.assertFalse(r1 == r2)
        self.assertFalse(r1 is r2)

    def test_load_from_file(self):
        """Loading from json file"""
        r1 = Rectangle(1, 1, 1, 1, 1)
        r2 = Rectangle(5, 6, 7, 8, 2)
        lists = [r1, r2]
        Rectangle.save_to_file(lists)

        out = Rectangle.load_from_file()
        self.assertTrue(isinstance(out, list))

        self.assertTrue(isinstance(out[0], Rectangle))
        self.assertTrue(isinstance(out[1], Rectangle))
        self.assertEqual(str(r1), str(out[0]))
        self.assertEqual(str(r2), str(out[1]))

    def test_return_empty(self):
        """json_to_string returns none"""
        output = Rectangle.to_json_string(None)
        self.assertEqual(output, "[]")
        output = Rectangle.to_json_string([])
        self.assertEqual(output, "[]")

    def test_save_empty(self):
        """Empty list input"""
        lists = []
        Rectangle.save_to_file(lists)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_None(self):
        """Input is none"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_load_no_file(self):
        """File doesnt exist"""
        try:
            Rectangle.save_to_file(None)
            os.remove("Rectangle.json")
        except BaseException:
            pass

        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_empty_file(self):
        """File is empty"""
        try:
            Rectangle.save_to_file(None)
            os.remove("Rectangle.json")
        except BaseException:
            pass

        open("Rectangle.json", 'a').close()
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_class_basic_init(self):
        """Ids"""
        self.assertEqual(Rectangle(1, 1).id, 1)

    def test_display_basic_square(self):
        """Print the instance"""
        with self.captured_output() as (out, err):
            Rectangle(2, 2).display()
            # This can go inside or outside the `with` block
            output = out.getvalue().strip()
            self.assertEqual(output, "##\n##")

    def test_display_square_with_x(self):
        """Print the instance"""
        with self.captured_output() as (out, err):
            Rectangle(2, 2, 2).display()
            # This can go inside or outside the `with` block
            output = out.getvalue()
            print(output)
            self.assertEqual(output, "  ##\n  ##\n")

    def test_display_square_with_y(self):
        """Print the instance"""
        with self.captured_output() as (out, err):
            Rectangle(2, 2, 0, 2).display()
            # This can go inside or outside the `with` block
            output = out.getvalue()
            self.assertEqual(output, "\n\n##\n##\n")

    def test_display_square_with_x_and_y(self):
        """Print the instance"""
        with self.captured_output() as (out, err):
            Rectangle(2, 2, 2, 2).display()
            # This can go inside or outside the `with` block
            output = out.getvalue()
            self.assertEqual(output, "\n\n  ##\n  ##\n")
