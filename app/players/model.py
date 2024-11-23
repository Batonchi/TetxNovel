# В файле описаны модели таблиц из БД которые получаются и отправляются по запросу

class Player:

    def __init__(self, id: int, nick_name: str, hero_id: int, feedback: str):
        self.nick_name = nick_name
        self.hero_id = hero_id
        self.feedback = feedback
        self.id = id
