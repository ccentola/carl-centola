#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Carl Centola'
SITENAME = 'Carl Centola'
SITEURL = ''

THEME = 'theme'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'


STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Linkedin', '#'),
          ('Twitter', '#'),
          ('Github','#'),)

DEFAULT_PAGINATION = False

GOOGLE_ANALYTICS = 'UA-113866332-1'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
