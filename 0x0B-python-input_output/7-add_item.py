#!/usr/bin/python3
"""add all arguments to a python list, and save to file"""
import sys
save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file

try:
    content = load_from_json("add_item.json")
except:
    content = []

argc = len(sys.argv)
for i in range(1, argc):
    content.append(sys.argv[i])
save_to_json(content, "add_item.json")
