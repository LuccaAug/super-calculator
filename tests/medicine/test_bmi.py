import unittest

from medicine.bmi import BMI


class BMITestCase(unittest.TestCase):
    bmi: BMI

    def setUp(self) -> None:
        self.bmi = BMI()

    def test_normal_values(self):
        self.bmi.height = 1.9
        self.bmi.weight = 78

        bmi = 21.61
        self.assertEqual(self.bmi.do_math(), bmi)


if __name__ == '__main__':
    unittest.main()
