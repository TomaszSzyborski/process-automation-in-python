"""
Napisz klasę Zwierze, w której określisz odpowiednie pola:
- gatunek
- liczba nóg
- liczba oczu
- waga w kg
- sposob wydawania potomstwa na świat
- habitat (wodny, lądowy, wodnolądowy)
- tryb życia (dzienny nocny)

oraz metody:
- sprawdzająca stan przytomności (śpi lub jest aktywne)
- śpij i wybudź się - jako argument podaj godzinę, odwołaj się do trybu życia, żeby określić czy jest to możliwe
- rodź potomstwo - wynikiem ma być jajo lub noworodek, oraz ich liczba (zwróć tuplę - (str, int))

zwierzęta nocne budzą się o 18 a zasypiają o 6 rano (użyj domkniętych przedziałów)
zwierzęta dzienne budzą się o 6 rano a zasypiają o 18 (użyj domkniętych przedziałów)
Ssaki rodzą od karty do 5 młodych (możesz uwzględnić szczególne przypadki jajorodnych)
Ptaki składają od karty do 3 jaj
Płazy - dziesiątki jaj
Gady - dziesiątki jaj
Ryby - setki tysięcy jaj
Pajęczaki - dziesiątki do setek


Następnie, stwórz trzy klasy potomne wedle uznania:
Gady, Ptaki, Ssaki, Płazy, Ryby, Owady, Pajęczaki
"""
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
                 tryb_zycia = "dzienny",
                 habitat = "lądowy",
                 rodzenie_potomstwa="noworodek"):
        self.gatunek = gatunek
        self.waga_w_kg = waga_w_kg
        self.tryb_zycia = tryb_zycia
        self.habitat = habitat
        self.rodzenie_potomstwa = rodzenie_potomstwa
        self.przytomnosc = True

#     def rodz_potomstwo(self, od=karty, do=karty):
#         return Ssak("jamnik", 5)
#
#
#
# jamnik = Ssak("dachshund", 5)
# print(jamnik.rodz_potomstwo(karty, 5).gatunek)
# print(jamnik.czy_przytomne())
# print(jamnik.przytomnosc_o_godzinie(12))
# print(jamnik.tryb_zycia)
# print(jamnik.habitat)
