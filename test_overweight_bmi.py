import unittest
from bmi_calc import bmi_check

class TestBMICalcOverweight(unittest.TestCase):
    
    def test_bmi_calc_overweight(self):
        self.assertEqual(bmi_check(40, 1.20), ('overweight', 27.8))
    
if __name__ == '__main__':
    unittest.main()