class Item:
    def __init__(self, name, description, weight) -> None:
        self.name = name
        self.description = description
        self.weight = weight

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'weight': self.weight,
        }
