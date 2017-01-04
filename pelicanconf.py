#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mike Clymer'
HIDE_AUTHORS = True
SITENAME = 'My So-Called Effective Theory'
SITEURL = 'http://mikeclymer.github.io' # Intentionally left blank, see ./publishconf.py

PATH = 'content'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
ARTICLE_LANG_URL = 'posts/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL

LINKS = (('Fedscape', 'http://fedscape.com/'),)

# Social widget
# SOCIAL = (('Github', 'https://github.com/mikeclymer'),
#           ('LinkedIn', 'https://www.linkedin.com/in/mikeclymer'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['extras', 'images']
EXTRA_PATH_METADATA = {
    'extras/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'extras/android-chrome-512x512.png': {'path': 'android-chrome-512x512.png'},
    'extras/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extras/browserconfig.xml': {'path': 'browserconfig.xml'},
    'extras/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extras/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/manifest.json': {'path': 'manifest.json'},
    'extras/mstile-150x150.png': {'path': 'mstile-150x150.png'},
    'extras/safari-pinned-tab.svg': {'path': 'safari-pinned-tab.svg'},
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup', 'pelican-bootstrapify']

BOOTSTRAPIFY = {
    'table': ['table', 'table-striped', 'table-hover'],
    'img': ['img-fluid'],
    'blockquote': ['blockquote'],
}

# Theme settings --------------------------------------------------------------
THEME = 'themes/pelican-alchemy/alchemy'

# SITESUBTITLE = 'A magical \u2728 Pelican theme'
SITEIMAGE = '/images/happy_place.jpg width=200 height=200'
# DESCRIPTION = 'A functional, clean, responsive theme for Pelican. Heavily ' \
#               'inspired by crowsfoot and clean-blog, powered by Bootstrap.'

ICONS = [
    ('github', 'https://github.com/mikeclymer'),
    ('linkedin-square', 'https://www.linkedin.com/in/mikeclymer'),
    ('stack-overflow', 'http://stackoverflow.com/users/551818/mike-clymer'),
]

PYGMENTS_STYLE = 'friendly'
RFG_FAVICONS = True

# Default value is ['index', 'tags', 'categories', 'authors', 'archives']
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'archives', 'sitemap']
SITEMAP_SAVE_AS = 'sitemap.xml'
