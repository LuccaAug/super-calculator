import unittest

from physic.work import Work


class WorkTestCase(unittest.TestCase):
    work: Work

    def setUp(self) -> None:
        self.work = Work()

    def test_normal_value(self):
        self.work.force = 777
        self.work.distance = 13

        work = self.work.do_math()
        self.assertEqual(work, 10101)

    def test_zero_force(self):
        self.work.force = 0
        self.work.distance = 13

        work = self.work.do_math()
        self.assertEqual(work, 0)

    def test_zero_distance(self):
        self.work.force = 13
        self.work.distance = 0

        work = self.work.do_math()
        self.assertEqual(work, 0)


if __name__ == '__main__':
    unittest.main()
