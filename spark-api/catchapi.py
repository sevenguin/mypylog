# -*-coding:utf-8 -*-
#python 3.5

import urllib.request
import os
from html.parser import HTMLParser

base = 'http://spark.apache.org/docs/latest/api/python/'
index_url = '%sindex.html' % base

class YbHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = {}
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            if len(attrs) == 2:
                if attrs[0] == ('class', 'reference internal'):
                    h, v = attrs[1]
                    if v.find('#') < 0:
                        self.links[v] = '%s%s' % (base, v)

def saveToFile(path, name, data):
    if not os.path.exists(path):
        os.mkdir(path)
    f = open(path.strip(os.sep) + os.sep + name, 'w+')
    f.write(data)

def readFromUrl(url):
    r = urllib.request.urlopen(url)
    return r.read().decode('gbk')

if __name__ == '__main__'():
    dirpath = "D:\pysparkapi"
    d = readFromUrl(index_url)
    saveToFile(dirpath, "index.html", d)

    parser = YbHTMLParser()
    parser.feed(d)

    for k in parser.links.keys():
        d = readFromUrl(parser.links[k])
        saveToFile(dirpath, k, d)
