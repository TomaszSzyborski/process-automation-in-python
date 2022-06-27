"""
mając listę owoców
stwórz słowniki mające jako klucze nazwy rozpoczynające się wielką literą
karty. jako warotści długości nazw
2. jako wartości ceny będące sumą kodów ASCII pierwszej i ostatniej litery podzieloną przez długość nazwy
"""

fruits = ['apple', 'mango', 'banana', 'cherry', 'passionfruit', 'dragonfruit', 'date']

# ad.karty
first = {fruit.title(): len(fruit) for fruit in fruits}
print(first)

# ad.2
second = {fruit.title(): f"{(ord(fruit[0]) + ord(fruit[-1])) / len(fruits):.2f}" for fruit in fruits}
print(second)
