#!/usr/bin/python3
""" """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from sqlalchemy.orm.collections import InstrumentedList
NoneType = type(None)


class test_City(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(cls):
        """test_city testing setup"""
        pass

    def setUp(self):
        """executes after a test"""
        self.name = "City"
        self.value = City

    def tearDown(self):
        """executes before a test"""
        pass

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), NoneType)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), NoneType)

    def test_places(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.places), InstrumentedList)
