from  project import FizzBuzz
import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_give_3_should_Fizz(self):
        number = 3
        expect_result = "Fizz"

        result = FizzBuzz.fizzbuzz(number)
        self.assertEqual(expect_result,result)

    def test_give_5_should_Buzz(self):
        number = 5
        expect_result = "Buzz"

        result = FizzBuzz.fizzbuzz(number)
        self.assertEqual(expect_result,result)

    def test_give_15_should_FizzBuzz(self):
        number = 15
        expect_result = "FizzBuzz"

        result = FizzBuzz.fizzbuzz(number)
        self.assertEqual(expect_result,result)

    def test_give_50_should_Buzz(self):
        number = 50
        expect_result = "Buzz"

        result = FizzBuzz.fizzbuzz(number)
        self.assertEqual(expect_result,result)

    def test_give_90_should_FizzBuzz(self):
        number = 90
        expect_result = "FizzBuzz"

        result = FizzBuzz.fizzbuzz(number)
        self.assertEqual(expect_result,result)

    def test_give_95_should_FizzBuzz(self):
        number = 95
        expect_result = "Buzz"

        result = FizzBuzz.fizzbuzz(number)
        self.assertEqual(expect_result,result)

    def test_give_99_should_FizzBuzz(self):
        number = 99
        expect_result = "Fizz"

        result = FizzBuzz.fizzbuzz(number)
        self.assertEqual(expect_result,result)


