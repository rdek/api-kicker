#! /usr/bin/env python3

import requests
import sys
import json
import argparse

# COMMAND LINE ARGUMENTS PARSER
## arguments help content formatter
class smartFormatter(argparse.HelpFormatter):
    def _split_lines(self, text, width):
        if text.startswith('R|'):
            return text[2:].splitlines()
        return argparse.HelpFormatter._split_lines(self, text, width)

## proper arguments definitions
parser = argparse.ArgumentParser(description="TESTOWY DESCRIPTION", formatter_class=smartFormatter)
parser.add_argument("-u", "--url", type=str, help="Target URL to check")
parser.add_argument("-f", "--file", type=str, help="File with targets urls to check")
parser.add_argument("-H", "--header", type=str, help='R|Header parameter, one per flag, e.g.:\n'
    '     /> python3 api-kicker.py -h "Host: example.com" -h "Content-Type: application/json"')
parser.add_argument("--headers", type=str, help="File with request headers, format - one under another")


arg = parser.parse_args()

class httpClient:
    
    def target(source):
        pass
pass
url = 'https://www.site.com/api/products/search?phrase=nonono'

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

