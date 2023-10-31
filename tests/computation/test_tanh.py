import unittest

from computation.tanh import TanH


class TanHTestCase(unittest.TestCase):
    tanh: TanH

    def setUp(self) -> None:
        self.tanh = TanH()

    def test_normal_value(self):
        self.tanh.input = 0.13
        value = self.tanh.do_math()
        self.assertEqual(value, 0.12927258360605834)


if __name__ == '__main__':
    unittest.main()
