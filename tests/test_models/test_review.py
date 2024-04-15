#!/usr/bin/python3
"""Module for the review model tests"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """
    Test the review model.
    Inherit from the base mode test
    """

    def __init__(self, *args, **kwargs):
        """Test for initialization of constructors"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """test for place id (foreign key)"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """test for user id (foreign key)"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """test for the review text (description)"""
        new = self.value()
        self.assertEqual(type(new.text), str)
