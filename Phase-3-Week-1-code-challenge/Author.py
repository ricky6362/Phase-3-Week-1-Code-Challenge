from Article import Article
class Author:
    _all = []

    def __init__(self, name):
        self._name = name
        self._all.append(self)

    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all() if article.author() == self]

    def magazines(self):
        return list({article.magazine() for article in self.articles()})

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        return list({magazine.category() for magazine in self.magazines()})

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def get_all_articles(cls):
        return Article.all()
