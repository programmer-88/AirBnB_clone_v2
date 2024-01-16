#!/usr/bin/python3
"""Test case for class Amenity """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models import storage_type


class test_Amenity(test_basemodel):
    """Amenity class test """

    def __init__(self, *args, **kwargs):
        """Start amenity class test"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ test for name attribute"""
        new = self.value()
        if storage_type == 'db':
            self.assertEqual(type(new.name), type(None))
        else:
            self.assertEqual(type(new.name), str)
