import unittest
from bmi_calc import bmi_check

class TestNegativeBMI(unittest.TestCase):
    def test_negative_weight(self):
        self.assertEqual(bmi_check(-67, 1.68), "invalid input")

    def test_negative_height(self):
        self.assertEqual(bmi_check(67, -1.68), "invalid input")

    def test_negative_weight_and_height(self):
        self.assertEqual(bmi_check(-67, -1.68), "invalid input")

if __name__ == '__main__':
    unittest.main()