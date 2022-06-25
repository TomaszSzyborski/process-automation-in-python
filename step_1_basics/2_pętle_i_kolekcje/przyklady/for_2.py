# # oblicz ilosc liczb parzystych i nieparzystych w zakresie
# zakres = range(1, 101)
# parzyste = 0
# nieparzyste = 0
#
# for liczba in zakres:
#
#     licznik_for = 0
#
#     # jesli parzysta to dodac do licznika parzystych
#     if liczba % 2 == 0:
#         parzyste += 1
#     else:
#         nieparzyste +=1
#
#     licznik_for += 1
#
# print("Parzyste: {}, nieparzyste: {}".format(parzyste, nieparzyste))
# print(licznik_for)
#
#


print("in for")
licznik_podejsc = 0
for i in range(30):
    print(f"wykonuję się {i}")
    print(f"podejście {licznik_podejsc}")
    if i % 2 == 0:
        continue
    licznik_podejsc += 1
    print("podaj hasło")
    if licznik_podejsc > 10:
        break

print("in while")
licznik_podejsc = 0
while True:
    print("podaj hasło")
    licznik_podejsc += 1
    if licznik_podejsc > 3:
        break
