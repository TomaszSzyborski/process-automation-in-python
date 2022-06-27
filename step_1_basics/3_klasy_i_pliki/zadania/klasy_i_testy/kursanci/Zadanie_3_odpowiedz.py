"""
Wymagnia:
Zapimportuj klasę Kursant a następnie przetestuj ustawianie i odczytywanie propertisów

Użyj unittest do testowania metod w klasie
Użyj modułów random oraz string, żeby losować dane (np. imię)

Napisz klasy_i_testy pozytywne i negatywne (z prawidłowymi danymi i nieprawidłowymi)

Dla chętnych:
oprócz zwykłych testów jednostkowych napisz klasy_i_testy używając podejścia data driven testing
"""

import unittest
import random
import string

from .Zadanie_1_odpowiedz import Kursant


class KursantTest(unittest.TestCase):

    def setUp(self):
        self.random_name = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        self.instance_under_test = Kursant(self.random_name)

    def test_read_name(self):
        self.assertEqual(
            self.instance_under_test.imie,
            self.random_name,
        msg="Odczytane imię jest zgodne z wprowadzonym")

    def test_default_odrobiona_praca_domowa(self):
        self.assertFalse(
            self.instance_under_test.odrobiona_praca_domowa,
        msg="Domyślna praca domowa jest ustawiona na False")

    def test_default_obecnosc(self):
        self.assertTrue(
            self.instance_under_test.obecnosc,
        msg="Domyślna obecnosc jest ustawiona na True")

    def test_default_punkty_z_egzaminu(self):
        self.assertIsNone(
            self.instance_under_test.punkty_z_egzaminu,
        msg="Domyślne punkty z egzaminu są ustawione Na none")

    def test_set_odrobiona_praca_domowa_as_true(self):
        self.instance_under_test.odrobiona_praca_domowa = True

        self.assertTrue(
            self.instance_under_test.odrobiona_praca_domowa,
        msg="Odrobiona praca domowa została ustawiona na True")

    def test_set_odrobiona_praca_domowa_as_false(self):
        self.instance_under_test.odrobiona_praca_domowa = False

        self.assertFalse(
            self.instance_under_test.odrobiona_praca_domowa,
        msg="Odrobiona praca domowa została ustawiona na False")



    def test_set_obecnosc_as_true(self):
        self.instance_under_test.obecnosc = True

        self.assertTrue(
            self.instance_under_test.obecnosc,
        msg="Obecność została ustawiona na True")

    def test_set_obecnosc_as_false(self):
        self.instance_under_test.obecnosc = False

        self.assertFalse(
            self.instance_under_test.obecnosc,
        msg="Obecność została ustawiona na False")

    def test_set_punkty_z_egzaminu_as_10(self):
        self.instance_under_test.punkty_z_egzaminu = 10

        self.assertEqual(
            self.instance_under_test.punkty_z_egzaminu,
            10,
        msg="Punkty z egzaminu zostały ustawione na -10")

    def test_set_punkty_z_egzaminu_as_minus_10(self):
        self.instance_under_test.punkty_z_egzaminu = -10

        self.assertEqual(
            self.instance_under_test.punkty_z_egzaminu,
            -10,
        msg="Punkty z egzaminu zostały ustawione na -10")


if __name__ == '__main__':
    unittest.main()
