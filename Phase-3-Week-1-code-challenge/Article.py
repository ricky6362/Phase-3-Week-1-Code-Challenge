class Article:
    _all = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        self._all.append(self)

    def __str__(self):
        return f"Article: {self.title()} by {self.author().name()} in {self.magazine().name()}"

    def title(self):
        return self._title

    def author(self):
        return self._author

    def magazine(self):
        return self._magazine

    @classmethod
    def all(cls):
        return cls._all
