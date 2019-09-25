
import unittest
import mytry.math

class TestMathModule(unittest.TestCase):

    def setUp(self):
        '''Set up some variables that can be used across all test methods'''
        self.a = 2
        self.b = 4

    def test_add(self):  # Method name must start with "test"
        self.assertEqual(mytry.math.add_two_numbers(self.a, self.b), 6)
        self.assertEqual(mytry.math.add_two_numbers(-1, 2), 1)

    def test_multiply(self):
        self.assertEqual(mytry.math.multiply_two_numbers(self.a, self.b), 8)
        self.assertEqual(mytry.math.multiply_two_numbers(-1, 2), -2)


#if __name__ == '__main__':
#    unittest.main()
