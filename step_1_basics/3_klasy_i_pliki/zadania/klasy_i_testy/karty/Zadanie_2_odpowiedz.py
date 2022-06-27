"""
Wymagania:
napisz dwie klasy: Kon, Osiol, dziedziczące po klasie Zwierze (wykorzystaz zadanie_3 z poprzedniego dnia)

Nastepnie stworz klasy:
- Mul - dziedziczącą po Koniu i Ośle
- Oslomul - dziedziczącą po Ośle i Koniu

"""
import random

from random import randint


class Zwierze:
    gatunek = ""
    liczba_nog = ""
    liczba_oczu = ""
    waga_w_kg = 0
    rodzenie_potomstwa = ""
    habitat = ""
    tryb_zycia = ""
    przytomnosc = None

    # Object constructor
    def __init__(self,
                 gatunek,
                 liczba_nog,
                 liczba_oczu,
                 waga_w_kg,
                 rodzenie_potomstwa,
                 habitat,
                 tryb_zycia):
        self.gatunek = gatunek
        self.liczba_nog = liczba_nog
        self.liczba_oczu = liczba_oczu
        self.waga_w_kg = waga_w_kg
        self.rodzenie_potomstwa = rodzenie_potomstwa
        self.habitat = habitat
        self.tryb_zycia = tryb_zycia
        self.przytomnosc = True

    def czy_przytomne(self):
        return self.przytomnosc

    def przytomnosc_o_godzinie(self, godzina):
        if self.tryb_zycia == "dzienny":
            if 6 <= godzina <= 18:
                przytomne = True
            else:
                przytomne = False
        elif self.tryb_zycia == "nocny":
            if 18 <= godzina <= 24 or 0 <= godzina <= 6:
                przytomne = True
            else:
                przytomne = False
        return przytomne

    def spij(self):
        self.przytomnosc = False

    def obudz_sie(self):
        self.przytomnosc = True

    def rodz_potomstwo(self, od=1, do=1):
        return self.rodzenie_potomstwa, randint(od, do)


class Ssak(Zwierze):
    liczba_nog = 4
    liczba_oczu = 2

    def __init__(self,
                 gatunek,
                 waga_w_kg,
                 tryb_zycia="dzienny",
                 habitat="lądowy",
                 rodzenie_potomstwa="noworodek"):
        self.gatunek = gatunek
        self.waga_w_kg = waga_w_kg
        self.tryb_zycia = tryb_zycia
        self.habitat = habitat
        self.rodzenie_potomstwa = rodzenie_potomstwa
        self.przytomnosc = True


#     def rodz_potomstwo(self, od=1, do=1):
#         return Ssak("jamnik", 5)
#
#
#
# jamnik = Ssak("dachshund", 5)
# print(jamnik.rodz_potomstwo(1, 5).gatunek)
# print(jamnik.czy_przytomne())
# print(jamnik.przytomnosc_o_godzinie(12))
# print(jamnik.tryb_zycia)
# print(jamnik.habitat)


class Kon(Ssak):
    # barwa = "gniady"

    def __init__(self, barwa="gniady", gatunek="", waga_w_kg=None):
        super().__init__(gatunek, waga_w_kg)
        self.barwa = barwa
        if waga_w_kg is None:
            self.waga_w_kg = random.randint(100, 700)
        else:
            self.waga_w_kg = waga_w_kg


class Osiol(Ssak):
    def __init__(self, barwa="szarobury", gatunek="", waga_w_kg=None):
        super().__init__(gatunek, waga_w_kg)
        self.barwa = barwa
        if waga_w_kg is None:
            self.waga_w_kg = random.randint(100, 200)
        else:
            self.waga_w_kg = waga_w_kg


class Mul(Kon, Osiol):
    rodzenie_potomstwa = None

    def __init__(self, gatunek="Muł"):
        super().__init__()
        self.gatunek = gatunek

    def rodz_potomstwo(self, **kwargs):
        return "BEZPŁODNY"


class Oslomul(Osiol, Kon):
    rodzenie_potomstwa = None

    def __init__(self, gatunek="Oslomulica"):
        super().__init__()
        self.gatunek = gatunek

    def rodz_potomstwo(self, **kwargs):
        return "BEZPŁODNY"


if __name__ == '__main__':
    konik = Kon(barwa="kary", gatunek="Arab")
    osiolek = Osiol(barwa="szary", gatunek="Europejski")

    print("konik:")
    print(konik.barwa)
    print(konik.gatunek)
    print(konik.tryb_zycia)
    print(konik.habitat)
    print(konik.rodz_potomstwo())

    print(80 * "#")

    print("osiolek:")
    print(osiolek.barwa)
    print(osiolek.gatunek)
    print(osiolek.tryb_zycia)
    print(osiolek.habitat)
    print(osiolek.rodz_potomstwo(**{"od":5,"do":17}))

    print(80 * "#")

    mulica = Mul()
    print("Muł:")
    print(mulica.barwa)
    print(mulica.gatunek)
    print(mulica.tryb_zycia)
    print(mulica.habitat)
    print(mulica.rodz_potomstwo())

    print(80 * "#")

    oslomulica = Oslomul()
    print("Osłomuł:")
    print(oslomulica.barwa)
    print(oslomulica.gatunek)
    print(oslomulica.tryb_zycia)
    print(oslomulica.habitat)
    print(oslomulica.rodz_potomstwo())
