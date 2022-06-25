"""
Stwórz listę trzech słowniki - Krystynę, Agnieszkę i Piotrka
Każdy kursant powinien mieć imię, informację o obecności i pracy domowej oraz punkty na egzaminie

Przejdź przez 6 dni kursu wypisując progres kursantów:
- Imię
- Obecność (ustaw losowo)
- Czy praca domowa jest odrobiona czy nie (ustaw losowo)
- Uzyskane punkty na egzaminie (ustaw losowo) (ustaw dopiero 6 dnia kursu)

Podpowiedź:
użyj random.choice do losowego ustawienia True i False
użyj random.randint do losowego ustawienia punktów (w zakresie 0 - 100)
"""
import copy
from pprint import pprint
from random import choice, randint
Krystyna = {'imie': 'Krystyna', 'obecnosc': None, 'praca_domowa': None}
Agnieszka = {'imie': 'Agnieszka', 'obecnosc': None, 'praca_domowa': None}
Piotrek = {'imie': 'Piotrek', 'obecnosc': None, 'praca_domowa': None}

lista = []

for day in range(1, 7):
    for kursant in [Krystyna, Agnieszka, Piotrek]:
        k = copy.deepcopy(kursant)
        k['obecnosc'] = choice([False, True])
        k['praca_domowa'] = choice([False, True])
        if day == 6:
            k['punkty'] = randint(0, 100)

        lista.append(k)

pprint(lista)
