import unittest

import dataconverter


class TestConverterMethods(unittest.TestCase):

    def test_convert_time(self):
        self.assertEqual(dataconverter.convert_time('2017-08-13T08:52:26.000Z'), 8*3600 + 60 * 52 + 26)

    def test_convert(self):

        gps_csv_data = [['2017-08-13T08:52:26.000Z', '60.385390', '5.217217', '61.9', '7.0', '219.93', '0.94605947', '0', 'gps', '1.02', '0.85', '1.33','','','','','100.0'],
                        ['2017-08-13T08:53:00.000Z', '60.385588', '5.217857', '56.2', '11.1', '0.0', '0.0', '0', 'gps', '2.22', '0.94', '2.41','','' ,'' , 'TILTING', '100.0']]

        gps_data = dataconverter.convert_data(gps_csv_data)

        gps_data_expected = [(26 + 60 * 52 + 60 * 60 * 8, 60.385390, 5.217217, 61.9),
                             (00 + 53 * 60 + 8 * 60 * 60, 60.385588, 5.217857, 56.2)]

        self.assertListEqual(gps_data, gps_data_expected)


if __name__ == '__main__':
    unittest.main()