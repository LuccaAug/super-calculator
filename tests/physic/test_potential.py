import unittest

from physic.potential import Potential


class PotentialTestCase(unittest.TestCase):
    potential: Potential

    def setUp(self) -> None:
        self.potential = Potential()

    def test_normal_value(self):
        self.potential.mass = 13
        self.potential.height = 130

        potential = self.potential.do_math()
        self.assertEqual(potential, 16578.9)

    def test_zero_mass(self):
        self.potential.mass = 0
        self.potential.height = 13

        potential = self.potential.do_math()
        self.assertEqual(potential, 0)

    def test_zero_height(self):
        self.potential.mass = 13
        self.potential.height = 0

        potential = self.potential.do_math()
        self.assertEqual(potential, 0)


if __name__ == '__main__':
    unittest.main()
