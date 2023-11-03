import unittest

from computation.relu import ReLU


class ReLUTestCase(unittest.TestCase):
    relu: ReLU

    def setUp(self) -> None:
        self.relu = ReLU()

    def test_zero_value(self):
        self.relu.input = 0
        value = self.relu.do_math()
        self.assertEqual(value, 0)

    def test_negative_value(self):
        self.relu.input = -13
        value = self.relu.do_math()
        self.assertEqual(value, 0)

    def test_positive_value(self):
        self.relu.input = 13
        value = self.relu.do_math()
        self.assertEqual(value, 13)


if __name__ == '__main__':
    unittest.main()
