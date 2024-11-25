# модели для работы с данными из БД

class Region:

    def __init__(self, region_name:str, hero_placed: str, maybe_items: str, region_id: int = None):
        self.region_name = region_name
        self.hero_placed = hero_placed
        self.maybe_items = maybe_items
        if region_id:
            self.region_id = region_id


class Session:

    def __init__(self, player_id: int, checkpoint: int, player_puppet: int, game_session_id: int = None):
        self.player_id = player_id
        self.checkpoint = checkpoint
        self.player_puppet = player_puppet
        if game_session_id:
            self.game_session_id = game_session_id



