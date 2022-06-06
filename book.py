class Book:

    def __init__(self, id, name, author) -> None:
        self.id = id
        self.name = name
        self.author = author

    def __str__(self) -> str:
        return self.name