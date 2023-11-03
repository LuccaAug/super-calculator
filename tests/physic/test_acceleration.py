import unittest

from physic.acceleration import Acceleration


class AccelerationTestCase(unittest.TestCase):
    acceleration: Acceleration

    def setUp(self) -> None:
        self.acceleration = Acceleration()

    def test_normal_value(self):
        self.acceleration.time = 1.3
        self.acceleration.initial_velocity = 0
        self.acceleration.final_velocity = 130

        acceleration = self.acceleration.do_math()
        self.assertEqual(acceleration, 100)

    def test_zero_value(self):
        self.acceleration.time = 1.3
        self.acceleration.initial_velocity = 0
        self.acceleration.final_velocity = 0

        acceleration = self.acceleration.do_math()
        self.assertEqual(acceleration, 0)

    def test_time_zero(self):
        self.acceleration.time = 0
        self.acceleration.initial_velocity = 0
        self.acceleration.final_velocity = 130

        self.assertRaises(ValueError, self.acceleration.do_math)


if __name__ == '__main__':
    unittest.main()
