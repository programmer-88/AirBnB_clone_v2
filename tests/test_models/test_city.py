#!/usr/bin/python3
"""Test module for city class """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models import storage_type


class test_City(test_basemodel):
    """test for city class """

    def __init__(self, *args, **kwargs):
        """initializing test class """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """test case for state_id """
        new = self.value()
        if storage_type == 'db':
            self.assertEqual(type(new.name), type(None))
        else:
            self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """test case for attribute name """
        new = self.value()
        if storage_type == 'db':
            self.assertEqual(type(new.name), type(None))
        else:
            self.assertEqual(type(new.name), str)
