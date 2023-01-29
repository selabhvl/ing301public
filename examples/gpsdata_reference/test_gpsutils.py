import unittest

import gpsutils

ACCURACY = 0.5


class TestUtilsMethods(unittest.TestCase):

    def test_find_max(self):
        da_start = [9.0, 1.0, 2.0, 6.0]
        da_middle = [1.0, 2.0, 7.0, 3.0]
        da_end = [1.0, 2.0, 7.0, 10.0]

        self.assertEqual(gpsutils.find_max(da_start), 9.0)
        self.assertEqual(gpsutils.find_max(da_middle), 7.0)
        self.assertEqual(gpsutils.find_max(da_end), 10.0)

    def test_find_min(self):
        da_start = [1.0, 2.0, 7.0, 3.0]
        da_middle = [9.0, 1.0, 2.0, 6.0]
        da_end = [2.0, 2.0, 7.0, 1.0]

        self.assertEqual(gpsutils.find_min(da_start), 1.0)
        self.assertEqual(gpsutils.find_min(da_middle), 1.0)
        self.assertEqual(gpsutils.find_min(da_end), 1.0)

    def test_distance(self):
        self.assertAlmostEqual(gpsutils.distance(60.385390, 5.217217, 60.379527, 5.3227322), 5835, delta=ACCURACY)
        self.assertAlmostEqual(gpsutils.distance(60.379527, 5.3227322, 60.385390, 5.217217), 5835, delta=ACCURACY)

        self.assertAlmostEqual(gpsutils.distance(60.385390, 5.217217, 60.376988, 5.227082), 1080, delta=ACCURACY)
        self.assertAlmostEqual(gpsutils.distance(60.376988, 5.227082, 60.385390, 5.217217), 1080, delta=ACCURACY)

        self.assertAlmostEqual(gpsutils.distance(60.376988, 5.227082, 60.376988, 5.227082), 0, delta=ACCURACY)

    def test_speed(self):
        self.assertAlmostEqual(gpsutils.speed(10, 60.385390, 5.217217, 60.376988, 5.227082), (108.0 * 60 * 60) / 1000,
                               delta=ACCURACY)


if __name__ == '__main__':
    unittest.main()
