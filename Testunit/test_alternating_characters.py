from project import alternating_characters
import unittest

class AlternatingCharacters(unittest.TestCase):
    def test_AAAA_should_3(self):
        s = "AAAA"
        expected_result = 3

        result = alternating_characters.alternatingCharacters(s)
        self.assertEqual(expected_result,result)


    def test_BBBBB_should_4(self):
        s = "BBBBB"
        expect_result = 4

        result = alternating_characters.alternatingCharacters(s)
        self.assertEqual(expect_result,result)
    
    def test_ABABABAB_should_0(self):
        s = "ABABABAB"
        expect_result = 0

        result = alternating_characters.alternatingCharacters(s)
        self.assertEqual(expect_result,result)

    def test_AABBABABBBBBABBABABBBBABBABABABBABBABBBBAAABBBBBBBBBBBABBBBBBBABBBBBBBBBBBBABBABBBBAABBBBBAAAABBBBBB_should_62(self):
        s = "AABBABABBBBBABBABABBBBABBABABABBABBABBBBAAABBBBBBBBBBBABBBBBBBABBBBBBBBBBBBABBABBBBAABBBBBAAAABBBBBB"
        expect_result = 62

        result = alternating_characters.alternatingCharacters(s)
        self.assertEqual(expect_result,result)
    
    def test_ABBAABBBBBABBABBABBABAAABBBAABAAABAABBBABABAAABAAAABAAAAABAAAAAAABABAABBAABABABBABABAABAABAABABBBBAA_should_45(self):
        s = "ABBAABBBBBABBABBABBABAAABBBAABAAABAABBBABABAAABAAAABAAAAABAAAAAAABABAABBAABABABBABABAABAABAABABBBBAA"
        expect_result = 45

        result = alternating_characters.alternatingCharacters(s)
        self.assertEqual(expect_result,result)
    
    

