#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/home/enigma/WEB/WEBFINAL/Final/app.py")

from config import app as application
