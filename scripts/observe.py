import urllib.request as request    # Default python version 3.6
from html.parser import HTMLParser  # 
import sys, os
import timeit

# The following imports require using the pip install command in the command prompt
# please ensure your path variable contains the path to your python installation
#---------------------------------------------------------------------------------------------
# should your path be assigned to an older version of python you must reset it
# to the version 3.6 installation directory, neglecting this step will result in errors

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class ParseContent(HTMLParser):
    def error(self, message):
        pass

    # Overridable -- finish processing of start+end tag: <tag.../>
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    # Overridable -- handle start tag
    def handle_starttag(self, tag, attrs):
        pass

    # Overridable -- handle end tag
    def handle_endtag(self, tag):
        pass

    # Overridable -- handle character reference
    def handle_charref(self, name):
        pass

    # Overridable -- handle entity reference
    def handle_entityref(self, name):
        pass

    # Overridable -- handle data
    def handle_data(self, data):
        pass

    # Overridable -- handle comment
    def handle_comment(self, data):
        pass

    # Overridable -- handle declaration
    def handle_decl(self, decl):
        pass

    # Overridable -- handle processing instruction
    def handle_pi(self, data):
        pass


class HtmlScrape:
    def __init__(self, parent=None, url="", header={'User-Agent': 'metaprinter'}):
        parser = ParseContent()
        self.url = url
        self.header = header
        req = request.Request(self.url, headers=self.header)
        html = request.urlopen(req).read()

        self.html = html.decode("utf-8")


class IVWebView(QWebEngineView):
    def __init__(self, parent=None):
        super(IVWebView, self).__init__(parent)
        self.setUpdatesEnabled(True)


class InfoView(QFrame):
    def __init__(self, parent=None):
        super(InfoView, self).__init__(parent)

        # self.scraper = HtmlScrape(parent=self, url="http://www.reddit.com")
        # print(self.scraper.html)

        self.IVWV = IVWebView(parent=self)
        self.page = QWebEnginePage()
        self.page.setUrl(QUrl("http://www.google.com"))
        self.IVWV.setPage(self.page)

        self.browser_layout = QHBoxLayout()
        self.browser_layout.addWidget(self.IVWV)
        self.source_layout = QHBoxLayout()
        self.main_layout = QVBoxLayout()

        self.main_layout.addLayout(self.browser_layout)
        self.main_layout.addLayout(self.source_layout)
        self.setLayout(self.main_layout)

    def handle_html(self, *argv):
        print(argv)
    
    def extract_html(self):
        self.page.toHtml(self.HandleHtml)


class IVTabs(QTabWidget):
    def __init__(self, parent=None):
        super(IVTabs, self).__init__(parent)

    def new_tab(self):
        self.addTab(InfoView(), "Tab " + str(self.count() + 1))
        self.setCurrentIndex(self.count() - 1)

    def close_tab(self):
        self.removeTab(self.currentIndex())


class AppWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AppWindow, self).__init__(parent)
        self.title = 'obac'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 400
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.IVT = IVTabs(parent=self)
        self.setCentralWidget(self.IVT)
        self.initUI()

    def initUI(self):
        main_menu = self.menuBar()

        file_menu = main_menu.addMenu('File')

        new_tab_button = QAction(QIcon('exit24.png'), 'New Tab', self)
        new_tab_button.setShortcut('Ctrl+T')
        new_tab_button.triggered.connect(self.IVT.new_tab)
        file_menu.addAction(new_tab_button)

        close_tab_button = QAction(QIcon('exit24.png'), 'Close Tab', self)
        close_tab_button.setShortcut('Ctrl+Alt+T')
        close_tab_button.triggered.connect(self.IVT.close_tab)
        file_menu.addAction(close_tab_button)

        exit_button = QAction(QIcon('exit24.png'), 'Exit', self)
        exit_button.setShortcut('Ctrl+Q')
        exit_button.setStatusTip('Exit application')
        exit_button.triggered.connect(self.close)
        file_menu.addAction(exit_button)

        self.IVT.new_tab()
        self.show()


if __name__ == "__main__":
    qApp = QApplication(sys.argv)
    aw = AppWindow()
    aw.show()
    sys.exit(qApp.exec_())
