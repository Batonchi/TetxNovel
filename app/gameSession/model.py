class Region:

    def __init__(self, region_name:str, description: str, hero_placed: str, maybe_items: str, id=None):
        self.region_name = region_name
        self.description = description
        self.hero_placed = hero_placed
        self.maybe_items = maybe_items
        if id:
            self.id = id


class Session:

    def __init__(self, player_id: int, world_map: str, placement: str, checkpoint: int, items: str, the_player_puppet: int, id: int=None):
        self.player_id = player_id
        self.world_map = world_map
        self.placement = placement
        self.checkpoint = checkpoint
        self.items = items
        self.the_player_puppet = the_player_puppet
        if id:
            self.id = id




