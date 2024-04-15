#!/usr/bin/python3
"""Module for the user model tests"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """
    test cases for the user model
    inherits from the test base model
    """

    def __init__(self, *args, **kwargs):
        """test for the constructor initialization"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """test for first name attribute"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """test for last name attribute"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """test for email attribute"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """test for password attribute"""
        new = self.value()
        self.assertEqual(type(new.password), str)
