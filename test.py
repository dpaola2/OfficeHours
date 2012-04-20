#! /usr/bin/env python

import sys, os, nose
from os.path import dirname, abspath
from pprint import pprint

PARENT_DIR = abspath('..')
sys.path.insert(0, PARENT_DIR)
pprint(sys.path)

from test.models import DayTest

nose.run()

