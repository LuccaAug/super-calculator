import unittest

from trigonometric.tangent import Tangent


class TangentTestCase(unittest.TestCase):
    tangent: Tangent

    def setUp(self) -> None:
        self.tangent = Tangent()

    def test_0_degree(self):
        self.tangent.angle_degrees = 0

        tangent = self.tangent.do_math()
        self.assertEqual(tangent, 0)

    def test_45_degree(self):
        self.tangent.angle_degrees = 45

        tangent = self.tangent.do_math()
        self.assertEqual(tangent, 1)

    def test_90_degree(self):
        self.tangent.angle_degrees = 90

        self.assertRaises(ValueError, self.tangent.do_math)


if __name__ == '__main__':
    unittest.main()
