import sys
from pathlib import Path
import unittest

thisfile = Path(__file__)
sys.path.append(str(thisfile.parent))


from exercises import *


class AoCTest(unittest.TestCase):

    def test_01_2025(self):
        input = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82\
        """
        dial = Dial()
        self.assertEqual(3, dial.obtain_password(input.split('\n')))


if __name__ == "__main__":
    unittest.main()
