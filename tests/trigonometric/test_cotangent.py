import unittest

from trigonometric.cotangent import Cotangent


class CotangentTestCase(unittest.TestCase):
    cotangent: Cotangent

    def setUp(self) -> None:
        self.cotangent = Cotangent()

    def test_0_degree(self):
        self.cotangent.angle_degrees = 0

        self.assertRaises(ValueError, self.cotangent.do_math)

    def test_45_degree(self):
        self.cotangent.angle_degrees = 45

        cotangent = self.cotangent.do_math()
        self.assertEqual(cotangent, 1)

    def test_90_degree(self):
        self.cotangent.angle_degrees = 90

        cotangent = self.cotangent.do_math()
        self.assertEqual(cotangent, 0)


if __name__ == '__main__':
    unittest.main()
