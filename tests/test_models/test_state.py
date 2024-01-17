#!/usr/bin/python3
"""Test module for the stae model"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from models import storage_type


class test_state(test_basemodel):
    """Test for state class """

    def __init__(self, *args, **kwargs):
        """Initializing for test class """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """test for the name attribute """
        new = self.value()
        if storage_type != 'db':
            self.assertEqual(type(new.name), str)
        else:
            self.assertEqual(type(new.name), str)
