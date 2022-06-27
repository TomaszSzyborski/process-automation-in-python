"""
Pobierz od uzytkownika dane:
- imie
- nazwisko
- wiek

wyswietl powitanie uzględniajace powyzsze zmienne.
"""

imie = input("Podaj imie: ")
nazwisko = input("Podaj nazwisko: ")
wiek = input("Podaj wiek: ")

print("Witaj {} {}, masz {} lat".format(imie, nazwisko, wiek))
