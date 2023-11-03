import unittest

from trigonometric.secant import Secant


class SecantTestCase(unittest.TestCase):
    secant: Secant

    def setUp(self) -> None:
        self.secant = Secant()

    def test_0_degree(self):
        self.secant.angle_degrees = 0

        secant = self.secant.do_math()
        self.assertEqual(secant, 1)

    def test_45_degree(self):
        self.secant.angle_degrees = 45

        secant = self.secant.do_math()
        self.assertEqual(secant, 1.41)

    def test_90_degree(self):
        self.secant.angle_degrees = 90

        self.assertRaises(ValueError, self.secant.do_math)


if __name__ == '__main__':
    unittest.main()
