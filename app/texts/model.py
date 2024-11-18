class Text:

    def __init__(self, content: str, degree_of_friendly: int, region_id: int, id=None):
        self.content = content
        self.degree_of_friendly = degree_of_friendly
        self.region_id = region_id
        if id:
            self.id = id
