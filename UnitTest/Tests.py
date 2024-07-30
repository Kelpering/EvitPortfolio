import unittest
from Calc import Calculator

class TestCalc(unittest.TestCase):
    def test_add(self):
        res = Calculator.Add(3,1)
        self.assertEqual(res, 4, 'Add')

    def test_sub(self):
        res = Calculator.Sub(1,1)
        self.assertEqual(res, 0, 'Sub')
    
    def test_mul(self):
        res = Calculator.Mul(4,2)
        self.assertEqual(res, 8, 'Mul')

    def test_div(self):
        res = Calculator.Div(14,7)
        self.assertEqual(res, 2, 'Div')
    
    def test_div_zero(self):
        res = Calculator.Div(14,0)
        self.assertEqual(res, 0, 'Div')


if __name__ == "__main__":
    unittest.main()