"""
Tytuł: ord i chr

Zadanie:
Zapisać swoje imię i nazwisko w wartościach numerycznych ASCII
oraz za pomoca dodawania, przy użyciu funkcji ord oraz chr

Podpowiedzi:
https://pl.wikipedia.org/wiki/ASCII
"""
result = list()

name = 'Szymon Kotlowski'

for ch in name:
    result.append(ord(ch))

print(result)

result2 = list()
for number in result:
    result2.append(chr(number))

print(''.join(result2))
