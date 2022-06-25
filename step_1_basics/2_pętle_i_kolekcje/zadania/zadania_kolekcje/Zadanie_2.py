"""
Wymagania:
Napisz program, który wczytuje od użytkownika wartości
i dodaje je do listy dopóki użytkownik nie poda wartości 'nie'

Wypisz listę na ekran.
"""

lista = []

while True:
    value = input('Podaj jakas wartosc: ')
    if value == 'nie':
        break
    lista.append(value)

print(lista)