#!/usr/bin/python3
"""Test case for base-model class"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
from models import storage_type


@unittest.skipIf(storage_type == 'db', 'test not supported')
class test_basemodel(unittest.TestCase):
    """test class for BaseModel class"""

    def __init__(self, *args, **kwargs):
        """ init the BaseModel test class"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ set up method to be executed before each test case """
        pass

    def tearDown(self):
        """ tear down method to be executed after each test case """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_init(self):
        """Tests init method of the BaseModel class."""
        self.assertIsInstance(self.value(), BaseModel)

    def test_default(self):
        """ default tests of BaseModel """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ tests BaseModel by using kwargs """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ tests BaseModel by using int kwargs"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ tests the str method of BaseModel"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ tests to_dict method od BaseModel"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ tests with None kwargs"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ tests by using kwargs with one argument"""
        n = {'name': 'test'}
        new = self.value(**n)
        self.assertEqual(new.name, n['name'])

    def test_id(self):
        """ tests id attribute of BaseModel """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ tests create_at attribute of BaseModel"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ tests updated_at attribute of BaseModel"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

