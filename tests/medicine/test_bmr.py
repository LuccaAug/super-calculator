import unittest

from medicine.bmr import BMR


class BMRTestCase(unittest.TestCase):
    bmr: BMR

    def setUp(self) -> None:
        self.bmr = BMR()

    def test_man_constants(self):
        self.bmr.set_constants_for_man()

        self.assertEqual(self.bmr.k, 88.362)
        self.assertEqual(self.bmr.k_weight, 13.397)
        self.assertEqual(self.bmr.k_height, 4.799)
        self.assertEqual(self.bmr.k_age, 5.677)

    def test_woman_constants(self):
        self.bmr.set_constants_for_woman()

        self.assertEqual(self.bmr.k, 447.593)
        self.assertEqual(self.bmr.k_weight, 9.247)
        self.assertEqual(self.bmr.k_height, 3.098)
        self.assertEqual(self.bmr.k_age, 4.330)

    def test_normal_values_for_man(self):
        self.bmr.set_constants_for_man()
        self.bmr.age = 23
        self.bmr.height = 190
        self.bmr.weight = 78

        bmr = self.bmr.do_math()
        self.assertEqual(bmr, 1914.57)

    def test_normal_values_for_woman(self):
        self.bmr.set_constants_for_woman()
        self.bmr.age = 23
        self.bmr.height = 160
        self.bmr.weight = 58

        bmr = self.bmr.do_math()
        self.assertEqual(bmr, 1380.01)


if __name__ == '__main__':
    unittest.main()
