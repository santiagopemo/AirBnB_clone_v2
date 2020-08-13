#!/usr/bin/python3
"""test_basemodel module """
import os
import pep8
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import models


class TestBaseModel(unittest.TestCase):
    """Unittests for testing the BaseModel class."""

    @classmethod
    def setUpClass(cls):
        """executes after all tests"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        cls.storage = FileStorage()
        cls.base = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """executes after all tests"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        del cls.storage
        del cls.base

    def test_default(self):
        """default test """
        i = BaseModel()
        self.assertEqual(type(i), BaseModel)

    def test_kwargs(self):
        """test kwargs"""
        i = BaseModel()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = BaseModel()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_str(self):
        """ """
        i = BaseModel()
        self.assertEqual(str(i), '[{}] ({}) {}'.format('BaseModel', i.id,
                                                       i.__dict__))

    def test_todict(self):
        """ """
        i = BaseModel()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = BaseModel(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        new = BaseModel(**n)
        self.assertEqual(new.Name, 'test')

    def test_id(self):
        """ """
        new = BaseModel()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = BaseModel()
        self.assertEqual(type(new.created_at), datetime)

    def test_updated_at(self):
        """ """
        new = BaseModel()
        self.assertEqual(type(new.updated_at), datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertTrue(new.created_at == new.updated_at)

    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/base_model.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_attributes(self):
        """Check for attributes."""
        self.assertEqual(str, type(self.base.id))
        self.assertEqual(datetime, type(self.base.created_at))
        self.assertEqual(datetime, type(self.base.updated_at))

    def test_methods(self):
        """Check for methods."""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "delete"))
        self.assertTrue(hasattr(BaseModel, "__str__"))

    def test_init(self):
        """Test initialization."""
        self.assertIsInstance(self.base, BaseModel)

    def test_init_args_kwargs(self):
        """Test initialization with args and kwargs."""
        dt = datetime.utcnow()
        bm = BaseModel(id="345", created_at=dt.isoformat())
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)

    @unittest.skipIf(type(models.storage) is DBStorage, "Testing DBStorage")
    def test_save(self):
        """Test save method."""
        old = self.base.updated_at
        self.base.save()
        self.assertLess(old, self.base.updated_at)
        with open("file.json", "r") as f:
            self.assertIn("BaseModel.{}".format(self.base.id), f.read())

    def test_to_dict(self):
        """Test to_dict method."""
        base_dict = self.base.to_dict()
        self.assertEqual(dict, type(base_dict))
        self.assertEqual(self.base.id, base_dict["id"])
        self.assertEqual("BaseModel", base_dict["__class__"])
        self.assertEqual(self.base.created_at.isoformat(),
                         base_dict["created_at"])
        self.assertEqual(self.base.updated_at.isoformat(),
                         base_dict["updated_at"])
        self.assertEqual(base_dict.get("_sa_instance_state", None), None)

    @unittest.skipIf(type(models.storage) is DBStorage, "Testing DBStorage")
    def test_delete(self):
        """test delete"""
        self.base.delete()
        self.assertNotIn(self.base, FileStorage._FileStorage__objects)


if __name__ == "__main__":
    unittest.main()
