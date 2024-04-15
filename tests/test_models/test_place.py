#!/usr/bin/python3
"""Test Module for the place model"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Test for place model"""

    def __init__(self, *args, **kwargs):
        """Test for the initialisation of the place model"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Test for the city_id attribute (foreign key)"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """test for the user_id attribute (foreign key)"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """test for the name attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """test for the description attribute"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """test for number of rooms attribute"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """test for number of bathrooms attribute"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """test for max guest attribute"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """test for price attribute"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """test for address map marker (latitude)"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """test for address map marker (longitude)"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """test for amenities id (foreign key)"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
