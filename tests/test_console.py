#!/usr/bin/python3
"""test_console module"""
import unittest
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
import os
import pep8
import models
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
HBNB = HBNBCommand()



class TestConsole(unittest.TestCase):
    """TestConsole Class"""
    def setUp(self):
        """Executes before a test case"""
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Executes after a test case"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    @unittest.skipIf(type(models.storage) == DBStorage, "Testing DBStorage")
    def test_create_no_args(self):
        """test do_create alone"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNB.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())

    @unittest.skipIf(type(models.storage) == DBStorage, "Testing DBStorage")
    def test_create_wrong_class(self):
        """test do_create wrong class"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNB.onecmd("create mmmmm")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())

    @unittest.skipIf(type(models.storage) == DBStorage, "Testing DBStorage")
    def test_create(self):
        """test do_create"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNB.onecmd("create BaseModel")
            bm = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNB.onecmd("create User")
            us = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNB.onecmd("create State")
            st = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNB.onecmd("create Place")
            pl = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNB.onecmd("create City")
            ct = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNB.onecmd("create Review")
            rv = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNB.onecmd("create Amenity")
            am = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNB.onecmd("all")
            self.assertIn(bm, f.getvalue())
            self.assertIn(us, f.getvalue())
            self.assertIn(st, f.getvalue())
            self.assertIn(pl, f.getvalue())
            self.assertIn(ct, f.getvalue())
            self.assertIn(rv, f.getvalue())
            self.assertIn(am, f.getvalue())

if __name__ == "__main__":
    unittest.main()        
