from pprint import pprint

from faker import Faker

fake = Faker()

# with open("plik.txt", "w") as f: # utworzy/otworzy wyczyści lik w całości i zapisuje dane
#     lines = '\n'.join([fake.text() for _ in range(100)])
#     f.writelines(lines)

#
# with open("plik.txt", "a") as f: # otwaorzy plik i doda dane na samym końcu
#     lines = '\n'.join([fake.text() for _ in range(100)])
#     f.writelines(lines)

#
with open("plik.txt", "r") as f: # otwaorzy plik i go odczyta
    lines = f.readlines()
    pprint(lines)