from pprint import pprint

from faker import Faker

fake = Faker()
with open("plik.txt", "w" ) as f: #parametr 'w' czysci plik i zapisuje dane
    lines = '\n'.join([fake.text() for _ in range(100)])
    f.writelines(lines)


# with open("plik.txt", "a" ) as f: #parametr 'a' zapisuje dane na koniec pliku
#     lines = '\n'.join([fake.text() for _ in range(100)])
#     f.writelines(lines)
#
#
# with open("plik.txt", "r" ) as f: #parametr 'a' czyta plik
#     output = f.readlines()
#     pprint(output)
#