import unittest

from trigonometric.tangent import Tangent


class TangentTestCase(unittest.TestCase):
    tangent: Tangent

    def setUp(self) -> None:
        self.tangent = Tangent()

    def test_normal_value(self):
        self.tangent.angle_degrees = 0

        tangent = self.tangent.do_math()
        self.assertEqual(tangent, 0)

    def test_undefined_tangent(self):
        self.tangent.angle_degrees = 450

        self.assertRaises(ValueError, self.tangent.do_math)


if __name__ == '__main__':
    unittest.main()
