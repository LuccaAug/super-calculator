import unittest

from physic.kinetic import Kinetic


class KineticTestCase(unittest.TestCase):
    kinetic: Kinetic

    def setUp(self) -> None:
        self.kinetic = Kinetic()

    def test_normal_value(self):
        self.kinetic.mass = 777
        self.kinetic.velocity = 130

        kinetic = self.kinetic.do_math()
        self.assertEqual(kinetic, 6565650)


if __name__ == '__main__':
    unittest.main()
