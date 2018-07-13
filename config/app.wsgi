#!/usr/bin/python
import os
import sys

path = "/home/pato"

if path not in sys.path:
	sys.path.append(path)

from blog import app as application

activate_this = '/home/pato/blog/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

