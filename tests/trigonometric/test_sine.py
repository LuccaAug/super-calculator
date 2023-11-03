import unittest

from trigonometric.sine import Sine


class SineTestCase(unittest.TestCase):
    sine: Sine

    def setUp(self) -> None:
        self.sine = Sine()

    def test_normal_value(self):
        self.sine.angle_degrees = 90

        sine = self.sine.do_math()
        self.assertEqual(sine, 1)


if __name__ == '__main__':
    unittest.main()
