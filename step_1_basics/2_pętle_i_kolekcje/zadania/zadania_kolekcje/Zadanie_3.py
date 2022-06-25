"""
Wymagania:
Napisz program, który wczytuje od użytkownika stringi w postaci klucz - wartość
Dodaj je do słownika.
Jeśli dany klucz istnieje w słowniku - nie rób nic.

Zapewnij możliwość podania kolejnych par klucz-wartość lub zaprzestawania ich podawania.

Wypisz elementy słownika na ekran w formie "klucz -> wartość"

Podpowiedź:
Użyj dwóch inputów do pobrania wartości
"""

slownik = {}

while True:

    word = input('Podaj pierwsze slowo: ')
    if word == 'exit':
        break

    word1 = input('Podaj drugie slowo: ')

    if word not in slownik.keys():
        slownik[word] = word1
        print("added")
    else:
        print("not added")

print(slownik)
