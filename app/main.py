import sys


from PyQt6.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow, QWidget, QVBoxLayout, QGridLayout, \
    QFormLayout, QGroupBox, QLineEdit, QTextBrowser
from PyQt6.QtWebEngineWidgets import QWebEngineView
from app.database import create_database
from app.gameSession.service import SessionService, generate_world_map
from app.players.service import Player, PlayerService
from app.gameSession.model import Session
from app.heroes.service import ExistCreature, ExistCreatureService
from app.insert_data_into_DB import update_info


create_database()
# update_info('/textFiles/Table items.docx')


class MainWindow(QMainWindow):
    pass


# страница входа в игру
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
        self.load_page()
        vbox = QVBoxLayout()
        vbox.addWidget(self.view)
        self.view.setFixedSize(1500, 1800)
        self.setContentsMargins(350, 200, 0, 0)
        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)
        self.player_name = QLineEdit('ИМЯ', self)
        self.player_name.resize(850, 50)
        self.player_name.move(500, 50)
        self.player_name.setStyleSheet('background-color: rgb(0, 0, 0); color: rgb(255, 255, 255); font-size: 22px; outline: none;')
        self.setStyleSheet('background-color: #540000;')
        self.start_btn.clicked.connect(self.start_session)

    def load_page(self):
        with open('static/html/START.png.html', 'r') as f:
            html = f.read()
            self.view.setHtml(html)

    # функция создающая или подгружающая игровую сессию
    def start_session(self):
        try:
            player_name = self.player_name.text()
            player_id = PlayerService.get_player_by_name(player_name)
            session = SessionService.get_session_by_player_id(player_id[0])
            self.return_page = Preview(session[0])
            self.return_page.show()
        except Exception as e:
            try:
                player_name = self.player_name.text()
                last_id = PlayerService.get_last_player_id()
                if not (last_id is None):
                    last_id = int(last_id[0]) + 1
                    PlayerService.register_player(Player(last_id,
                                                         player_name, 0, ''))
                else:
                    PlayerService.register_player(Player(1,
                                                         player_name, 0, ''))
                    last_id = 1
                hero = ExistCreatureService.get_first_creature()
                hero = ExistCreature(hero[0], hero[1], hero[2], hero[3], hero[4], hero[5], hero[6])
                SessionService.set_session(
                    Session(SessionService.get_last_session_id(), last_id, 1, str(hero)))

            except Exception as e:
                print(e)


# ИГровой пробник окно
class Preview(QMainWindow):
    def __init__(self, id_of_session: int):
        super().__init__()
        self.initUI()
        self.id_session = id_of_session

    def initUI(self):
        self.setWindowTitle('Boundless Abyss Adventure')

        self.view = QWebEngineView()
        self.load_page()
        vbox = QVBoxLayout()
        vbox.addWidget(self.view)
        self.view.setFixedSize(1300, 1100)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)
        self.setStyleSheet('background-color: rgb(0, 0, 0);')
        self.dialog = QPushButton(self)
        self.dialog.setStyleSheet('background-color: #6B3030;')
        self.dialog.move(1325, 10)
        self.dialog.resize(600, 200)
        self.dialog_text_browser = QTextBrowser(self)
        (self.dialog_text_browser
         .setStyleSheet('background-color: #6B3030; font-size: 30px; padding: 15px; color: #000000; border-radius: 10px'))
        self.dialog_text_browser.move(1325, 230)
        self.dialog_text_browser.setFixedSize(600, 700)
        self.user_text_browser = QTextBrowser(self)
        self.user_text_browser.setStyleSheet('background-color: #6B3030; font-size: 22px; padding: 15x; border-radius: 10px')
        self.user_text_browser.setFixedSize(600, 100)
        self.user_text_browser.move(1325, 950)
        self.dialog.clicked.connect(self.scroll_down)

    def load_page(self):
        with open('static/html/preview.html', 'r') as f:
            html = f.read()
            self.view.setHtml(html)

    def scroll_down(self):
        self.view.page().runJavaScript('''
            window.scrollBy(0, 100)
                ''')


# конечная страница позже здесь появиться рейтинг
class EndPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('To be continued')

        self.button = QPushButton('Return lobby', self)
        self.button.setStyleSheet(
            'background-color: #540000; color: gb(255, 255, 255)r; font-size: 30px; outline: none;')
        self.button.resize(1100, 100)
        self.button.move(350, 100)
        self.button.setContentsMargins(0, 0, 0, 0)
        self.view = QWebEngineView()
        self.load_page()
        vbox = QVBoxLayout()
        vbox.addWidget(self.view)
        self.view.setFixedSize(1500, 1800)
        self.setContentsMargins(350, 200, 0, 0)
        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)
        self.setStyleSheet('background-color: #540000;')
        self.button.clicked.connect(self.return_lobby)

    def load_page(self):
        with open('static/html/END.png.html', 'r') as f:
            html = f.read()
            self.view.setHtml(html)

    def return_lobby(self):
        try:
            return_page = StartPage()
            self.return_page = return_page
            self.return_page.show()
        except Exception as e:
            print(e)

# gланируется добавить еще окон реализующий боевку и гру с броском дайсов
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Preview(1)
    window.show()
    app.exec()
