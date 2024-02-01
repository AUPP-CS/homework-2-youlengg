import unittest
from bmi_calc import bmi_check

class TestInvalidBMI(unittest.TestCase):
    
    def test_bmi_just_below_0(self):
        self.assertEqual(bmi_check(-1, 1.70), "invalid input")

    def test_bmi_exactly_at_0(self):
        self.assertEqual(bmi_check(0, 1.70), "invalid input")
        
if __name__ == '__main__':
    unittest.main()