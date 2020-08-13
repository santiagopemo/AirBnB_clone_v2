#!/usr/bin/python3
""" test place file """
from models.place import Place
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


class TestPlace(unittest.TestCase):
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

    def test_city_id(self):
        """ """
        new = Place()
        self.assertEqual(type(new.city_id), NoneType)

    def test_user_id(self):
        """ """
        new = Place()
        self.assertEqual(type(new.user_id), NoneType)

    def test_name(self):
        """ """
        new = Place()
        self.assertEqual(type(new.name), NoneType)

    def test_description(self):
        """ """
        new = Place()
        self.assertEqual(type(new.description), NoneType)

    def test_number_rooms(self):
        """ """
        new = Place()
        self.assertEqual(type(new.number_rooms), NoneType)

    def test_number_bathrooms(self):
        """ """
        new = Place()
        self.assertEqual(type(new.number_bathrooms), NoneType)

    def test_max_guest(self):
        """ """
        new = Place()
        self.assertEqual(type(new.max_guest), NoneType)

    def test_price_by_night(self):
        """ """
        new = Place()
        self.assertEqual(type(new.price_by_night), NoneType)

    def test_latitude(self):
        """ """
        new = Place()
        self.assertEqual(type(new.latitude), NoneType)

    def test_longitude(self):
        """ """
        new = Place()
        self.assertEqual(type(new.latitude), NoneType)

    def test_amenity_ids(self):
        """ """
        new = Place()
        self.assertEqual(type(new.amenity_ids), list)

    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/place.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """Check for docstrings."""
        self.assertIsNotNone(Place.__doc__)

    def test_attributes(self):
        """test attributes"""
        pl = Place()
        self.assertEqual(str, type(pl.id))
        self.assertEqual(datetime, type(pl.created_at))
        self.assertEqual(datetime, type(pl.updated_at))
        self.assertTrue(hasattr(pl, "__tablename__"))
        self.assertTrue(hasattr(pl, "city_id"))
        self.assertTrue(hasattr(pl, "name"))
        self.assertTrue(hasattr(pl, "description"))
        self.assertTrue(hasattr(pl, "number_rooms"))
        self.assertTrue(hasattr(pl, "number_bathrooms"))
        self.assertTrue(hasattr(pl, "max_guest"))
        self.assertTrue(hasattr(pl, "price_by_night"))
        self.assertTrue(hasattr(pl, "latitude"))
        self.assertTrue(hasattr(pl, "longitude"))

    def test_is_subclass(self):
        """Check that Place is a subclass of BaseModel."""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_init(self):
        """Test initialization."""
        pl = Place()
        self.assertIsInstance(pl, Place)

    @unittest.skipIf(type(models.storage) is DBStorage, "Filestorage")
    def test_save_filestorage(self):
        """Test save """
        pl = Place()
        sleep(0.6)
        pl.save()
        self.assertNotEqual(pl.created_at, pl.updated_at)

    def test_to_dict(self):
        """Test to_dict method."""
        pl = Place()
        place_dict = pl.to_dict()
        self.assertEqual(dict, type(place_dict))
        self.assertEqual(pl.id, place_dict["id"])
        self.assertEqual("Place", place_dict["__class__"])
        self.assertEqual(pl.created_at.isoformat(),
                         place_dict["created_at"])
        self.assertEqual(pl.updated_at.isoformat(),
                         place_dict["updated_at"])


if __name__ == "__main__":
    unittest.main(defaultTest="TestBaseModel", exit=False)
