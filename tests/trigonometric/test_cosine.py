import unittest

from trigonometric.cosine import Cosine


class CosineTestCase(unittest.TestCase):
    cosine: Cosine

    def setUp(self) -> None:
        self.cosine = Cosine()

    def test_0_degree(self):
        self.cosine.angle_degrees = 0

        cosine = self.cosine.do_math()
        self.assertEqual(cosine, 1)

    def test_45_degree(self):
        self.cosine.angle_degrees = 45

        cosine = self.cosine.do_math()
        self.assertEqual(cosine, 0.71)

    def test_90_degree(self):
        self.cosine.angle_degrees = 90

        cosine = self.cosine.do_math()
        self.assertEqual(cosine, 0)


if __name__ == '__main__':
    unittest.main()
