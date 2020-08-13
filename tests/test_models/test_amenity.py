#!/usr/bin/python3
""" test amenity file """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from sqlalchemy.orm.collections import InstrumentedList
import models
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
import os
from datetime import datetime
from models.base_model import Base
from sqlalchemy.orm import sessionmaker
from time import sleep
from tests.test_models.test_base_model import TestBaseModel
NoneType = type(None)


class TestAmenity(unittest.TestCase):
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

    def test_name2(self):
        """ """
        new = Amenity()
        self.assertTrue(hasattr(new, "name"))
        self.assertEqual(type(new.name), NoneType)

    def test_place_amenities(self):
        """ """
        new = Amenity()
        self.assertTrue(hasattr(new, "place_amenities"))
        self.assertEqual(type(new.place_amenities), InstrumentedList)

    def test_instance_attributes(self):
        """test for attributes."""
        am = Amenity()
        self.assertTrue(hasattr(am, "__tablename__"))
        self.assertTrue(hasattr(am, "name"))
        self.assertTrue(hasattr(am, "place_amenities"))

    def test_inherits_BaseModel(self):
        """test if subclass of BaseModel."""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_init_args_kwargs(self):
        """Test initialization with args and kwargs."""
        dt = datetime.utcnow()
        bm = Amenity(id="345", created_at=dt.isoformat())
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)

    @unittest.skipIf(type(models.storage) is DBStorage, "Filestorage")
    def test_save_Amenity(self):
        """test if the save works"""
        am = Amenity()
        sleep(0.6)
        am.save()
        self.assertNotEqual(am.created_at, am.updated_at)


if __name__ == "__main__":
    unittest.main()
