class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be an instance of Magazine")

        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, "_title"):
            print("Title cannot be changed once set!")
        elif not isinstance(value, str) or not (5 <= len(value) <= 50):
            raise TypeError("Title must be a string between 5 and 50 characters.")
        else:
            self._title = value


class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 1:
            self._name = name
        else:
            raise ValueError("Name must be a string with at least 1 character.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        print("Name cannot be changed once set!")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list(set(magazine.category for magazine in self.magazines()))


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Name must be a string between 2 and 16 characters.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must be a non-empty string.")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        return [author for author, count in author_counts.items() if count > 2]


# === TEST EXECUTION ===
# Creating instances
author1 = Author("John Doe")
magazine1 = Magazine("Tech Today", "Technology")

# Author writes an article
article1 = author1.add_article(magazine1, "The Future of AI")
article2 = author1.add_article(magazine1, "Cybersecurity Trends")

# Checking relationships
print(author1.articles())  # Should print a list of John's articles
print(author1.magazines())  # Should print a list of magazines John has written for
print(author1.topic_areas())  # Should print ['Technology']
