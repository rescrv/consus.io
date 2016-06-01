#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

################################# Site Metadata ################################

AUTHOR = 'Robert Escriva'
SITENAME = 'consus.io'
SITEURL = ''

TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT='%B %d, %Y'

#################################### Content ###################################

PATH = ''
PAGE_PATHS=['pages']
ARTICLE_PATHS=['posts']

WITH_FUTURE_DATES = False

FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

################################# Presentation #################################

THEME = './theme'
DIRECT_TEMPLATES = []

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

ARCHIVES_SAVE_AS = ''
ARTICLE_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''

#################################### Plugins ###################################

PLUGIN_PATHS = ['plugins']
PLUGINS = [
        'fixdatetime',
        'defaultunpublished',
        ]

MD_EXTENSIONS = [
        'markdown_include.include',
        ]

################################### No Feeds ###################################

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
