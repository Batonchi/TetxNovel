import sys

from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QPushButton, QGridLayout, QLabel
from PyQt6.QtWebEngineWidgets import QWebEngineView
from app.database import create_database



create_database()

# app = QApplication(sys.argv)
# view = QWebEngineView()
#
#
# url = QUrl.fromLocalFile('/view/static/error.html')
# view.load(url)
#
# view.show()
# app.exec()