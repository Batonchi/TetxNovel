import sys, time


from PyQt6.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow, QScrollArea, QWidget, QVBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl, QDir, QRect
from app.database import create_database
from PyQt6.QtGui import QIcon
from app.constant import *
import os

create_database()


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Boundless Abyss Adventure')

        self.view = QWebEngineView()
        self.loadPage()

        vbox = QVBoxLayout()
        vbox.addWidget(self.view)
        self.view.setFixedSize(1300, 1100)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)
        self.setStyleSheet('background-color: rgb(100, 0, 0);')
        self.qp = QPushButton(self)
        self.qp.clicked.connect(self.scroll_down)

    def loadPage(self):
        with open('static/html/preview.html', 'r') as f:
            html = f.read()
            self.view.setHtml(html)

    def scroll_down(self):
        self.view.page().runJavaScript('''
            window.scrollBy(0, 100)
                ''')




class Map(QMainWindow):
    pass


class StartPage(QMainWindow):
    pass


class EndPage(QMainWindow):
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
