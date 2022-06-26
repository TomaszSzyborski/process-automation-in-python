class Book:
    def __init__(self, title='', pages=0):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} with {self.pages} pages"


# chcemy aby sum() zwracało nam sumę stron w kolekcji książek
book1 = Book('Fluency', 381)
book2 = Book('The Martian', 385)
book3 = Book('Ready Player One', 386)

print(f"{book1}")


# teraz zwróci błąd
# try:
#     sum([book1, book2, book3])
# except TypeError as e:
#     print("ERROR:")
#     print(e)
#
# # teraz zwróci błąd
# try:
#     suma = book2, book3
#     print(suma)
# except TypeError as e:
#     print("ERROR:")
#     print(e)
#
# ########################################################################################################################
#
class Book:
    def __init__(self, title='', pages=0):
        self.title = title
        self.pages = pages

    def __str__(self):
        return self.title

    def __radd__(self, other):
        return self.pages + other

    def __add__(self, other):
        return self.pages + other
#
#
# # chcemy aby sum() zwracało nam sumę stron w kolekcji książek
book1 = Book('Fluency', 381)
book2 = Book('The Martian', 385)
book3 = Book('Ready Player One', 386)

# teraz zsumuje poprawnie
try:
    print(book1+ book2)
    suma = sum([book1, book2, book3])
    print(suma)
except TypeError as e:
    print("ERROR:")
    print(e)
#
#
# # zwykłe dodawanie
# try:
#     suma = book1 + book2
#     print(suma)
# except TypeError as e:
#     print("ERROR:")
#     print(e)
