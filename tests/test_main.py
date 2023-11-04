import unittest

from medicine.medicine_calculator import MedicineCalculator
from main import MainMenu


class MyTestCase(unittest.TestCase):
    menu: MainMenu

    def setUp(self) -> None:
        self.menu = MainMenu()

    def test_number_of_options(self):
        options = self.menu.options.keys()
        len_options = len(options)

        self.assertEqual(len_options, 5)

    def test_exit(self):
        self.menu.define_area('E')
        self.assertFalse(self.menu.in_loop)

    def test_area(self):
        self.menu.define_area('M')
        self.assertIsInstance(self.menu.calculator_area, MedicineCalculator)


if __name__ == '__main__':
    unittest.main()
