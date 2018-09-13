#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Win10, Git for Windows Bash
# Python 3.5.2
# - lxml     4.2.4
# - requests 2.19.1

from lxml import html
import requests

# NOTE: magic
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

keyword = input('/?q=(keyword): ')

# HTML
#search = requests.get('https://ff5ch.syoboi.jp/?q={}'.format(keyword))

# XML RSS 2.0
# UnicodeEncodeError: 'cp932' codec can't encode character '\udc97' in position 39: illegal multibyte sequence
# NOTE: .encode('cp932', 'surrogateescape')
query = requests.get('https://ff5ch.syoboi.jp/?q={}&alt=rss'.format(keyword).encode('cp932', 'surrogateescape'))

search_result_tree = html.fromstring(query.content)

# Search Result
sr_thread_title = search_result_tree.xpath('//title/text()')
sr_thread_url = search_result_tree.xpath('//guid/text()')

#print('TITLE: ', sr_thread_title)
#print('URL: ', sr_thread_url)

for thread in sr_thread_url:
    page = requests.get(thread)
    tree = html.fromstring(page.content)

    title = tree.xpath('//title/text()')
    comment = tree.xpath('//html/body/div[1]/div[1]/ul[1]/li[1]/text()')

    #print('TITLE: ', title)
    #print('URL: ', thread)
    #print('COMMENT: ', comment)

    print('TITLE:', title, 'RES:', comment, 'URL:', thread)

    #print('TITLE: ', title)
