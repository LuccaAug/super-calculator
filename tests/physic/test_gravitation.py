import unittest

from physic.gravitation import Gravitation


class GravitationTestCase(unittest.TestCase):
    gravitation: Gravitation

    def setUp(self) -> None:
        self.gravitation = Gravitation()

    def test_normal_value(self):
        self.gravitation.mass1 = 667000
        self.gravitation.mass2 = 1000000
        self.gravitation.distance = 1

        gravitation = self.gravitation.do_math()
        self.assertEqual(gravitation, 44.49)

    def test_zero_mass(self):
        self.gravitation.mass1 = 0
        self.gravitation.mass2 = 777
        self.gravitation.distance = 13

        gravitation = self.gravitation.do_math()
        self.assertEqual(gravitation, 0)

    def test_distance_zero(self):
        self.gravitation.mass1 = 13
        self.gravitation.mass2 = 777
        self.gravitation.distance = 0

        self.assertRaises(ValueError, self.gravitation.do_math)


if __name__ == '__main__':
    unittest.main()
