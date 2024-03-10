#!/usr/bin/python3
"""A module to model a place"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Place Model

    Description:
    Creates a new place which inherits from BaseModel
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    logitude = 0.0
    amenity_ids = []