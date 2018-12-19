#! /usr/bin/env python

import requests
import sys
import json

url = 'https://www.g2a.com/new/api/products/search?phrase=nonono'

# host = 'www.g2a.com'
# userAgent = 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0'
# accept = '*/*'
# acceptLanguage = 'en-US,en;q=0.5'
# acceptEncoding = 'gzip, deflate'
# cacheControl = 'no-cache'
# pragma = 'no-cache'
# contentType = 'application/json'

headers = {
        'Host': 'www.g2a.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; ev:52.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache'
        }

payloads = {
        'someData': 'someDataValue',
        'anotherData': 'anotherDataValue'
        }

l

