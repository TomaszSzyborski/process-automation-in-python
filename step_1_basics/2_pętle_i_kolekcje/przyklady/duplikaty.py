# zwroc liste bez duplikatow

lista = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
print(lista)
for index in range(2,5):
    lista.pop(index)
print(lista)


lista_bez_duplikatow = []

for element in lista:
    if element not in lista_bez_duplikatow:
        lista_bez_duplikatow.append(element)

print("Lista bez duplikatów: ")
print(lista_bez_duplikatow)

zestaw = len(set(lista))
print(zestaw)