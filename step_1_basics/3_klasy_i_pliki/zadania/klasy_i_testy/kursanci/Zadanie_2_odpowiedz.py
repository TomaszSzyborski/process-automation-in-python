"""
Wymagania:
Rozwiń klasę z zadania karty (uprzednio przeklejając kod tutaj)
w taki sposób by gdy punkty z egzaminu są nie ustawione (czyli są None)
to program wypisze stosowny komunikat: "Kursant IMIĘ musi najpierw podejść do egzaminu" i zwróci None
natomiast gdy ustawione - zwróci liczbę punktów uzyskanych na egzaminie

Stwórz trzech kursantów - Janka, Franka i Aleksa
Przejdź przez 15 dni kursu wypisując progres kursantów:
- Imię
- Obecność (ustaw losowo)
- Czy praca domowa jest odrobiona czy nie (ustaw losowo)
- Dzień kursu (najpierw ustaw zmienną w klasie - dzień kursu, a następnie odczytaj z tej zmiennej)
- Uzyskane punkty na egzaminie (ustaw losowo - 7 dnia tygodnia)

Podpowiedź:
użyj random.choice do losowego ustawienia True i False
użyj random.randint do losowego ustawienia punktów (w zakresie 0 - 100)
"""


class Kursant:
    dzien_kursu = 0

    def __init__(self, imie):
        self.__imie = imie.title()
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
        if not self.__punkty_z_egzaminu:
            print(f"Kursant {self.__imie} musi najpierw podejść do egzaminu!")
        return self.__punkty_z_egzaminu

    @punkty_z_egzaminu.setter
    def punkty_z_egzaminu(self, punkty):
        self.__punkty_z_egzaminu = punkty


if __name__ == '__main__':
    janek = Kursant("Janek")
    franek = Kursant("Franek")
    aleks = Kursant("Aleks")

    import random

    for _ in range(1, 16):
        Kursant.dzien_kursu += 1
        for kursant in [janek, franek, aleks]:
            print(f"Imię: {kursant.imie}")
            kursant.obecnosc = random.choice([True, False])
            print(f"Obecność: {kursant.obecnosc}")
            kursant.odrobiona_praca_domowa = random.choice([True, False])
            print(f"Odrobiona praca domowa: {kursant.odrobiona_praca_domowa}")
            print(f"Dzień kursu: {kursant.dzien_kursu}")
            if Kursant.dzien_kursu == 7:
                kursant.punkty_z_egzaminu = random.randint(1, 100)
            else:
                punkty = kursant.punkty_z_egzaminu
                if punkty:
                    print(punkty)
            print(80 * "=")
