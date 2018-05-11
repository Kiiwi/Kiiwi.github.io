#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = 'Tommy Ryan'
SITENAME = 'Data Science Dummy'
SITEURL = 'https://kiiwi.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

# Theme
THEME = 'MinimalXY'

# Theme customizations
MINIMALXY_CUSTOM_CSS = 'static/css/custom.css'
MINIMALXY_START_YEAR = 2018
MINIMALXY_CURRENT_YEAR = date.today().year

# Author
AUTHOR_INTRO = u'Hello world! I’m Tommy Ryan. Here I will post about my dive into the depths of data science.'
AUTHOR_DESCRIPTION = u'I\'m Tommy Ryan. I\'m interested in physics, astronomy and computer science. You will currently find me in Oslo.'
AUTHOR_AVATAR = 'theme/images/avatar2.png'
AUTHOR_WEB = 'http://www.linkedin.com/in/tommy-ryan'

# Social
SOCIAL = (
    ('github', 'https://github.com/kiiwi'),
    ('linkedin', 'http://www.linkedin.com/in/tommy-ryan'),
)

# Pretty URLs
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_URL = '{slug}'

# Ignore Notebook checkpoints
IGNORE_FILES = ['.ipynb_checkpoints']
