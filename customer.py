class Customer:

    def __init__(self, id, name, birth_date, address) -> None:
        self.id = id
        self.name = name
        # more

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def days_left_to_birthday(self):
        pass