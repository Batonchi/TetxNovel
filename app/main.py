import sys


from PyQt6.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow, QWidget, QVBoxLayout, QGridLayout, \
    QFormLayout, QGroupBox, QLineEdit
from PyQt6.QtWebEngineWidgets import QWebEngineView
from app.database import create_database
from app.gameSession.service import SessionService
from app.players.model import Player
from app.gameSession.model import Session


create_database()


class MainWindow(QMainWindow):

    def __init__(self, id_of_session: int):
        super().__init__()
        self.initUI()
        self.id_session = id_of_session

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
        self.setStyleSheet('background-color: rgb(0, 0, 0);')
        self.dialog = QPushButton(self)
        self.dialog.setStyleSheet('background-color: rgb(100, 0, 0);')
        self.dialog.move(1325, 20)
        self.dialog.resize(600, 200)

        #создание статус окошка
        #создание группы виджетов
        formLayot = QFormLayout()
        groupBox = QGroupBox()
        self.player = 0


    def loadPage(self):
        with open('static/html/preview.html', 'r') as f:
            html = f.read()
            self.view.setHtml(html)

    def scroll_down(self):
        self.view.page().runJavaScript('''
            window.scrollBy(0, 100)
                ''')


class StartPage(QMainWindow):


    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('Welcome to My GAme')

        self.start_btn = QPushButton('Начать игру', self)
        self.start_btn.setStyleSheet('background-color: #540000; color: gb(255, 255, 255)r; font-size: 30px; outline: none;')
        self.start_btn.resize(1100, 100)
        self.start_btn.move(350, 100)
        self.start_btn.setContentsMargins(0, 0, 0, 0)
        self.view = QWebEngineView()
        self.loadPage()
        vbox = QVBoxLayout()
        vbox.addWidget(self.view)
        self.view.setFixedSize(1500, 1800)
        self.setContentsMargins(350, 200, 0, 0)
        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)
        self.player_name = QLineEdit('ИМЯ', self)
        self.player_name.resize(300, 50)
        self.player_name.move(500, 50)
        self.player_name.setStyleSheet('background-color: rgb(0, 0, 0); color: rgb(255, 255, 255); font-size: 22px; outline: none;')
        self.setStyleSheet('background-color: #540000;')


    def loadPage(self):
        with open('static/html/START.png.html', 'r') as f:
            html = f.read()
            self.view.setHtml(html)

    def start_session(self):
        try:
            session_service = SessionService()
            session = session_service.get_session_by_player_name(self.player_name.text())
            if session:
                pass
            else:
                pass
        except Exception as e:
            print(e)



class Preview(QMainWindow):
    pass


class EndPage(QMainWindow):
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StartPage()
    window.show()
    app.exec()
