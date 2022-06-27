"""
Stwórz klasę Book, tak jak w przykładzie operator_overloading.py
Napisz przeciążenia operatorów aby porównać strony książek:
- dodanie ksiązki do książki
- sumowanie stron z kolekcji książek
- sprawdzanie mniejszości
- sprawdzanie mniejsze-równe
- sprawdzenie większości
- sprawdzenie większe-równe
- sprawdzenie równości
- sprawdzenie nierówności
- sprawdzenie cakowitej różnicy w liczbie stron
"""


class Book:
    title = ''
    pages = 0

    def __init__(self, title='', pages=0):
        self.title = title
        self.pages = pages

    def __radd__(self, other):
        return self.pages + other

    def __add__(self, other):
        return self.pages + other

    def __lt__(self, other):
        return self.pages < other

    def __le__(self, other):
        return self.pages <= other

    def __gt__(self, other):
        return self.pages > other

    def __ge__(self, other):
        return self.pages >= other

    def __eq__(self, other):
        return self.pages == other

    def __ne__(self, other):
        return self.pages != other

    def __sub__(self, other):
        return abs(self.pages - other.pages)


if __name__ == '__main__':
    elementarz = Book("Mały elementarz", 37)
    fizyka = Book("Podstawowy podręcznik fizyki kwantowej", 4756)

    print("sub")
    print(elementarz - fizyka)

    print("radd")
    print(sum([elementarz, fizyka]))

    print("add")
    print(elementarz + fizyka)

    print("lt")
    print(elementarz < fizyka)

    print("le")
    print(elementarz <= fizyka)

    print("eq")
    print(elementarz == fizyka)

    print("ne")
    print(elementarz != fizyka)

    print("gt")
    print(elementarz > fizyka)

    print("ge")
    print(elementarz >= fizyka)

    print("sub")
    print(elementarz - fizyka)

    print("drukuj tytuł największej")
    print(max(elementarz, fizyka).title)
