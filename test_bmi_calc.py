import unittest
from bmi_calc import bmi_check


class BMI(unittest.TestCase):
    def test_return_data_type(self):
        self.assertIsInstance(bmi_check(52, 1.3), tuple)

    def test_bmi_calc(self):
        self.assertEqual(bmi_check(67, 1.68), ("normal", 23.74))
        self.assertEqual(bmi_check(66, 1.20), ('extremely obese', 45.83))
        self.assertEqual(bmi_check(10, 0.90), ('underweight', 12.35))
        self.assertEqual(bmi_check(40, 1.20), ('overweight', 27.78))
        self.assertEqual(bmi_check(50, 1.20), ('obese', 34.72))

    def test_bmi_error(self):
        self.assertEqual(bmi_check("67", 1.68), ("invalid input", 1))
        self.assertEqual(bmi_check("67", "1.68"), ("invalid input", 1))
        self.assertEqual(bmi_check(67, "1.68"), ("invalid input", 1))
        self.assertEqual(bmi_check(636, 1.7), ("unrealistic information", 2))
        self.assertEqual(bmi_check(67, 3), ("unrealistic information", 2))


if __name__ == '__main__':
    unittest.main()
