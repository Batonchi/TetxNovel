import os
import docx2txt
import sys


from app.heroes.service import ExistCreatureService, ExistCreature
from app.items.service import ItemService, Item
from app.texts.service import TextService, AnswerTextService, Text
from app.gameSession.service import RegionService, Region
from app.dices.service import FaceService, Face, DiceService, Dice
from PyQt6.QtWidgets import (QPushButton, QTextEdit, QLabel, QMainWindow, QApplication, QDialog,
                             QFileDialog, QVBoxLayout)
from PyQt6.QtGui import QPixmap
from random import choices


# функция обрабатывает текст и заполняет таблицы по данным из текта
def update_info(text: str):
    tables_insert = {
        'heroes': (ExistCreatureService.set_creature, ExistCreature),
        'items': (ItemService.set_item, Item),
        'faces': (FaceService.set_face, Face),
        'answer_texts': (AnswerTextService.set_text, Text),
        "texts": (TextService.set_text, Text),
        'regions': (RegionService.set_region, Region),
        'dices': (DiceService.set_dice, Dice)
    }

    text = text.split('\n')
    for el in text:
        if el != '':
            elem_split = el.split(':')
            name_table = elem_split[0].split()[1]
            arguments = elem_split[1].rstrip().lstrip()[1: -1].split(', ')
            func = tables_insert[name_table][0]
            func_class_arg = tables_insert[name_table][1](*arguments)
            func(func_class_arg)


# окно в котором вы можете сохздать тот самый текст для функции выше
class CreateInsertDBDAta(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Внимательно читайте инструкцию')
        self.max_font_size = '22'
        self.min_font_size = '14'
        self.text_browser = QTextEdit(self)
        self.text_browser.setFixedSize(1000, 1000)
        self.text_browser.setStyleSheet('font-size: 18px; padding: 10px')
        self.send_insert_btn = QPushButton(self)
        self.send_insert_btn.setText('Отправить изменения')
        self.send_insert_btn.resize(200, 100)
        self.send_insert_btn.move(1020, 0)
        self.import_text_document_btn = QPushButton(self)
        self.import_text_document_btn.setText('Импортировать .docx или .txt файл')
        self.import_text_document_btn.resize(200, 100)
        self.import_text_document_btn.move(1020, 110)
        self.instruction = QPushButton(self)
        self.instruction.setText('Нажми на меня')
        self.instruction.resize(200, 100)
        self.instruction.move(1020, 220)
        self.label = QLabel(self)
        self.label.move(1020, 400)
        self.label.resize(700, 600)
        self.label.setStyleSheet('background-color: #3D3D3D;')
        self.clear_text_browser = QPushButton('Очистить поле текста', self)
        self.clear_text_browser.resize(320, 100)
        self.clear_text_browser.move(1410, 220)
        self.plus_btn = QPushButton('+', self)
        self.plus_btn.resize(50, 50)
        self.plus_btn.move(1020, 330)
        self.minus_btn = QPushButton('-', self)
        self.minus_btn.resize(50, 50)
        self.minus_btn.move(1090, 330)
        self.save_text_field = QPushButton('Сохранить в файл.txt', self)
        self.save_text_field.resize(150, 50)
        self.save_text_field.move(1150, 330)
        self.tables = {
            'answer_texts.png': QPushButton('answer_texts table', self),
            'texts.png': QPushButton('texts table', self),
            'regions.png': QPushButton('regions table', self),
            'dices.png': QPushButton('dices table', self),
            'faces.png': QPushButton('faces table', self),
            'heroes.png': QPushButton('heroes table', self),
            'items.png': QPushButton('items table', self),
        }
        for k in self.tables:
            self.tables[k].resize(150, 100)
            self.tables[k].clicked.connect(self.view_image)
        self.tables['answer_texts.png'].move(1240, 0)
        self.tables['texts.png'].move(1410, 0)
        self.tables['regions.png'].move(1580, 0)
        self.tables['dices.png'].move(1240, 110)
        self.tables['faces.png'].move(1410, 110)
        self.tables['heroes.png'].move(1580, 110)
        self.tables['items.png'].move(1240, 220)
        self.plus_btn.clicked.connect(self.do_bigger_text)
        self.minus_btn.clicked.connect(self.do_smaller_text)
        self.clear_text_browser.clicked.connect(self.do_clear)
        self.send_insert_btn.clicked.connect(self.send_insert)
        self.import_text_document_btn.clicked.connect(self.import_file)
        self.instruction.clicked.connect(self.instruct)
        self.save_text_field.clicked.connect(self.save_in_txt_file)

    # функция для вывода диаграмм БД таблиц
    def view_image(self):
        try:
            per = self.sender().text().split()
            self.label.setPixmap(QPixmap(f'app/static/diagrams/{per[0]}.png'))
        except Exception as e:
            print(e)

    # функция для импорта текстового файла для удобства
    def import_file(self):
        dialog = QFileDialog.getOpenFileName(
            self, 'Выбрать файл с данными', '',
            'Текст (*.docx *.txt)'
        )
        if dialog[0].split('.')[1] == 'docx':
            file = docx2txt.process(dialog[0])
            self.text_browser.setPlainText(file)
        else:
            with open(dialog[0], 'r', encoding='utf-8') as f:
                self.text_browser.setPlainText(f.read())

    # функция отвечающая за отправку текста из текстового поля на обработку функцией
    def send_insert(self):
        try:
            update_info(self.text_browser.toPlainText())
            custom_ok = CustomOKDialog()
            custom_ok.exec()

        except Exception as e:

            # класс диалогового окна использую так потому что мне кажется, что  оно нигде не пригодиться
            # Класс посвящен тем кто хочет сломать окно))))
            class CustomErrorDialog(QDialog):
                def __init__(self, error_text):
                    super().__init__()

                    self.setWindowTitle('Это инструкция')

                    error = QLabel(f'А я говорил, писать правильно ---- ERRRRRROR {error_text}!!!')
                    layout = QVBoxLayout()
                    layout.addWidget(error)
                    self.setLayout(layout)

            custom_dialog = CustomErrorDialog(e)
            custom_dialog.exec()

    # функция предоставляет доступ к диалоговому окну, внутри окно интсрукция по работе с данным редактором, и создает его
    def instruct(self):
        # класс диалогового окна использую так потому что мне кажется что здесь оно нигде не пригодиться
        class CustomInstructDialog(QDialog):
            def __init__(self):
                super().__init__()

                self.setWindowTitle('Это инструкция')

                layout = QVBoxLayout()
                instruction = QLabel('''Привествую в редакторе БД,
                                    Уважительная просьба ознакомиться с правилами заполнения БД.
                                    Ничего не рушьте! Все сделано из **** и ****, поэтому читайте внимательно!
                                    Во-первых, есди вам хочется изменить БД, пока что поддерживается
                                     только функция добавления.
                                    Во-вторых, ради того, чтобы было удобно заполнять интсрукцию, которая перейдет
                                     в SQL запрос следуйте ситнаксису:
                                     Table name_of_table_where_insert: (column_1, column_2, ... column_n)
                                    Также для простоты заполнения структура таблиц дроступна 
                                    по нажатию кнопки соответсвующего имени...Простите за грамотность, мы не на уроке 
                                    русского!
                                    здесь доступна функция по увеличеванию размера шрифта поля
                                    )))).
                                    С уважением разпработчик.
                                    Также стоит упомянуть что есть такие переменные как листы, к ним относяться:
                                                ---maybe_items/items/description -> почти вся странно названая хрень с 
                                                текст типом,
                                                поясню, там где нет в названиии id, name, но есть упомянание другой 
                                                таблицы, 
                                                либо множественнрое число.Перчесиление в них через ';' - точку 
                                                с запятой;
                                    Также встречаеться переменные, которые требуют для заполнения текстом с пугктацией,
                                    знак ', ' - строго зарезервирован!!!!!
                                    Хотите поставить запятую ставьте ',/' или сразу пишите текст
                                    Примеры моего заполнения:
                                            Table items: (Зачарованная херня,  5|xp;1|atk;5|mul;0.9|rev;1|drop;Для чего?
                                             Не знаю, скажу честно врагу будет не приятно,\\ а тебе больно. Тебе смешно?
                                              -Да это же просто зачарованная херня!,  странный предмет)
                                            Table items: (Честный меч , 5|xp;0|atk;10|mul;0.5|rev;7|en;Меч бесчестия с 
                                            честью врученный вам,  странный предмет)
                                            Table items: (Меч Паллада Тьмы, 10|atk;0.3|rev;15|en;Просто темный меч,
                                             оружие)
                                            Table items: (Еда богов, 10|xp;0.1|rev;2|en;Небесное наслаждение в одном 
                                            укусе…Одним разом не ограничишься, еда)
                                            Table items: (Вкусный попкорн, 1|xp;1|en;0.3|rev;Полученный посредством 
                                            убийства детских мечт попкорн… Он до сих пор вызывает сомнения у пробующих 
                                            его…Точно ли это попкорн?, еда)
                                    КОЛИЧЕСТВО АРГУМЕНТОВ СТАТИЧНО И СООТВЕТСВУЕТ ТАБЛИЦАМ ПРЕДСТАВЛЕННЫМ!
                                    Стоит упомянуть, любой запрос без 'энтера' просто в линию.
                                    стурктуру зависимостей см. start-data.txt.Там показано, что нужно, чтобы в
                                     дальнейшем поддерживать весь процесс
                                    ''')
                layout.addWidget(instruction)
                self.setLayout(layout)

        dialog = CustomInstructDialog()
        dialog.exec()

    # функция очистки текстового поля
    def do_clear(self):
        self.text_browser.setPlainText('')

    # функция для увеличения размера шрифта
    def do_bigger_text(self):
        style = self.text_browser.styleSheet().split('; ')
        font_size = style[0].split()[1].replace('px', '')
        if int(self.max_font_size) != int(font_size):
            self.text_browser.setStyleSheet(f'font-size: {int(font_size) + 1}px' + '; ' + '; '.join(style[1:]))

    # функция для уменьшения размера шрифта
    def do_smaller_text(self):
        style = self.text_browser.styleSheet().split('; ')
        font_size = style[0].split()[1].replace('px', '')
        if int(self.min_font_size) != int(font_size):
            self.text_browser.setStyleSheet(f'font-size: {int(font_size) - 1}px' + '; ' + '; '.join(style[1:]))

    # функция сохраняющая в файл формата .txt все из текстового поля
    def save_in_txt_file(self):
        try:
            name_of_file = ''.join(choices([chr(i) for i in range(97, 123)], k=10))
            with open(f'app\\textFiles\\{name_of_file}.txt', 'w') as f:
                f.write(self.text_browser.toPlainText())
            custom_ok = CustomOKDialog()
            custom_ok.exec()
        except Exception as e:
            print(e)


# кастомный диалог пока что здесь, как затычка до лучших времен.
class CustomOKDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Операция успешна')

        ok_status = QLabel(f'Ваш запрос обработан, Поздравляю!')
        layout = QVBoxLayout()
        layout.addWidget(ok_status)
        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CreateInsertDBDAta()
    window.show()
    app.exec()


