class Player:

    def __init__(self, nick_name: str, hero_id: int, feedback: str, id=None):
        self.nick_name = nick_name
        self.hero_id = hero_id
        self.feedback = feedback
        if id:
            self.id = id

