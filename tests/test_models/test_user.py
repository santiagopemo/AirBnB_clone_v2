#!/usr/bin/python3
""" test user file """
from models.user import User
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


class TestUser(unittest.TestCase):
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

    def test_first_name(self):
        """ """
        new = User()
        self.assertEqual(type(new.first_name), NoneType)

    def test_last_name(self):
        """ """
        new = User()
        self.assertEqual(type(new.last_name), NoneType)

    def test_email(self):
        """ """
        new = User()
        self.assertEqual(type(new.email), NoneType)

    def test_password(self):
        """ """
        new = User()
        self.assertEqual(type(new.password), NoneType)

    def test_pep8_User(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_User(self):
        """checking for docstrings"""
        self.assertIsNotNone(User.__doc__)

    def test_attributes_User(self):
        """chekcing if User have attributes"""
        us = User()
        self.assertTrue(hasattr(us, "__tablename__"))
        self.assertTrue(hasattr(us, "email"))
        self.assertTrue(hasattr(us, "id"))
        self.assertTrue(hasattr(us, "created_at"))
        self.assertTrue(hasattr(us, "updated_at"))
        self.assertTrue(hasattr(us, "password"))
        self.assertTrue(hasattr(us, "first_name"))
        self.assertTrue(hasattr(us, "last_name"))

    def test_is_subclass_User(self):
        """test if User is subclass of Basemodel"""
        us = User()
        self.assertTrue(issubclass(us.__class__, BaseModel), True)

    @unittest.skipIf(type(models.storage) is DBStorage, "Filestorage")
    def test_save_User(self):
        """test if the save works"""
        us = User()
        sleep(0.6)
        us.save()
        self.assertNotEqual(us.created_at, us.updated_at)

    def test_to_dict_User(self):
        """test if dictionary works"""
        us = User()
        self.assertEqual('to_dict' in dir(us), True)


if __name__ == "__main__":
    unittest.main(defaultTest="TestBaseModel", exit=False)
