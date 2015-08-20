#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import urllib2
from flask import Flask
app = Flask(__name__)

HOSTNAME = 'thermopi.fritz.box'


urlfinder = re.compile("([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}|((news|telnet|nttp|file|http|ftp|https)://)|(www|ftp)[-A-Za-z0-9]*\\.)[-A-Za-z0-9\\.]+):[0-9]*)?/[-A-Za-z0-9_\\$\\.\\+\\!\\*\\(\\),;:@&=\\?/~\\#\\%]*[^]'\\.}>\\),\\\"]")

def urlify2(value):
    return urlfinder.sub(r'<a href="\1">\1</a>', value)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    response = urllib2.urlopen(path)
    html = response.read()
    
    
    html = urlify2(html)

    pos = html.find('"/')
    print(html[pos:pos+100])

    result = 'webvpn :: %s ::' % path
    result += html.decode('utf-8')
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
