import unittest

from main import Calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        '''Test case function for addition'''
        self.calc = Calculator()
        result = self.calc.add(4, 7)
        expected = 11
        self.assertEqual(result, expected)

    def test_sub(self):
        '''Test case function for subtraction'''
        self.calc = Calculator()
        result = self.calc.sub(10, 5)
        expected = 5
        self.assertEqual(result, expected)

    def test_mul(self):
        '''Test case function for multiplication'''
        self.calc = Calculator()
        result = self.calc.mul(3, 7)
        expected = 21
        self.assertEqual(result, expected)

    def test_div(self):
        '''Test case function for division'''
        self.calc = Calculator()
        result = self.calc.div(10, 2)
        expected = 4
        self.assertEqual(result, expected)

    def test_sqr(self):
        '''Test case function for division'''
        self.calc = Calculator()
        result = self.calc.sqr(10)
        expected = 100
        self.assertEqual(result, expected)

    def test_sqr(self):
        self.calc = Calculator()
        result = self.calc.sqrt(100)
        expected = 10
        self.assertEqual(result, expected)