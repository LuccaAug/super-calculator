import unittest

from trigonometric.cosecant import Cosecant


class CosecantTestCase(unittest.TestCase):
    cosecant: Cosecant

    def setUp(self) -> None:
        self.cosecant = Cosecant()

    def test_0_degree(self):
        self.cosecant.angle_degrees = 0

        self.assertRaises(ValueError, self.cosecant.do_math)

    def test_45_degree(self):
        self.cosecant.angle_degrees = 45

        cosecant = self.cosecant.do_math()
        self.assertEqual(cosecant, 1.41)

    def test_90_degree(self):
        self.cosecant.angle_degrees = 90

        cosecant = self.cosecant.do_math()
        self.assertEqual(cosecant, 1)


if __name__ == '__main__':
    unittest.main()
