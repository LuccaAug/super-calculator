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


if __name__ == '__main__':
    unittest.main()
