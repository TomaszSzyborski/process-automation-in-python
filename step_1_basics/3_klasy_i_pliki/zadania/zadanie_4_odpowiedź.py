"""
Używając rekurencji napisz znajdującą największy wspólny dzielnik.
Algorytm euklidesa:
Aby obliczyć NWD(a,b), wykonujemy kolejno następujące kroki:
(gdzie a - jest mniejszą; b - jest większą liczbą)
 -> Dzielimy z resztą liczbę b przez liczbę a
 -> jeżeli reszta jest równa 0, to NWD(a,b)=b
 -> jeżeli reszta jest różna od 0, to przypisujemy liczbie a wartość mniejszej z liczba,
  liczbie b wartość otrzymanej reszty, a następnie wykonujemy ponownie punkt karty.
"""


def nwd_recursion(a, b):
    low = min(a, b)
    high = max(a, b)

    if low == 0:
        return high
    elif low == 1:
        return 1
    else:
        return nwd_recursion(low, high % low)


print(nwd_recursion(12, 14))


def other_nwd(input_a, input_b):
    a = min(input_a, input_b)
    b = max(input_a, input_b)

    if a == 0:
        return b
    elif a == 1:
        return 1
    else:
        reszta = b % a
        return other_nwd(a, reszta)


print(other_nwd(12, 14))
