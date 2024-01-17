#!/usr/bin/python3
"""Test module for Review model """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from models import storage_type


class test_review(test_basemodel):
    """ Review Test Class"""

    def __init__(self, *args, **kwargs):
        """ Initialise review test class"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ test case for place_id attribute"""
        new = self.value()
        if storage_type != 'db':
            self.assertEqual(type(new.place_id), str)
        else:
            self.assertEqual(type(new.place_id), type(None))

    def test_user_id(self):
        """ test case for user_id attribute"""
        new = self.value()
        if storage_type != 'db':
            self.assertEqual(type(new.user_id), str)
        else:
            self.assertEqual(type(new.user_id), type(None))

    def test_text(self):
        """ test case for text attribute"""
        new = self.value()
        if storage_type != 'db':
            self.assertEqual(type(new.text), str)
        else:
            self.assertEqual(type(new.text), type(None))