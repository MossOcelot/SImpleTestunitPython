from  project import cats_and_a_mouse
import unittest

class Cats_mouse(unittest.TestCase):
    def test_1_2_3_should_cat_b(self):
        cat_a = 1
        cat_b = 2
        mouse_c = 3
        expected_result = "Cat B"

        result = cats_and_a_mouse.catAndMouse(cat_a,cat_b,mouse_c)
        self.assertEqual(expected_result, result)

    def test_40_50_60_should_cat_b(self):
        cat_a = 40
        cat_b = 50
        mouse_c = 60
        expected_result = "Cat B"

        result = cats_and_a_mouse.catAndMouse(cat_a,cat_b,mouse_c)
        self.assertEqual(expected_result, result)
    
    def test_80_90_100_should_cat_b(self):
        cat_a = 80
        cat_b = 90
        mouse_c = 100
        expected_result = "Cat B"

        result = cats_and_a_mouse.catAndMouse(cat_a,cat_b,mouse_c)
        self.assertEqual(expected_result, result)

