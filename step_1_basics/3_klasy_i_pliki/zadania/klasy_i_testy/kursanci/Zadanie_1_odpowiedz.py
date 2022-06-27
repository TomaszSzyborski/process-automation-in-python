"""
Wymagania:
Stwórz klasę Kursant posiadającą pola:
- dzień kursu - niech będzie polem klasy dostępnym dla wszystkich instancji
- odrobiona praca domowa - dotyczy tylko pojedynczej instancji (domyślnie False)
- obecność - dotyczy tylko pojedynczej instancji (domyślnie True)
- punkty z egzaminu - dotyczy tylko pojedynczej instancji (domyślnie None)
- imie - dotyczy tylko pojedynczej instancji (jedyny parametr konstruktora)
(dla chętnych - zapewnij, żeby imię zawsze zaczynało się wielką literą, niezależnie jakimi literami wrzucimy stringa do konstruktora)

Wszystkie pola oprócz dnia kursu powinny być pseudoprywatne.


Stwórz metody: getter i setter dla pól:
- imie (tylko getter, ustaw imię w konstruktorze - niech imię będzie jedynym prarametrem)
- odrobiona praca domowa
- obecność
- punkty z egzaminu
mając na uwadze że dzień kursu i punkty z egzaminu intem
a obecność i odrobiona praca domowa booleanem
"""


class Kursant:
    dzien_kursu = 0

    def __init__(self, imie):
        self.__imie = imie  # można imie.title(), żeby zapewnić wielką literę na początku i małe dalej
        self.__odrobiona_praca_domowa = False
        self.__obecnosc = True
        self.__punkty_z_egzaminu = None

    @property
    def imie(self):
        return self.__imie

    @property
    def odrobiona_praca_domowa(self):
        return self.__odrobiona_praca_domowa

    @odrobiona_praca_domowa.setter
    def odrobiona_praca_domowa(self, boolean):
        self.__odrobiona_praca_domowa = boolean

    @property
    def obecnosc(self):
        return self.__obecnosc

    @obecnosc.setter
    def obecnosc(self, boolean):
        self.__obecnosc = boolean

    @property
    def punkty_z_egzaminu(self):
        return self.__punkty_z_egzaminu

    @punkty_z_egzaminu.setter
    def punkty_z_egzaminu(self, punkty):
        self.__punkty_z_egzaminu = punkty
