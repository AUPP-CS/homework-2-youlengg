import unittest
from bmi_calc import bmi_check

class TestExtremelyObeseBMI(unittest.TestCase):
    
    def test_bmi_exactly_at_40(self):
        self.assertEqual(bmi_check(116, 1.70), ("extremely obese", 40.1))

    def test_bmi_just_above_40(self):
        self.assertEqual(bmi_check(120, 1.70), ("extremely obese", 41.5))

if __name__ == '__main__':
    unittest.main()