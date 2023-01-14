from  project import funny_string
import unittest

class FunnyString(unittest.TestCase):
    def test_acxz_should_Funny(self):
        s = "acxz"
        expected_result = "Funny"
        result = funny_string.funnyString(s)
        self.assertEqual(expected_result, result)

    def test_bcxz_should_Not_Funny(self):
        s = "bcxz"
        expected_result = "Not Funny"
        result = funny_string.funnyString(s)
        self.assertEqual(expected_result, result)
    
    def test_ivvkxq_should_Not_Funny(self):
        s = "ivvkxq"
        expected_result = "Not Funny"
        result = funny_string.funnyString(s)
        self.assertEqual(expected_result, result)
    
    def test_ivvkx_should_Not_Funny(self):
        s = "ivvkx"
        expected_result = "Not Funny"
        result = funny_string.funnyString(s)
        self.assertEqual(expected_result, result)

    def test_jkotzxzxrxtzytlruwrxytyzsuzytwyzxuzytryzuzysxvsmupouysywywqlhg_shoud_Funny(self):
        s = "jkotzxzxrxtzytlruwrxytyzsuzytwyzxuzytryzuzysxvsmupouysywywqlhg"
        expected_result = "Funny"
        result = funny_string.funnyString(s)
        self.assertEqual(expected_result, result)