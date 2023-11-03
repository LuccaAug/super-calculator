import unittest

from trigonometric.cosine import Cosine


class CosineTestCase(unittest.TestCase):
    cosine: Cosine

    def setUp(self) -> None:
        self.cosine = Cosine()

    def test_normal_value(self):
        self.cosine.angle_degrees = 0

        cosine = self.cosine.do_math()
        self.assertEqual(cosine, 1)


if __name__ == '__main__':
    unittest.main()
