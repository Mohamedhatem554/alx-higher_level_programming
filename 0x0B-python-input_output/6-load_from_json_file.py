#!/usr/bin/python3
"""6-load_from_json_file.py"""
import json


def load_from_json_file(filename):
    """load from json file"""
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
