#!/usr/bin/python3
"""Script: 7-add_item.py
Adds all command-line arguments to a
Python list and saves them to a file."""


import sys
from os import path
from typing import List
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

if path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list: List[str] = []

my_list.extend(sys.argv[1:])

save_to_json_file(my_list, filename)
