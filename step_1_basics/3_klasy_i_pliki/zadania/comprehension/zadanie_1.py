"""
Wymagania:
Użyj list comprehension, żeby:
karty. Stworzyć listę szceścianów liczb jeśli liczba bazowa jest podzielna przez 5 (1 od 1 do 500)
2. Mając do dyspozycji tuplę (1, 2) stworzyć listę wszystkich kombinacji.
   Wynik: (1, 1), (1, 2), (2, 1), (2, 2)
3. Stworzyć listę list zawierającą liczby podzielone przez 2, podzielone przez 3 oraz bazowe liczby
   gdy liczba bazowa w zakresie
   daje resztę 3 przy dzielenie przez 4 (zakres od 1 to 500)
   Wynik:
   [[1.5, 1, 3], [3.5, 2.3333333, 7], ...]
4. Stworzyć listę list, w której listy wewnętrzne zawierają liczby z zakresu pierwszej
   listy podzielone przez liczby z zakresu drugiej listy
   Przykład:
   lista_1 = [1, 2, 3]
   lista_2 = [1, 2, 3, 4]
   wynik => [[1.0, 0.5, 0.3333333333333333, 0.25], [2.0, 1.0, 0.6666666666666666, 0.5], [3.0, 1.5, 1.0, 0.75]]
"""