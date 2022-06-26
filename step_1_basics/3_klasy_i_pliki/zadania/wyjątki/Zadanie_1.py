"""
Pobierz dane numeryczne od użytkownika i zapisz je do listy.
Użyj obsługi wyjątków by zwrócić użytkownikowi uwagę, gdy poda dane nienumeryczne.
Kontynuuj pytanie o dane dopóki użytkownik nie wpisze litery "N"
"""

liczby = []
while True:
    data = input("podaj liczbę ( lub N gdy chcesz zakończyć):")
    if data == 'N':
        print("dziękujęmy za skorzystanie")
        break
    try:
        liczby.append(int(data))
        a = 1/0
    except ValueError:
        print("Proszę podać liczbę")
    except Exception as e:
        print(e)
        print("ups")
    
print(liczby)