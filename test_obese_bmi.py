import unittest
from bmi_calc import bmi_check

class TestObeseBMI(unittest.TestCase):
 
    def test_bmi_just_below_40(self):
        self.assertEqual(bmi_check(109, 1.70)[0], "obese")

if __name__ == '__main__':
    unittest.main()