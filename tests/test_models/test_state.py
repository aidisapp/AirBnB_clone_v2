#!/usr/bin/python3
"""Module for state model test"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """
    Test cases for the state model
    Inherits from base model test
    """

    def __init__(self, *args, **kwargs):
        """test for the constructor initialization"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """test for the name attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)
