class Article:

    def __init__(self, title: str, content: str, autor: str):
        self.title = title
        self.content = content
        self.author = autor

    def edit(self, new_content: str):
        self.content = new_content

    def change_author(self, new_autor: str):
        self.author = new_autor

    def rename(self,new_title: str):
        self.title = new_title

    def __repr__(self):
        return f"{self.title} - {self.content}: {self.author}"


article = Article(
    "Highest Recorded Temperature",
    "Temperatures across Europe are unprecedented, according to scientists.",
    "Ben Turner"
)
article.edit(
    "Syracuse, a city on the coast of the Italian island of Sicily, registered temperatures of 48.8 degrees Celsius"
)
article.rename(
    "Temperature in Italy"
)
article.change_author(
    "B. T."
)
print(article)
