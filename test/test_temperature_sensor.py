import unittest
from unittest import mock
from src.temperature_sensor import ValidateUserInput, ValidateTemperatures, RequiredCalculations

class TestTemperatureSensor(unittest.TestCase):

    # Test ValidateUserInput function
    def test_ValidateUserInput_valid(self):
        with mock.patch('builtins.input', return_value='5'):
            self.assertEqual(ValidateUserInput(), 5)

    def test_ValidateUserInput_invalid(self):
        with mock.patch('builtins.input', return_value='abc'):
            self.assertIsNone(ValidateUserInput())

    def test_ValidateUserInput_out_of_bound(self):
        with mock.patch('builtins.input', return_value='0'):
            self.assertIsNone(ValidateUserInput())

    # Test ValidateTemperatures function
    def test_ValidateTemperatures_valid(self):
        with mock.patch('builtins.input', side_effect=['20', '30', '40']):
            self.assertEqual(ValidateTemperatures(3), [20.0, 30.0, 40.0])

    def test_ValidateTemperatures_invalid(self):
        with mock.patch('builtins.input', side_effect=['20', 'abc', '30', '40']):
            self.assertEqual(ValidateTemperatures(3), [20.0, 30.0, 40.0])

    def test_RequiredCalculations_empty_list(self):
        with self.assertRaises(ValueError):
            RequiredCalculations([])

    def test_RequiredCalculations_single_value(self):
        temperatures = [50.0]
        self.assertEqual(RequiredCalculations(temperatures), (50.0, 50.0, 50.0))

    # Boundary Value Analysis (BVA)
    def test_BVA_min_boundary(self):
        with mock.patch('builtins.input', return_value='-50'):
            self.assertEqual(ValidateTemperatures(1), [-50.0])

    def test_BVA_max_boundary(self):
        with mock.patch('builtins.input', return_value='150'):
            self.assertEqual(ValidateTemperatures(1), [150.0])

    def test_BVA_near_boundary(self):
        with mock.patch('builtins.input', side_effect=['-49', '149']):
            self.assertEqual(ValidateTemperatures(2), [-49.0, 149.0])

    def test_Robustness_alphabetic_characters(self):
        with mock.patch('builtins.input', side_effect=['20', 'abc', '30', '40']):
            self.assertEqual(ValidateTemperatures(3), [20.0, 30.0, 40.0])

    def test_Robustness_special_characters(self):
        with mock.patch('builtins.input', side_effect=['10', '@', '-40', '20']):
            self.assertEqual(ValidateTemperatures(3), [10.0, -40.0, 20.0])

    # Special Scenarios
    def test_Special_large_input_values(self):
        temperatures = [2**31 - 1, -2**31]
        self.assertEqual(RequiredCalculations(temperatures), (-2**31, 2**31 - 1, (2**31 - 1 + -2**31) / 2))

    def test_Special_all_inputs_same(self):
        temperatures = [50.0, 50.0, 50.0]
        self.assertEqual(RequiredCalculations(temperatures), (50.0, 50.0, 50.0))

    def test_Special_empty_list(self):
        with self.assertRaises(ValueError):
            RequiredCalculations([])

    

if __name__ == '__main__':
    unittest.main()