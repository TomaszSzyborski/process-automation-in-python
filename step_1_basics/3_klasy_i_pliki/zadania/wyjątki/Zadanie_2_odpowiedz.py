"""
Wymagania:
Napisz program który stworzy plik csv (nazwij go dane_zadanie_2.csv) z danymi pobieranymi od użytkownika:
Imię, Nazwisko, Rok_Urodzenia. (w pętli)
Użyj funkcji
Użyj obsługi błędów aby upewnić się, że rok jest daną numeryczną
Dodaj kolumnę "Wiek", wartość ma być obliczona z obecnego roku przy użyciu danych z kolumny Rok_Urodzenia


Następnie otwórz plik i wypisz jego zawartość na ekran.
"""
lista_osob = []

while True:
    imie = input("Podaj Imie")
    nazwisko = input("Podaj Nazwisko ")
    rok_urodzenia = input("Podaj Rok Urodzenia ")
    try:
        dane_osobowe = {"imie": imie, "nazwisko": nazwisko,
                        "rok urodzenia": int(rok_urodzenia), "wiek": 2020 - int(rok_urodzenia)}
        lista_osob.append(dane_osobowe)
    except ValueError:
        print(f"Bład -  wprowadź rok jako liczbę")

    kontynuacja = input("Czy chesz kontynuować Y/N ").lower()
    if kontynuacja == 'n':
        break

with open("osoba.csv", 'a') as file:
    file.writelines([",".join(map(str, osoba.values())) + "\n" for osoba in lista_osob])

with open("osoba.csv", 'r+') as file:
    supposed_headers = list(map(str.strip, file.readlines(1)[0].split(",")))
    print(supposed_headers)
    print(list(lista_osob[0].keys()))

    content = file.readlines()
    content = content if content else []

    if supposed_headers != list(lista_osob[0].keys()):
        print("Updatig headers...")
        print(f"{content=}")
        headers = ",".join(lista_osob[0].keys()) + "\n"
        content.insert(0, headers)
        print(f"{content=}")

with open("osoba.csv", 'w') as file:
    file.writelines(content)
