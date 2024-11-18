class Reference:
    def __init__(self, id, author, title, journal, year ):
        self.id = id
        self.author = author
        self.title = title
        self.journal = journal
        self.year = year

    def __str__(self):
        return f"Article, author: {self.author}, title: {self.title}, journal: {self.journal} year: {self.year}"