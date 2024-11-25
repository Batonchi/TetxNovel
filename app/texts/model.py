# модель для обертки  данных из answers_texts и texts таблиц БД


class Text:

    def __init__(self, content: str, degree_of_friendly: int, region_id: int, who_say: str = None, text_id: int = None):
        self.content = content
        self.degree_of_friendly = degree_of_friendly
        self.region_id = region_id
        self.who_say = who_say
        if text_id:
            self.text_id = text_id
        if who_say:
            self.who_say = who_say
