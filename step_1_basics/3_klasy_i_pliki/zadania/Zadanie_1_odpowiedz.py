"""
Wymagania:
Napisz klasę mającą dwie metody:
- get_string
- print_string

get_string - pobiera od użytkownika stringa
print_string - wypisuje stringa na ekran - co druga litera powinna być wielka.

Przykład:
asdasdasdasd -> 'AsDaSdAsDaSd'
"""


class IOString:
    def __init__(self):
        self.class_string = ""

    def get_string(self):
        self.class_string = input("Podaj string: ")

    def print_string(self):
        lista = []
        for i, letter in enumerate(self.class_string):
            if i%2==0:
                lista.append(letter.upper())
            else:
                lista.append(letter.lower())

        print("".join(lista))

str1 = IOString()
str1.get_string()
str1.print_string()

# # ver2
# class IOString(object):
#     def __init__(self):
#         self.class_string = ""
#
#     def get_string(self):
#         self.class_string = input("Podaj string: ")
#
#     def print_string(self):
#         lista = [letter.lower() if i % 2 else letter.upper() for i, letter in enumerate(self.class_string)]
#         print("".join(lista))
#
#
# str1 = IOString()
# str1.get_string()
# str1.print_string()


# # ver3
# class IOString(object):
#     def __init__(self):
#         self.class_string = ""
#
#     def get_string(self):
#         self.class_string = input("Podaj string: ")
#
#     def print_string(self):
#         lista = list(map((lambda item: item[karty].lower() if item[0] % 2 else item[karty].upper()), enumerate(self.class_string)))
#         print("".join(lista))
#
#
# str1 = IOString()
# str1.get_string()
# str1.print_string()

# ver4
# from itertools import chain
#
# class IOString(object):
#     def __init__(self):
#         self.class_string = ""
#
#     def get_string(self):
#         self.class_string = input("Podaj string: ")
#
#     def print_string(self):
#         small = self.class_string[karty::2].lower()
#         big = self.class_string[::2].upper()
#         lista = list(chain(*zip(big, small)))
#         print("".join(lista))
#
#
# str1 = IOString()
# str1.get_string()
# str1.print_string()
