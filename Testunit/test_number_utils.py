from project import number_utils  
import unittest

class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = number_utils.is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_5_6_7_is_not_prime(self):
        prime_list = [5,6,7]
        is_prime = number_utils.is_prime_list(prime_list)

        self.assertFalse(is_prime)

    def test_give_47_53_59_is_prime(self):
        prime_list = [47,53,59]
        is_prime = number_utils.is_prime_list(prime_list)

        self.assertTrue(is_prime)

    def test_give_7_8_9_is_not_prime(self):
        prime_list = [7,8,9]
        is_prime = number_utils.is_prime_list(prime_list)

        self.assertFalse(is_prime)

    def test_give_61_62_63_is_not_prime(self):
        prime_list = [61,62,63]
        is_prime = number_utils.is_prime_list(prime_list)

        self.assertFalse(is_prime)

    def test_give_71_73_79_is_prime(self):
        prime_list = [71,73,79]
        is_prime = number_utils.is_prime_list(prime_list)

        self.assertTrue(is_prime)

    def test_give_83_89_97_is_prime(self):
        prime_list = [83,89,97]
        is_prime = number_utils.is_prime_list(prime_list)

        self.assertTrue(is_prime)