#!/usr/bin/python3
""" test review file """
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
from models.review import Review
from tests.test_models.test_base_model import TestBaseModel
from time import sleep
NoneType = type(None)


class TestReview(unittest.TestCase):
    '''
        Testing Review class
    '''

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

    def test_Review_inheritance(self):
        '''
            tests that the Review class Inherits from BaseModel
        '''
        new_review = Review()
        self.assertIsInstance(new_review, BaseModel)

    def test_Review_attributes(self):
        '''
            Test that Review class has place_id, user_id and text
            attributes.
        '''
        new_review = Review()
        self.assertTrue("place_id" in new_review.__dir__())
        self.assertTrue("user_id" in new_review.__dir__())
        self.assertTrue("text" in new_review.__dir__())

    def test_Review_attributes(self):
        '''
            Test that Review class has place_id, user_id and text
            attributes.
        '''
        new_review = Review()
        place_id = getattr(new_review, "place_id")
        user_id = getattr(new_review, "user_id")
        text = getattr(new_review, "text")
        self.assertIsInstance(place_id, NoneType)
        self.assertIsInstance(user_id, NoneType)
        self.assertIsInstance(text, NoneType)

    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/review.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """Check for docstrings."""
        self.assertIsNotNone(Review.__doc__)

    @unittest.skipIf(type(models.storage) is DBStorage, "Filestorage")
    def test_save_Review(self):
        """test if the save works"""
        new_review = Review()
        sleep(0.6)
        new_review.save()
        self.assertNotEqual(new_review.created_at, new_review.updated_at)

    def test_to_dict(self):
        """Test to_dict method."""
        new_review = Review()
        review_dict = new_review.to_dict()
        self.assertEqual(dict, type(review_dict))
        self.assertEqual(new_review.id, review_dict["id"])
        self.assertEqual("Review", review_dict["__class__"])
        self.assertEqual(new_review.created_at.isoformat(),
                         review_dict["created_at"])
        self.assertEqual(new_review.updated_at.isoformat(),
                         review_dict["updated_at"])


if __name__ == "__main__":
    unittest.main(defaultTest="TestBaseModel", exit=False)
