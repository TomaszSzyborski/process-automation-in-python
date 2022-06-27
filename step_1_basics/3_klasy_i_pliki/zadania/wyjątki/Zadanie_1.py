"""
Pobierz dane numeryczne od użytkownika i zapisz je do listy.
Użyj obsługi wyjątków by zwrócić użytkownikowi uwagę, gdy poda dane nienumeryczne.
Kontynuuj pytanie o dane dopóki użytkownik nie wpisze litery "N"
"""
liczby = []
while True:
    data = input("podaj liczbe ( lub N gdy chcesz zakonczyc: ")
    if data == 'N':
        print('dziekujemy za skorzystanie')
        break
    try:
        liczby.append(int(data))
    except ValueError as f:
        print('Prosze podac liczbe')
        #print(f)