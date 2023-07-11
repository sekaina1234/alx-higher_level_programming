#!/usr/bin/python3
"""Adds all arguments to a Python list
and saves them to a JSON file"""


import sys
from os import path
from importlib.machinery import SourceFileLoader

save_to_json_file = SourceFileLoader("save_to_json_file", 
        "./5-save_to_json_file.py").load_module().save_to_json_file
load_from_json_file = SourceFileLoader("load_from_json_file", 
        "./6-load_from_json_file.py").load_module().load_from_json_file
