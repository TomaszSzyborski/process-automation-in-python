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

wynik = int(input('Podaj wynik: '))

if wynik >= 90:
    print('Twoja cena to 5')
elif 80 <= wynik < 90:
    print('Twoja ocena to 4')
elif 70 <= wynik < 80:
    print('Twoja ocena to 3')
elif 60 <= wynik < 70:
    print('Twoja ocena to 3+')
elif 50 <= wynik < 60:
    print('Twoja ocena to 3')
else:
    print('Nie zdałeś')
