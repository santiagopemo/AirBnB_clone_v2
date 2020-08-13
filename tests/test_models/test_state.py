#!/usr/bin/python3
""" test state file """
from models.state import State
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


class TestState(unittest.TestCase):
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

    def test_name3(self):
        """ """
        new = State()
        self.assertEqual(type(new.name), NoneType)

    def test_pep8_Review(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_State(self):
        """checking for docstrings"""
        self.assertIsNotNone(State.__doc__)

    def test_attributes_State(self):
        """test State have attributes"""
        st = State()
        self.assertTrue(hasattr(st, '__tablename__'))
        self.assertTrue('id' in st.__dict__)
        self.assertTrue('created_at' in st.__dict__)
        self.assertTrue('updated_at' in st.__dict__)
        self.assertTrue(hasattr(st, 'name'))

    def test_attributes(self):
        """test for attributes type"""
        st = State()
        self.assertEqual(str, type(st.id))
        self.assertEqual(datetime, type(st.created_at))
        self.assertEqual(datetime, type(st.updated_at))
        self.assertTrue(hasattr(st, "name"))

    def test_is_subclass_State(self):
        """test if State is subclass of BaseModel"""
        st = State()
        self.assertTrue(issubclass(st.__class__, BaseModel), True)

    @unittest.skipIf(type(models.storage) is DBStorage, "Filestorage")
    def test_save_State(self):
        """test save"""
        st = State()
        sleep(0.6)
        st.save()
        self.assertNotEqual(st.created_at, st.updated_at)

    @unittest.skipIf(type(models.storage) is DBStorage, "Filestorage")
    def test_to_dict(self):
        """test to_dict"""
        st = State()
        st.save()
        state_dict = st.to_dict()
        self.assertEqual(dict, type(state_dict))
        self.assertEqual(st.id, state_dict["id"])
        self.assertEqual("State", state_dict["__class__"])
        self.assertEqual(st.created_at.isoformat(),
                         state_dict["created_at"])
        self.assertEqual(st.updated_at.isoformat(),
                         state_dict["updated_at"])


if __name__ == "__main__":
    unittest.main(defaultTest="TestBaseModel", exit=False)
