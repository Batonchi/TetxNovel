# В файле описаны модели таблиц из БД которые получаются и отправляются по запросу

# класс для структурирования полученных данных из таблицы players БД
class Player:

    def __init__(self, nick_name: str, hero_id: int, feedback: str, player_id: int = None):
        self.nick_name = nick_name
        self.hero_id = hero_id
        self.feedback = feedback
        if player_id:
            self.player_id = player_id
