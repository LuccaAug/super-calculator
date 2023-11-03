import unittest

from medicine.bmi import BMI


class BMITestCase(unittest.TestCase):
    bmi: BMI

    def setUp(self) -> None:
        self.bmi = BMI()

    def test_normal_value(self):
        self.bmi.height = 1.9
        self.bmi.weight = 78

        bmi = self.bmi.do_math()
        self.assertEqual(bmi, 21.61)


if __name__ == '__main__':
    unittest.main()
