#!/usr/bin/python3
"""
This module defines a function that adds all arguments to a Python list
then saves them to a file
"""


import sys
save_to_json_file = _import_('5-save_to_json_file').save_to_json_file
import_module = _import_('6-load_from_json_file')
load_from_json_file = import_module.load_from_json_file


file_name = "add_item.json"
my_list = []

try:
    my_list = load_from_json_file(file_name)
except Exception as e:
    pass

for f in range(1, len(sys.argv)):
    my_list.append(sys.argv[f])

save_to_json_file(my_list, file_name)
