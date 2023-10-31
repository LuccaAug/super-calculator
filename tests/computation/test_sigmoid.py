import unittest

from computation.sigmoid import Sigmoid


class SigmoidTestCase(unittest.TestCase):
    sigmoid: Sigmoid

    def setUp(self) -> None:
        self.sigmoid = Sigmoid()

    def test_normal_value(self):
        self.sigmoid.input = 0.13
        value = self.sigmoid.do_math()
        self.assertEqual(value, 0.5324543063873187)


if __name__ == '__main__':
    unittest.main()
