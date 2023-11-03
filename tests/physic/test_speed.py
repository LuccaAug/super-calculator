import unittest

from physic.speed import Speed


class SpeedTestCase(unittest.TestCase):
    speed: Speed

    def setUp(self) -> None:
        self.speed = Speed()

    def test_normal_value(self):
        self.speed.time = 1.3
        self.speed.distance = 130

        speed = self.speed.do_math()
        self.assertEqual(speed, 100)

    def test_time_zero(self):
        self.speed.time = 0
        self.speed.distance = 130

        self.assertRaises(ValueError, self.speed.do_math)


if __name__ == '__main__':
    unittest.main()
