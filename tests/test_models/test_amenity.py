#!/usr/bin/python3
""" """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from sqlalchemy.orm.collections import InstrumentedList
NoneType = type(None)


class test_Amenity(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(cls):
        """test_city testing setup"""
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
