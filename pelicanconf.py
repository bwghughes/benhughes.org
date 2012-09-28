#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Ben Hughes"
SITENAME = u"benhughes.org"
SITEURL = u'http://benhughes.org'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'
THEME = 'blog-template'
TYPOGRIFY = True
PLUGINS = ['pelican.plugins.sitemap',]
SITEMAP = {'format': 'xml'}
#GITHUB_ACTIVITY_FEED = "https://github.com/bwghughes.atom"

# Blogroll
LINKS = (('Susanne Madsen', 'http://www.susannemadsen.co.uk'),
        ('Bob Marshall', 'http://flowchainsensei.wordpress.com/'),
        ('Charles Leifer', 'http://charlesleifer.com'),
        ('Kenneth Reitz', 'http://kennethreitz.com'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/bwghughes'),)

STATIC_PATHS = ["images", "pictures"]
DEFAULT_PAGINATION = 5
