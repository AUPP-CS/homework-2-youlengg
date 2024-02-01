import unittest
from bmi_calc import bmi_check

class TestNormalBMI(unittest.TestCase):

    def test_bmi_just_above_18_5(self):
        weight = 54
        height = 1.70
        self.assertEqual(bmi_check(weight, height), ('normal', 18.7))


if __name__ == '__main__':
    unittest.main()