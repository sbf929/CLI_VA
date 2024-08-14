""" Functions for handling different types of data for memory. """
import json

def add_to_list(value_list: list, new_value: str):
    """Adds `new_value` to a existing `value_list`."""

    if new_value.lower not in value_list:
        value_list.append(new_value)

def add_to_dict(dict_, key, value):
    """Adds new value """
    dict_[f'{key}'] = value

def save_in_database():
    "some"