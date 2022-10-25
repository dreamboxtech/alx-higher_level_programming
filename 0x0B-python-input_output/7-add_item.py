#!/usr/bin/python3
"""a script that adds all arguments to a Python list,
and then save them to a file:"""
import json
import sys
import os

args = sys.argv[1:]
filename = "add_item.json"

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.isfile(filename):
    lst = load_from_json_file(filename)
else:
    lst = []
lst.extend(args)

save_to_json_file(lst, filename)
