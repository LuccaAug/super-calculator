import unittest

from trigonometric.cotangent import Cotangent


class CotangentTestCase(unittest.TestCase):
    cotangent: Cotangent

    def setUp(self) -> None:
        self.cotangent = Cotangent()

    def test_normal_value(self):
        self.cotangent.angle_degrees = 45

        cotangent = self.cotangent.do_math()
        self.assertEqual(cotangent, 1)

    def test_undefined_cotangent(self):
        self.cotangent.angle_degrees = 720

        self.assertRaises(ValueError, self.cotangent.do_math)


if __name__ == '__main__':
    unittest.main()
