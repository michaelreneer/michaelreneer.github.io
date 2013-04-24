#!/usr/bin/env python

# Basic
AUTHOR = 'Michael Kelly Reneer'
DESCRIPTION = ''
KEYWORDS = ''
LICENSE = '&copy; 2012 ' + AUTHOR + '.'
SITENAME = 'Michael Kelly Reneer'
SITEURL = 'http://localhost:8000'
TIMEZONE = 'America/New_York'

ARTICLE_EXCLUDES = (
    'extra',
    'images',
    'pages',
)
DIRECT_TEMPLATES = (
    'archives',
    'index',
    'projects',
)
EXTRA_TEMPLATES_PATHS = [
    'content/extra/templates',
]
FILES_TO_COPY = (
    # ('extra/icons/apple-touch-icon-114x114-precomposed.png',
    #     'apple-touch-icon-114x114-precomposed.png'),
    # ('extra/icons/apple-touch-icon-144x144-precomposed.png',
    #     'apple-touch-icon-144x144-precomposed.png'),
    # ('extra/icons/apple-touch-icon-57x57-precomposed.png',
    #     'apple-touch-icon-57x57-precomposed.png'),
    # ('extra/icons/apple-touch-icon-72x72-precomposed.png',
    #     'apple-touch-icon-72x72-precomposed.png'),
    # ('extra/icons/apple-touch-icon-precomposed.png',
    #     'apple-touch-icon-precomposed.png'),
    # ('extra/icons/apple-touch-icon.png', 'apple-touch-icon.png'),
    # ('extra/icons/favicon.ico', 'favicon.ico'),
    ('extra/robots.txt', 'robots.txt'),
)
MARKUP = (
    'markdown',
)
PLUGINS = [
    'pelican.plugins.assets',
    'pelican.plugins.sitemap',
]

ARCHIVES_SAVE_AS = 'blog/index.html'
ARTICLE_LANG_SAVE_AS = False
ARTICLE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{slug}/'
AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = False
PAGE_LANG_SAVE_AS = False
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PROJECTS_SAVE_AS = 'projects/index.html'
TAG_SAVE_AS = False

# Feed
CATEGORY_FEED_ATOM = None
FEED_ALL_ATOM = None

# Translations
TRANSLATION_FEED_ATOM = None

# Theming
DISQUS_SITENAME = 'michaelreneer'
MENUITEMS = (
    ('Blog', 'blog/'),
    ('Projects', 'projects/'),
    ('About', 'about/'),
)
SOCIAL = (
    ('Email', 'mailto:contact@michaelreneer.com'),
    ('GitHub', 'http://github.com/michaelreneer'),
    ('Twitter', 'http://twitter.com/michaelreneer'),
    ('Linkedin', 'http://www.linkedin.com/pub/michael-reneer/20/26/9a0/')
)
THEME = 'theme'
TWITTER_USERNAME = 'michaelreneer'

# Plugins
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}
