#! /usr/bin/env python3

import requests
import sys
import json
import argparse

# COMMAND LINE ARGUMENTS PARSER
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="Target URL to check")
parser.add_argument("-f", "--file", help="File with targets urls to check")
parser.add_argument("-h", "--header", help="Header parameter, one per flag. 
        E.g.: -h "Host: example.com" -h "Content-Type: application/json"")
parser.add_argument("-H", "--headers", help="File with request headers, format - one under another")


args = parser.parse_args()

class httpClient:
    
    def target(source)
pass
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

