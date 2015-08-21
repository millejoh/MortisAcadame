#!python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'John Miller'
SITENAME = 'Mortis Acadame'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Central'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('IPython.org', 'http://ipython.org/'),
         ('Jupyter', 'http://jupyter.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/millejoh/'),)

DEFAULT_PAGINATION = 10

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["liquid_tags"]

# Theme
THEME = "themes/built-texts"
COLOPHON = True
COLOPHON_TITLE = 'Colophon'
COLOPHON_CONTENT = 'All education must begin with the premise that one day the student will die.'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
