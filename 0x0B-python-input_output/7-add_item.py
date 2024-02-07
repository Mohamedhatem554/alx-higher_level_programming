#!/usr/bin/python3
"""7-add_item.py"""
import json
import os.path
import sys
from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
list_json = []

if os.path.exists(filename):
    list_json = load_from_json_file(filename)
for i in argv[1:]:
    list_json.append(i)
save_to_json_file(list_json, filename)