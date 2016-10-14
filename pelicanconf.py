#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tang'
SITENAME = u"""<span style="color:black;">Tangmath</span> <span style="color:#AA1032;">Blog</span>"""
SITEURL = 'https://tqlsz.github.io'
#SITEURL = 'http://localhost:8000'
#AUTHOR = 'wonux'

TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {'en': '%b %d, %Y'}
DEFAULT_LANG = u'en'

DISQUS_SITENAME = 'tqlsz'

PLUGIN_PATHS = ["../pelican-plugins"]
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'liquid_tags.img', 'neighbors', 'related_posts', 'assets', 'share_post', 'multi_part']
MD_EXTENSIONS = ['codehilite(css_class=highlight,linenums=True)', 'extra', 'headerid', 'toc(permalink=true)', 'fenced_code', ]

SITEMAP = {
    'format': 'xml',
    'priorities': {
         'articles': 0.5,
         'indexes': 0.5,
         'pages': 0.5
     },
     'changefreqs': {
         'articles': 'monthly',
         'indexes': 'daily',
         'pages': 'monthly'
     }
}

# Appearance
THEME = '../pelican-elegant'
TYPOGRIFY = True
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_CATEGORY = 'Misc'
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = u'{slug}.html'
PAGE_URL = u'{slug}.html'
PAGE_SAVE_AS = u'{slug}.html'


# Feeds
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = 'feeds/%s.atom.xml'

# Social
SOCIAL = (
        ('Leetcode', 'https://leetcode.com/'),
        ('Github', 'https://github.com/tqlsz'),
        ('Coursera', 'https://zh.coursera.org/'),
        ('Email', 'mailto:349111840@qq.com'),
          )

# Elegant theme
STATIC_PATHS = ['theme/images', 'images']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
USE_SHORTCUT_ICONS = True

# Elegant Labels
SOCIAL_PROFILE_LABEL = u'Contact'
RELATED_POSTS_LABEL = 'Keep Reading'
SHARE_POST_INTRO = 'Share on:'
COMMENTS_INTRO = u'Comments Below:'

# Mailchimp
#EMAIL_SUBSCRIPTION_LABEL = u'Get Monthly Updates'
#EMAIL_FIELD_PLACEHOLDER = u'Enter your email...'
#SUBSCRIBE_BUTTON_TITLE = u'Send me Free updates'
#MAILCHIMP_FORM_ACTION = u'empty'

# SMO
TWITTER_USERNAME = u'wonux'
FEATURED_IMAGE = SITEURL + '/theme/images/apple-touch-icon-152x152.png'

# Legal
SITE_LICENSE = u'<span xmlns:dct="http://purl.org/dc/terms/" property="dct:title"> Tangmath Blog "</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/tqlsz" property="cc:attributionName" rel="cc:attributionURL">tang</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.'

# SEO
SITE_DESCRIPTION = u'My name is tangqinglong \u2016 a engineer in China SZ. I am tqlsz at Github. This is my personal blog.'

# Landing Page
PROJECTS = [
        {
            'name': 'Leetcode',
            'url':
            'https://leetcode.com/',
            'description': '算法题'},
        {
            'name': 'Github',
            'url':
            'https://github.com/tqlsz',
            'description': 'My open source project and code.'},
        {
            'name': 'Coursera',
            'url':
            'https://zh.coursera.org/', 
            'description': '优质课程'
            }]

LANDING_PAGE_ABOUT = {'title': '开源博客主站/Open Source Master',
        'details': """<div itemscope itemtype="http://schema.org/Person">
        <p>My name is <span itemprop="name">tang</span>. I am <a href="https://github.com/tqlsz/" title="My Github profile" itemprop="url"><span itemprop="nickname">tqlsz</span></a> at Github. You can also reach me via <a href="mailto:349111840@qq.com" title="My email address" itemprop="email">email</a>.</p></div>"""}

