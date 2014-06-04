#!/usr/bin/env python

from __future__ import print_function
import requests
import html5lib
import sys
from html5lib import treebuilders
parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("lxml"))


def google_search(query):
    import urllib
    args = {'q': query,
            'v': '1.0',
            'start': 0,
            'rsz': 8,
            'safe': "off",
            'filter': 1,
            'hl': 'en'}
    data = requests.get('http://ajax.googleapis.com/ajax/services/search/web',
                        params=args).json()
    if 'responseStatus' not in data:
        return 'response does not have a responseStatus'
    if data['responseStatus'] != 200:
        return data.get('responseDetails', 'responseStatus is not 200')
    results = []
    if 'results' in data['responseData']:
        for result in data['responseData']['results']:
            results.append(urllib.unquote(result['unescapedUrl']))
    return results


query = 'stackoverflow ' + ' '.join(sys.argv[1:])
answer_xpath = ('.//{http://www.w3.org/1999/xhtml}div[@class="answer"]//'
                '{http://www.w3.org/1999/xhtml}div[@class="post-text"]')
stack_overflow_urls = google_search(query)
if isinstance(stack_overflow_urls, str):
    print(stack_overflow_urls)
    sys.exit(1)
print(stack_overflow_urls[0])
stack_overflow_html = requests.get(stack_overflow_urls[0]).text
stack_overflow_dom = parser.parse(stack_overflow_html)
first_answer = stack_overflow_dom.findall(answer_xpath)[0]
print(''.join([txt for txt in first_answer.itertext()]))
