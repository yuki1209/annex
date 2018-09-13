#!/usr/bin/env python

import requests

# HTML
# url = 'https://ff5ch.syoboi.jp/?q=test'

# XML RSS 2.0
url = 'https://ff5ch.syoboi.jp/?q=test&alt=rss'

response = requests.get(url)

print(response)

print(type(response))

# url
print('url:', response.url)

# status_code
print('status_code:', response.status_code)

# headers
print('headers:', response.headers)

# encoding
print('encoding:', response.encoding)

#print(response.text)
#print(response.text.encode('utf-8', 'surrogateescape'))
#print(response.text.encode('cp932', 'surrogateescape'))
