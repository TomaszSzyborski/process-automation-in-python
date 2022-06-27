"""
Wymagania:
Sprawdź czy podana przez użytkownika liczba
jest podzielna przez 3, 5, 7

Wypisz wyniki na ekran.

Pamiętaj o komentarzach.

Rezultat wypisz na ekran.

Podpowiedź:
Odpowiednio formatuj stringi
"""

liczba = int(input("Podaj liczbe: "))

print("Podana liczba to: {}".format(liczba))

# dzielimy liczbę na 3 - i sprawdzamy resztę z dzielenia
if liczba % 3 == 0:
    print("Liczba {}, jest podzielna przez 3.".format(liczba))
else:
    print("Liczba {}, nie jest podzielna przez 3.".format(liczba))

if liczba % 5 == 0:
    print("Liczba {}, jest podzielna przez 5.".format(liczba))
else:
    print("Liczba {}, nie jest podzielna przez 5.".format(liczba))

if liczba % 7 == 0:
    print("Liczba {}, jest podzielna przez 7.".format(liczba))
else:
    print("Liczba {}, nie jest podzielna przez 7.".format(liczba))
