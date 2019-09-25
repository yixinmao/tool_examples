
import unittest
import mytry.string

class TestMathModule(unittest.TestCase):

    def setUp(self):
        '''Set up some variables that can be used across all test methods'''
        self.s = 'My String'

    def test_upper(self):
        self.assertEqual(mytry.string.upper(self.s), 'MY STRING')
        self.assertEqual(mytry.string.upper('abc'), 'ABC')

    def test_lower(self):
        self.assertEqual(mytry.string.lower(self.s), 'my string')
        self.assertEqual(mytry.string.lower('ABC'), 'abc')

