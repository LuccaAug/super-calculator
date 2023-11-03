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


if __name__ == '__main__':
    unittest.main()
