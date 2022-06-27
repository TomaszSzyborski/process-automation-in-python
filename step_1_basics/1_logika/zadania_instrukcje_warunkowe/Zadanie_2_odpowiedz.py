"""
Wymagania:
Napisz algorytm wystawiający ocenę na podstawie punktów uzyskanych na egzaminie
podaj ocenę na podstawie progu procentowego
5 od 90 do 100, 4+ od 80, 4 od 70, 3+ od 60, 3 od 50
Rezultat wypisz na ekran.

Podpowiedź:
przyjmij dane od uzytkownika
zweryfikuj dane
wypisz odpowiedni wynik lub komentarz dotyczący wprowadzonych danych
"""

punkty = int(input("Podaj punkty (od 0 do 100): "))

if 90 <= punkty <= 100:
    print("Twoja ocena to 5.")
elif 80 <= punkty:
    print("Twoja ocena to 4+.")
elif 70 <= punkty:
    print("Twoja ocena to 4.")
elif 60 <= punkty:
    print("Twoja ocena to 3+.")
elif 50 <= punkty:
    print("Twoja ocena to 3.")
else:
    print("Twoja ocena jest niedostateczna.")