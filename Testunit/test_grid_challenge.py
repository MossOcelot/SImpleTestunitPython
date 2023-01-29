from project import grid_challenge  
import unittest

class TestGrid_challenge(unittest.TestCase):
    def test_1_5_should_YES(self):
        grid = ['eabcd','fghij','olkmn','trpqs','xywuv']
        n = 5

        expect_result = "YES"
        result = grid_challenge.gridChallenge(n,grid)
        

        self.assertEqual(expect_result, result)
    
    def test_1_3_should_YES(self):
        grid = ['uxf','vof','hmp']
        n = 3

        expect_result = "NO"
        result = grid_challenge.gridChallenge(n,grid)

        self.assertEqual(expect_result, result)

    def test_1_2_should_YES(self):
        grid = ['kc','iu']
        n = 2

        expect_result = "YES"
        result = grid_challenge.gridChallenge(n,grid)

        self.assertEqual(expect_result, result)

    def test_1_3_should_YES(self):
        grid = ['ttt','zzz', 'zzz']
        n = 3

        expect_result = "YES"
        result = grid_challenge.gridChallenge(n,grid)

        self.assertEqual(expect_result, result)

    def test_1_7_should_YES(self):
        grid = ['zzzzzwz','zzzzzzw','wzzzzzz','zzwzzzz','zzyzzzz','zzzzyzz','zzzzzyz']
        n = 7

        expect_result = "YES"
        result = grid_challenge.gridChallenge(n,grid)

        self.assertEqual(expect_result, result)

    