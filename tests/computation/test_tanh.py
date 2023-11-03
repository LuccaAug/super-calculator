import unittest

from computation.tanh import TanH


class TanHTestCase(unittest.TestCase):
    tanh: TanH

    def setUp(self) -> None:
        self.tanh = TanH()

    def test_normal_value(self):
        self.tanh.input = 0.13
        value = self.tanh.do_math()
        self.assertEqual(value, 0.13)

    def test_zero_value(self):
        self.tanh.input = 0
        value = self.tanh.do_math()
        self.assertEqual(value, 0)

    def test_giant_value(self):
        self.tanh.input = 13131313
        value = self.tanh.do_math()
        self.assertEqual(value, 1)

    def test_giant_negative_value(self):
        self.tanh.input = -13131313
        value = self.tanh.do_math()
        self.assertEqual(value, -1)


if __name__ == '__main__':
    unittest.main()
