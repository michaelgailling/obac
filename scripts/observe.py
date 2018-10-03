import urllib.request as request
from html.parser import HTMLParser
import sys, os
import timeit
import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class ParseContent(HTMLParser):
    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


class HtmlScrape(request):
    def __init__(self, parent):
        url = ""
        hdr = {'User-Agent': 'metaprinter'}
        req = self.Request(url, headers=hdr)
        html = self.urlopen(req).read()

        html = html.decode("utf-8")