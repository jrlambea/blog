#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'J.R. Lambea'
SITENAME = 'J.R. Blog'
SITEURL = 'https://jrlambea.me'
SITESUBTITLE = 'SysAdmin | Security Operations | Cloud Infrastructure'

PATH = 'content'

TIMEZONE = 'Europe/Andorra'

DEFAULT_LANG = 'ES'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/jrlambea'),
          ('linkedin', 'https://www.linkedin.com/in/jrlambea/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/Flex'

# Flex specific settings
STATIC_PATHS = ['img']
PYGMENTS_STYLE = 'monokai'
THEME_COLOR = 'dark'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

PYGMENTS_STYLE = 'emacs'
PYGMENTS_STYLE_DARK = 'monokai'
DISQUS_SITENAME = 'blog-ecg5wppj8o'

COPYRIGHT_NAME = 'J. R. Lambea'
COPYRIGHT_YEAR = '2020'
GITHUB_CORNER_URL = 'https://github.com/jrlambea/blog/'
