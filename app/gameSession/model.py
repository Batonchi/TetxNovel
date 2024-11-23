# модели для работы с данными из БД

class Region:

    def __init__(self, id: int, region_name:str, hero_placed: str, maybe_items: str):
        self.region_name = region_name
        self.hero_placed = hero_placed
        self.maybe_items = maybe_items
        self.id = id


class Session:

    def __init__(self, id: int, player_id: int, checkpoint: int, player_puppet: int):
        self.player_id = player_id
        self.checkpoint = checkpoint
        self.player_puppet = player_puppet
        self.id = id




