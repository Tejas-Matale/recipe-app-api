from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_sub_number(self):
        res = calc.sub(10, 15)
        self.assertEqual(res, -5)
