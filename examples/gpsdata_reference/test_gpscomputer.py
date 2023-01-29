import unittest

import gpscomputer


class TestComputerMethods(unittest.TestCase):
    ACCURACY = 0.5

    def setUp(self):
        self.gps_data = [
            (28800, 60.376988, 5.227082, 10),
            (28810, 60.385390, 5.217217, 20),
            (28840, 60.379527, 5.3227322, 10),
            (28870, 60.385390, 5.217217, 40),
            (28880, 60.376988, 5.227082, 50)]

    def test_total_distance(self):
        EXP_TOTALDISTANCE = 1080 + 5835 + 5835 + 1080

        self.assertAlmostEqual(gpscomputer.total_distance(self.gps_data), EXP_TOTALDISTANCE, delta=self.ACCURACY)

    def test_total_elevation(self):
        EXP_TOTALELEVATION = 10 + 30 + 10

        self.assertAlmostEqual(gpscomputer.total_elevation(self.gps_data), EXP_TOTALELEVATION, delta=self.ACCURACY)

    def total_time(self):
        EXP_TOTALTIME = 1 * 60 + 20

        self.assertAlmostEqual(gpscomputer.total_time(self.gps_data), EXP_TOTALTIME, delta=self.ACCURACY)

    def test_segment_speeds(self):
        EXP_SPEEDS = [(108.0 * 60 * 60) / 1000, (194.5 * 60 * 60) / 1000, (194.5 * 60 * 60) / 1000,
                      (108.0 * 60 * 60) / 1000]

        speeds = gpscomputer.segment_speeds(self.gps_data)

        self.assertEqual(len(speeds), len(EXP_SPEEDS))

        for i in range(1, len(EXP_SPEEDS)):
            self.assertAlmostEqual(speeds[i], EXP_SPEEDS[i], delta=self.ACCURACY)

    def test_max_speed(self):
        EXP_MAXSPEED = (194.5 * 60 * 60 / 1000)

        self.assertAlmostEqual(gpscomputer.max_speed(self.gps_data), EXP_MAXSPEED, delta=self.ACCURACY)

    def test_average_speed(self):
        EXP_TOTALDISTANCE = 1080 + 5835 + 5835 + 1080
        EXP_TOTALTIME = 1 * 60 + 20

        EXP_AVERAGESPEED = ((EXP_TOTALDISTANCE / EXP_TOTALTIME) * 60 * 60) / 1000

        self.assertAlmostEqual(gpscomputer.average_speed(self.gps_data), EXP_AVERAGESPEED, delta=self.ACCURACY)

    def test_kcal(self):
        MS = 2.236936

        self.assertAlmostEqual(gpscomputer.kcal(1.0, 1, 13.0 / MS), 8.0 / 3600.0, delta=self.ACCURACY)
        self.assertAlmostEqual(gpscomputer.kcal(2.0, 1, 13.0 / MS), 2 * 8.0 / 3600.0, delta=self.ACCURACY)
        self.assertAlmostEqual(gpscomputer.kcal(3.0, 2, 13.0 / MS), 3 * 2 * 8.0 / 3600.0, delta=self.ACCURACY)

    def test_total_energy(self):
        self.assertAlmostEqual(gpscomputer.total_energy(self.gps_data, 80.0), 24.88, delta=self.ACCURACY)


if __name__ == '__main__':
    unittest.main()
