import unittest

from trigonometric.sine import Sine


class SineTestCase(unittest.TestCase):
    sine: Sine

    def setUp(self) -> None:
        self.sine = Sine()

    def test_0_degree(self):
        self.sine.angle_degrees = 0

        sine = self.sine.do_math()
        self.assertEqual(sine, 0)

    def test_45_degree(self):
        self.sine.angle_degrees = 45

        sine = self.sine.do_math()
        self.assertEqual(sine, 0.71)

    def test_90_degree(self):
        self.sine.angle_degrees = 90

        sine = self.sine.do_math()
        self.assertEqual(sine, 1)


if __name__ == '__main__':
    unittest.main()
