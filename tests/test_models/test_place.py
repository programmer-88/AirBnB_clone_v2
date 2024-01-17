#!/usr/bin/python3
"""Test module for place """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models import storage_type


class test_Place(test_basemodel):
    """ test Place class"""

    def __init__(self, *args, **kwargs):
        """ init test class """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ tests city_id attribute"""
        new = self.value()
        if storage_type != 'db':
            self.assertEqual(type(new.city_id), str)
        else:
            self.assertEqual(type(new.city_id), type(None))

    def test_user_id(self):
        """ Test case for user_id attribute """
        new = self.value()
        if storage_type != 'db':
            self.assertEqual(type(new.user_id), str)
        else:
            self.assertEqual(type(new.user_id), type(None))

    def test_name(self):
        """ Test Case for name attribute """
        new = self.value()
        if storage_type != 'db':
            self.assertEqual(type(new.name), str)
        else:
            self.assertEqual(type(new.name), type(None))

    def test_description(self):
        """ Test case for description attribute """
        new = self.value()
        if storage_type != 'db':
            self.assertEqual(type(new.description), str)
        else:
            self.assertEqual(type(new.description), type(None))

    def test_number_rooms(self):
        """ test case for number_rooms attribute """
        new = self.value()
        if storage_type != 'db':
            self.assertEqual(type(new.number_rooms), int)
        else:
            self.assertEqual(type(new.number_rooms), type(None))

    def test_number_bathrooms(self):
        """ test case for number_bathrooms attribute """
        new = self.value()
        if storage_type != 'db':
            self.assertEqual(type(new.number_bathrooms), int)
        else:
            self.assertEqual(type(new.number_bathrooms), type(None))

    def test_max_guest(self):
        """ test case for max_guest attribute """
        new = self.value()
        if storage_type != 'db':
            self.assertEqual(type(new.max_guest), int)
        else:
            self.assertEqual(type(new.max_guest), type(None))

    def test_price_by_night(self):
        """ test case for price_by_night attribute """
        new = self.value()
        if storage_type != 'db':
            self.assertEqual(type(new.price_by_night), int)
        else:
            self.assertEqual(type(new.price_by_night), type(None))

    def test_latitude(self):
        """ test case for latitude attribute """
        new = self.value()
        if storage_type != 'db':
            self.assertEqual(type(new.latitude), float)
        else:
            self.assertEqual(type(new.latitude), type(None))

    def test_longitude(self):
        """ test case for longtitude attribute """
        new = self.value()
        if storage_type != 'db':
            self.assertEqual(type(new.longitude), float)
        else:
            self.assertEqual(type(new.longitude), type(None))

    def test_amenity_ids(self):
        """ test case for aminity_ids attribute """
        new = self.value()
        if storage_type != 'db':
            self.assertEqual(type(new.amenity_ids), list)
        else:
            self.assertEqual(type(new.amenity_ids), type(None))