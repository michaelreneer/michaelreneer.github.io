#!/usr/bin/env python

import os
import sys
sys.path.append(os.curdir)

from pelicanconf import *

# Basic
DELETE_OUTPUT_DIRECTORY = True
RELATIVE_URLS = False
SITEURL = 'http://michaelreneer.com'

# Feed
FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/all.atom.xml'

# Theming
GOOGLE_ANALYTICS = 'UA-36860769-1'
