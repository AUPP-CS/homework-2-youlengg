import unittest
from bmi_calc import bmi_check

class TestUnrealisticBMI(unittest.TestCase):
    
    def test_very_high_bmi(self):
        self.assertEqual(bmi_check(636, 1.7), "unrealistic information")

if __name__ == '__main__':
    unittest.main()