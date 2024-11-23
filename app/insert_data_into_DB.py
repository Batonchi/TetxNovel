import os
import docx2txt


from app.heroes.service import ExistCreatureService, ExistCreature
from app.items.service import ItemService, Item
from app.texts.service import TextService, AnswerTextService, Text
from app.gameSession.service import RegionService, Region
from app.dices.service import FaceService, Face, DiceService, Dice


# функция обрабатывает файл докс и запалняет БД данными
def update_info(file_name: str):
    tables_insert = {
        'heroes': (ExistCreatureService.set_creature, ExistCreature),
        'items': (ItemService.set_item, Item),
        'faces': (FaceService.set_face, Face),
        'answer_texts': (AnswerTextService.set_text, Text),
        "texts": (TextService.set_text, Text),
        'regions': (RegionService.set_region, Region),
        'dices': (DiceService.set_dice, Dice)
    }

    text = docx2txt.process(os.path.abspath(file_name)).split('\n')
    for el in text:
        if el != '':
            elem_split = el.split(':')
            name_table = elem_split[0].split()[1]
            arguments = elem_split[1].rstrip().lstrip()[1: -1].split(', ')
            arguments[0] = int(arguments[0])
            if name_table == 'texts' or name_table == 'answer_texts':
                arguments[3] = int(arguments[3])
                func = tables_insert[name_table][0]
                func_class_arg = tables_insert[name_table][1](*arguments)
                func(func_class_arg)
            else:
                func = tables_insert[name_table][0]
                func_class_arg = tables_insert[name_table][1](*arguments)
                func(func_class_arg)
