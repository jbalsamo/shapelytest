#!/usr/bin/python
import json
import shapely

cur_objects = json.loads(open('curations.json').read())

print cur_objects[1]["geometry"]
