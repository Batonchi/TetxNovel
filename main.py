import os
import sqlite3
import sys


from insert_data_into_DB import *
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QTextBrowser
from PyQt6.QtWebEngineWidgets import QWebEngineView
from database import create_database, get_connection
from app.gameSession.service import SessionService, Session
from app.players.service import PlayerService, Player
from app.heroes.service import ExistCreatureService
from insert_data_into_DB import update_info
from constant import PATH


create_database()
try:
    with get_connection(PATH) as conn:
        if conn.cursor().execute('''SELECT * FROM items WHERE id = 1''').fetchone() is None:
            raise Exception('hernya')
except Exception as error:
    print(error)
    try:
        data = open(os.path.join(os.getcwd(), 'app\\textFiles\\start-data.txt'), 'r', encoding='utf-8')
        update_info(data.read())
    except Exception as er:
        print(er)


# страница основного игрового процесса
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
        self.start_btn.resize(550, 100)
        self.start_btn.move(900, 100)
        self.start_btn.setContentsMargins(0, 0, 0, 0)
        self.open_editor_window_btn = QPushButton('Перейти в окно редактора', self)
        self.open_editor_window_btn.setStyleSheet('background-color: #540000; color: gb(255, 255, 255)r; font-size: 30px; outline: none;')
        self.open_editor_window_btn.resize(550, 100)
        self.open_editor_window_btn.move(350, 100)
        self.open_editor_window_btn.setContentsMargins(0, 0, 0, 0)

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
        self.open_editor_window_btn.clicked.connect(self.return_to_editor_window)

    # более приятный и отслеживаемый процесс загрузки страницы HTML
    def load_page(self):
        path = os.path.abspath('app\\static\\START.png.html')
        with open(path, 'r') as f:
            self.view.setHtml(f.read())

    # функция создающая или подгружающая игровую сессию
    def start_session(self):
        try:
            player_name = self.player_name.text()
            player = PlayerService.get_player_by_name(player_name)
            session = SessionService.get_session_by_player_id(player.player_id)
            if int(session.checkpoint) >= 10:
                # здесь будет бросать в основное окно Main Window, когда я его
                # сделаю, пока что только диалоговое окно о прохождении
                class CustomEndDialog(QDialog):
                    def __init__(self):
                        super().__init__()
                        self.setWindowTitle('Поздравляю!')

                        message = QLabel(f'''ПРиятно видеть человека прошедшего вводную часть моей игры! Спасибо.
                        На данный момент это конец, но скоро здесь появитья продолжение.''')
                        layout = QVBoxLayout()
                        layout.addWidget(message)
                        self.setLayout(layout)

                custom_end_dialog = CustomEndDialog()
                custom_end_dialog.exec()
            else:
                self.return_page = Preview(session.game_session_id)
                self.return_page.show()
        except Exception as e:
            print(e)
            try:
                player_name = self.player_name.text()
                if PlayerService.get_player_by_name(player_name) is None:
                    PlayerService.register_player(Player(player_name, 0, ''))
                player = PlayerService.get_player_by_name(player_name)
                hero = ExistCreatureService.get_first_creature()
                SessionService.set_session(
                    Session(player.player_id, 1, str(hero)))
                session = SessionService.get_session_by_player_id(player.player_id)
                self.return_page = Preview(session.game_session_id)
                self.return_page.show()
            except Exception as e:
                print(e)

    def return_to_editor_window(self):
        try:
            self.return_page = CreateInsertDBDAta()
            self.return_page.show()
        except Exception as e:
            print(e)


# ИГровой пробник окно
class Preview(QMainWindow):
    def __init__(self, id_of_session: int):
        super().__init__()
        self.initUI(id_of_session)
        self.id_of_session = id_of_session

    def initUI(self, id_of_session):
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
        self.dialog_name_region_text_browser = QTextBrowser(self)
        self.dialog_name_region_text_browser.move(1325, 220)
        self.dialog_name_region_text_browser.resize(600, 70)
        self.dialog_name_region_text_browser.setStyleSheet('background-color: rgb(100, 0, 0); border-radius: 10px;'
                                                           ' color: rgb(255, 255, 255); padding: 15px; font-size: 30px;')
        self.dialog_text_browser = QTextBrowser(self)
        (self.dialog_text_browser
         .setStyleSheet('background-color: #6B3030; font-size: 30px;'
                        'padding: 15px; color: #ffffff; border-radius: 10px'))
        self.dialog_text_browser.move(1325, 300)
        self.dialog_text_browser.setFixedSize(600, 750)
        self.dialog.clicked.connect(self.scroll_down_history)
        self.dialog_stack = []

    # более приятный и отслеживаемый процесс загрузки страницы HTML
    def load_page(self):
        path = os.path.abspath('app\\static\\preview.html')
        with open(path, 'r') as f:
            self.view.setHtml(f.read())

    # функция, которая делает видимость стэка из диалогов см. структуру функции
    # изначально если нет dialog_stack то его создают, а потом воспроизводят.
    def scroll_down_history(self):
        if not self.dialog_stack:
            try:
                # НЕ пытайтесь поянть это...
                # Могу сказать одно что здесь используются различные махинации с БД с помрощью фуннкций из сервисов
                session = SessionService.get_session_by_id(self.id_of_session)
                checkpoint = session.checkpoint
                region = RegionService.get_region_by_id(checkpoint)
                heroes_placed = region.heroes_placed
                heroes = [ExistCreatureService.get_creature_by_name(name) for name in heroes_placed.split(';')]
                for hero in heroes:
                    texts = TextService.get_texts_by_region_id_and_hero_name(region.region_id, hero.hero_name)
                    for text in texts:
                        self.dialog_stack.append((hero, text, region.region_name))
                self.scroll_down_history()
            except TypeError as e:
                if str(e) == "'NoneType' object is not subscriptable":
                    self.return_page = EndPage()
                    self.return_page.show()
                    self.close()
            except Exception as e:
                print(e)
        else:
            try:
                pop_text_list = self.dialog_stack.pop(0)
                self.dialog_name_region_text_browser.setText(pop_text_list[2])
                text = pop_text_list[1].content
                res_text = ''
                for substr in text:
                    if substr == '\\':
                        continue
                    res_text += substr
                self.dialog_text_browser.setText(f'''{pop_text_list[0].hero_name}: \n
                {res_text}''')
                if not self.dialog_stack:
                    session = SessionService.get_session_by_id(self.id_of_session)
                    SessionService.update_checkpoint(session.checkpoint, self.id_of_session)
            except Exception as e:
                print(e)

        self.view.page().runJavaScript('''
            window.scrollBy(0, 200)
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

    # более приятный и отслеживаемый процесс загрузки страницы HTML
    def load_page(self):
        path = os.path.abspath('app\\static\\END.png.html')
        with open(path, 'r') as f:
            self.view.setHtml(f.read())

    # функция возврата к STARTPAGE
    def return_lobby(self):
        try:
            self.return_page = StartPage()
            self.return_page.show()
            self.close()
        except Exception as e:
            print(e)


# планируется добавить еще окон реализующий боевку и гру с броском дайсов
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StartPage()
    window.show()
    app.exec()
