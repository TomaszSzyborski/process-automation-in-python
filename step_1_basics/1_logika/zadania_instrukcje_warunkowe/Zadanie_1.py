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

liczba = int(input('Podaj liczbe: '))

div_by_three = liczba % 3 == 0
div_by_five = liczba % 5 == 0
div_by_seven = liczba % 7 == 0

if div_by_three or div_by_five or div_by_seven:
    if div_by_three:
        print(f'Podana {liczba=} jest podzielna przez 3')
    if div_by_five:
        print(f'Podana {liczba=} jest podzielna przez 5')
    if div_by_seven:
        print(f'Podana {liczba=} jest podzielna przez 7')
else:
    print(f'Podana {liczba=} nie jest podzielna przez 3, 5 ani 7')
