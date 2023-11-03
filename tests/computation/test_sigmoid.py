import unittest

from computation.sigmoid import Sigmoid


class SigmoidTestCase(unittest.TestCase):
    sigmoid: Sigmoid

    def setUp(self) -> None:
        self.sigmoid = Sigmoid()

    def test_normal_value(self):
        self.sigmoid.input = 0.13
        value = self.sigmoid.do_math()
        self.assertEqual(value, 0.53)

    def test_giant_value(self):
        self.sigmoid.input = 13131313
        value = self.sigmoid.do_math()
        self.assertEqual(value, 1)

    def test_giant_negative_value(self):
        self.sigmoid.input = -100
        value = self.sigmoid.do_math()
        self.assertEqual(value, 0)


if __name__ == '__main__':
    unittest.main()
