import unittest
import exercise1

class TestExercise1(unittest.TestCase):

    def test_max_pair(self):
        self.assertEqual(exercise1.max_pair(('Hallo',3),("World",5)), ("World",5))
        self.assertEqual(exercise1.max_pair(('Hei',0), ('Hei',0), ('Hei',0)))
        self.assertEqual(exercise1.max_pair(('smaller',-10), ('larger',10), ('larger',10)))
    
    def test_make_index(self):
        input = ['the', 'quick', 'brown', 'fox', 'the', 'jumps', 'over', 'the', 'brown', 'wall']
        expected = {
            'fox' : 1,
            'brown' : 2,
            'the' : 3,
            'quick' : 1,
            'jumps' : 1,
            'wall' : 1
        }
        self.assertEqual(exercise1.make_index(input), expected)
    

    def test_make_index_capitals(self):
        self.assertEqual(exercise1.make_index(['world', 'WoRlD', 'WORLD']), {'world' :3 })


    def test_make_index_corner_cases(self):
        self.assertEqual(exercise1.make_index([]), {})
        self.assertEqual(exercise1.make_index(['hei', 'verden', 'hei']), { 'hei': 2, 'verden': 1})


    def test_clear_index(self):
        input = {
            'det' : 42,
            'odin' : 10,
            'og' : 9,
            'ulv' : 1,
            'til' : 1,
            'gud' : 3
        }
        expected = {
            'odin' : 10,
            'ulv' : 1,
            'gud' : 3
        }
        self.assertEqual(exercise1.clear_index(input), expected)


if __name__ == '__main__':
    unittest.main()
    

