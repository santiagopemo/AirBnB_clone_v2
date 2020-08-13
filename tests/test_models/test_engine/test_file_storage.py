#!/usr/bin/python3
""" Module for testing file storage"""
from models import storage
import os
from models.place import Place
import unittest
from sqlalchemy.orm.collections import InstrumentedList
from datetime import datetime
import models
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
import os
import pep8
from models.review import Review
from time import sleep
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
NoneType = type(None)


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

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
        """ Set up test environment """
        # del_list = []
        # for key in storage._FileStorage__objects.keys():
        #     del_list.append(key)
        # for key in del_list:
        #     del storage._FileStorage__objects[key]
        pass

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        FileStorage._FileStorage__objects = {}
        fs = FileStorage()
        self.assertEqual(len(fs.all()), 0)

    @unittest.skipIf(type(models.storage) is DBStorage, "Filestorage")
    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    @unittest.skipIf(type(models.storage) is DBStorage, "Filestorage")
    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    @unittest.skipIf(type(models.storage) is DBStorage, "Filestorage")
    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    @unittest.skipIf(type(models.storage) is DBStorage, "Filestorage")
    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    @unittest.skipIf(type(models.storage) is DBStorage, "Filestorage")
    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    @unittest.skipIf(type(models.storage) is DBStorage, "Filestorage")
    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    @unittest.skipIf(type(models.storage) is DBStorage, "Filestorage")
    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    @unittest.skipIf(type(models.storage) is DBStorage, "Filestorage")
    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    @unittest.skipIf(type(models.storage) is DBStorage, "Filestorage")
    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    @unittest.skipIf(type(models.storage) is DBStorage, "Filestorage")
    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)

    def test_pep8_FileStorage(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """Check for docstrings."""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)
        self.assertIsNotNone(FileStorage.delete.__doc__)

    def test_attributes(self):
        """Check for attributes."""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_methods(self):
        """Check for methods."""
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertTrue(hasattr(FileStorage, "reload"))
        self.assertTrue(hasattr(FileStorage, "delete"))

    def test_methods(self):
        """Check for methods."""
        fs = FileStorage()
        self.assertTrue(hasattr(fs, "all"))
        self.assertTrue(hasattr(fs, "new"))
        self.assertTrue(hasattr(fs, "reload"))
        self.assertTrue(hasattr(fs, "delete"))

    def test_init(self):
        """Test initialization."""
        fs = FileStorage()
        self.assertTrue(isinstance(fs, FileStorage))

    def test_all(self):
        """Test default all method."""
        fs = FileStorage()
        bm = BaseModel()
        fs.new(bm)
        am = Amenity()
        fs.new(am)
        ct = City()
        fs.new(ct)
        us = User()
        fs.new(us)
        pl = Place()
        fs.new(pl)
        st = State()
        fs.new(st)
        rv = Review()
        fs.new(rv)
        objs = fs.all()
        self.assertEqual(type(objs), dict)
        self.assertIs(objs, FileStorage._FileStorage__objects)
        self.assertTrue(len(objs) >= 7)

    def test_all_cls(self):
        """Test all method with specified cls."""
        FileStorage._FileStorage__objects = {}
        fs = FileStorage()
        st = State()
        fs.new(st)
        obj = fs.all(State)
        self.assertEqual(type(obj), dict)
        self.assertEqual(len(obj), 1)
        self.assertEqual(st, list(obj.values())[0])

    @unittest.skipIf(type(models.storage) is DBStorage, "Filestorage")
    def test_new(self):
        """Test new method."""
        fs = FileStorage()
        bm = BaseModel()
        bm.save()
        store = fs.all()
        self.assertIn("BaseModel." + bm.id, store.keys())
        self.assertIn(bm, store.values())

    def test_save(self):
        """Test save method."""
        fs = FileStorage()
        bm = BaseModel()
        fs.new(bm)
        am = Amenity()
        fs.new(am)
        ct = City()
        fs.new(ct)
        us = User()
        fs.new(us)
        pl = Place()
        fs.new(pl)
        st = State()
        fs.new(st)
        rv = Review()
        fs.new(rv)
        fs.save()
        with open("file.json", "r", encoding="utf-8") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + ct.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + rv.id, save_text)

    def test_reload(self):
        """Test reload method."""
        fs = FileStorage()
        bm = BaseModel()
        with open("file.json", "w", encoding="utf-8") as f:
            key = "{}.{}".format(type(bm).__name__, bm.id)
            json.dump({key: bm.to_dict()}, f)
        fs.reload()
        store = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, store)

    def test_delete(self):
        """Test delete method."""
        fs = FileStorage()
        bm = BaseModel()
        key = "{}.{}".format(type(bm).__name__, bm.id)
        FileStorage._FileStorage__objects[key] = bm
        fs.delete(bm)
        self.assertNotIn(bm, FileStorage._FileStorage__objects)

if __name__ == "__main__":
    unittest.main()
