#!/usr/bin/python3
"""Test module for the user model """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from models import storage_type

class test_User(test_basemodel):
    """Test for user class"""

    def __init__(self, *args, **kwargs):
        """ Initializing user test class"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ test case for first_name attribute"""
        new = self.value()
        if storage_type != 'db':
            self.assertEqual(type(new.first_name), str)
        else:
            self.assertEqual(type(new.first_name), type(None))

    def test_last_name(self):
        """ test case for last_name attribute"""
        new = self.value()
        if storage_type != 'db':
            self.assertEqual(type(new.last_name), str)
        else:
            self.assertEqual(type(new.last_name), type(None))

    def test_email(self):
        """ test case for email attribute"""
        new = self.value()
        if storage_type != 'db':
            self.assertEqual(type(new.email), str)
        else:
            self.assertEqual(type(new.email), type(None))

    def test_password(self):
        """ test case for password attribute"""
        new = self.value()
        if storage_type != 'db':
            self.assertEqual(type(new.password), str)
        else:
            self.assertEqual(type(new.password), type(None))