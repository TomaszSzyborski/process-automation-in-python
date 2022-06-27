"""
Pobierz dane numeryczne od użytkownika i zapisz je do listy.
Użyj obsługi wyjątków by zwrócić użytkownikowi uwagę, gdy poda dane nienumeryczne.
Kontynuuj pytanie o dane dopóki użytkownik nie wpisze litery "N"
"""

lista_danych = []

# wersja karty
# while True:
#     dane = input("Podaj numer.\nJeśli chcesz zakończyć dodawanie liczb napisz 'N': ")
#     try:
#         if dane == 'N':
#             break
#         else:
#             lista_danych.append(float(dane))
#     except ValueError:
#         print(f"Wpisałeś '{dane}'!!\nPowinieneś podać numer!")

# wersja 2
# usuwa if oraz break i przenosi do warunku pętli while
# UWAGA: należy dodać zmienną <dane> przed pętlą

dane = None
while dane != 'N':
    dane = input("Podaj numer.\nJeśli chcesz zakończyć dodawanie liczb napisz 'N': ")
    try:
        lista_danych.append(float(dane))
    except ValueError:
        print(f"Wpisałeś '{dane}'!!\nPowinieneś podać numer!")

# wersja 3
# dodatkowo dba o typy wprowadzonych danych integer i float
# dodatkowo wypisuje podziękowanie na wyjściu z pętli
# dane = None
# while dane != 'N':
#     dane = input("Podaj numer.\nJeśli chcesz zakończyć dodawanie liczb napisz 'N': ")
#     try:
#         liczba = float(dane)
#         liczba = int(dane) if liczba.is_integer() else liczba
#         lista_danych.append(liczba)
#     except ValueError:
#         if dane == 'N':
#             print("Dziękujemy za skorzystanie z programu")
#         else:
#             print(f"Wpisałeś '{dane}'!!\nPowinieneś podać numer!")

if not lista_danych:
    print("Lista jest pusta")
else:
    print(lista_danych)

# wersja 4
# stawia na tworzenie funkcji i użycie słownika z funkcjami

# helper functions
def string_to_numeric(string):
    number = float(string)
    # ternary operator -> {outcome} if {condition} is true, else {outcome_2}
    return int(number) if number.is_integer() else number


def append_to_collection(item_string=None, collection=[]):
    if not item_string:
        print("Lista elementów: ", collection)
    else:
        collection.append(string_to_numeric(item_string))


# functions for dict
def default_function(dane):
    return lambda: append_to_collection(dane)


def exit_function():
    append_to_collection()
    print("Dziękujemy za skorzystanie z programu")
    return exit(0)


def pobranie_danych():
    function_dict = {'N': exit_function}
    try:
        dane = input("Podaj numer.\nJeśli chcesz zakończyć dodawanie liczb napisz 'N': ")
        function_dict.get(dane, lambda: append_to_collection(dane))()
    except ValueError:
        print(f"Wpisałeś '{dane}'!!\nPowinieneś podać numer!")

if __name__ == '__main__':
    while True:
        pobranie_danych()

