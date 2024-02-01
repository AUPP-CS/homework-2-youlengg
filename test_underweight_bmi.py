import unittest
from bmi_calc import bmi_check

class TestUnderweightBMI(unittest.TestCase):
    
    def test_bmi_just_under_18_5(self):
        weight = 50
        height = 1.70
        self.assertEqual(bmi_check(weight, height), ('underweight', 17.3))

if __name__ == '__main__':
    unittest.main()