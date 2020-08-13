#!/usr/bin/python3
""" test city file """
import unittest
from models.city import City
from models.base_model import BaseModel
from sqlalchemy.orm.collections import InstrumentedList
from datetime import datetime
import models
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
import os
import pep8
from time import sleep
from tests.test_models.test_base_model import TestBaseModel
NoneType = type(None)


class TestCity(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(cls):
        """executes after all tests"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    @classmethod
    def tearDownClass(cls):
        """executes after all tests"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def setUp(self):
        """executes after a test"""
        pass

    def tearDown(self):
        """executes before a test"""
        pass

    def test_state_id(self):
        """ """
        new = City()
        self.assertEqual(type(new.state_id), NoneType)

    def test_name(self):
        """ """
        new = City()
        self.assertEqual(type(new.name), NoneType)

    def test_places(self):
        """ """
        new = City()
        self.assertEqual(type(new.places), InstrumentedList)

    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/city.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """Check for docstrings."""
        self.assertIsNotNone(City.__doc__)

    def test_instance_attributes(self):
        """Check for attributes."""
        ct = City()
        self.assertTrue(hasattr(ct, "__tablename__"))
        self.assertTrue(hasattr(ct, "name"))
        self.assertTrue(hasattr(ct, "state_id"))

    def test_is_subclass_City(self):
        """Inherits from BaseModel"""
        ct = City()
        self.assertTrue(issubclass(ct.__class__, BaseModel), True)

    @unittest.skipIf(type(models.storage) is DBStorage, "Filestorage")
    def test_save_City(self):
        """test if the save works"""
        ct = City()
        sleep(0.6)
        ct.save()
        self.assertNotEqual(ct.created_at, ct.updated_at)

    def test_to_dict(self):
        """test to_dict"""
        ct = City()
        self.assertTrue('to_dict' in dir(ct))


if __name__ == "__main__":
    unittest.main()
