import unittest

from trigonometric.cosecant import Cosecant


class CosecantTestCase(unittest.TestCase):
    cosecant: Cosecant

    def setUp(self) -> None:
        self.cosecant = Cosecant()

    def test_normal_value(self):
        self.cosecant.angle_degrees = 90

        cosecant = self.cosecant.do_math()
        self.assertEqual(cosecant, 1)

    def test_undefined_cosecant(self):
        self.cosecant.angle_degrees = 180

        self.assertRaises(ValueError, self.cosecant.do_math)


if __name__ == '__main__':
    unittest.main()
