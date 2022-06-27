"""
Wymagania:
Na podstawie klasy z Zadania_1 stwórz dwie po niej dziedziczące: Book_2 i Notebook

Niech:
- Klasa Book_2 posiada pole (typu lista) z linijkami tekstu
oraz metodę do odczytu tego pola o nazwie read_book()
która wypisuje linijki książki jedna po drugiej
lub gdy książka jest pusta wypisuje stosowny komentarz
- Klasa Notebook posiada pole (typu lista) z linijkami tekstu oraz metody:
    do odczytu kolejnych linijek - jeśli zeszyt jest pusty to podaj stosowny komunikat
    do zapisu kolejnych linijek - dodaj nową linię do listy linijek
    do edycji kolejnych linijek - zmień linię o danym indeksie na wprowadzaną linię
"""

from code.Day_5.zadania.klasy.Zadanie_1_odpowiedz import Book


class Book_2(Book):
    def __init__(self, lines_of_text=None, pages=32, title=""):
        super().__init__(title=title, pages=pages)
        self.__lines_of_text = lines_of_text

    def read_book(self):
        if self.__lines_of_text is None:
            print("Książka jest pusta!")
        else:
            print("\n".join(self.__lines_of_text))


class Notebook(Book):
    def __init__(self, lines_of_text=None, pages=32, title=""):
        super().__init__(title=title, pages=pages)
        self.__lines_of_text = lines_of_text

    def read_notebook(self):
        if self.__lines_of_text is None:
            print("Notes jest pusty!")
        else:
            print("\n".join(self.__lines_of_text))

    def write_to_notebook(self, line):
        if self.__lines_of_text is None:
            self.__lines_of_text = []
        self.__lines_of_text.append(line)

    def change_line(self, line_index, line):
        if self.__lines_of_text is None:
            print("Najpierw napisz conieco w zeszycie, żeby potem mieć co poprawiać :)")
        else:
            self.__lines_of_text[line_index] = line


if __name__ == '__main__':
    book_1 = Book_2(["asdasd", "adasdasd"])
    book_2 = Book_2(["asdasd", "adasdasd"])

    print(book_1 + book_2)
    print(book_1 == book_2)
    print(book_1 - book_2)
    book_1.read_book()

    notebook_1 = Notebook(title="Biologia")
    notebook_2 = Notebook(title="Matematyka")

    notebook_1.read_notebook()
    notebook_1.change_line(2, "Orki to takie pandy, tylko, ze w wodzie i maja pletwy")
    print()
    notebook_1.write_to_notebook("new line in notebook")
    notebook_1.write_to_notebook("new line in notebook")

    notebook_1.read_notebook()
    print()

    notebook_1.change_line(1, "zmieniamy")
    notebook_1.read_notebook()
