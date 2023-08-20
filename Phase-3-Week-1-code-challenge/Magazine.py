from Article import Article
class Magazine:
    _all = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._all.append(self)

    def __str__(self):
        return f"Magazine: {self.name()} ({self.category()})"

    def name(self):
        return self._name

    def category(self):
        return self._category

    def articles(self):
        return [article for article in Article.all() if article.magazine() == self]

    def article_titles(self):
        return [article.title() for article in self.articles()]

    def contributors(self):
        return list({article.author() for article in self.articles()})

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def find_by_name(cls, name):
        return next((magazine for magazine in cls.all() if magazine.name() == name), None)

    @classmethod
    def article_titles(cls):
        return [article.title() for magazine in cls.all() for article in magazine.articles()]

    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            author = article.author()
            author_count[author] = author_count.get(author, 0) + 1
        return [author for author, count in author_count.items() if count > 2]
