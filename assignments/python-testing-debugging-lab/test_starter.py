# Tests for Python Testing and Debugging Lab

import importlib.util
import pathlib
import unittest


MODULE_PATH = pathlib.Path(__file__).with_name("starter-code.py")
SPEC = importlib.util.spec_from_file_location("starter_code", MODULE_PATH)
starter_code = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(starter_code)


class TestStarterCode(unittest.TestCase):
    def test_calculate_average_typical(self):
        self.assertAlmostEqual(starter_code.calculate_average([70, 80, 90]), 80.0)

    def test_calculate_average_empty_list(self):
        self.assertEqual(starter_code.calculate_average([]), 0.0)

    def test_is_strong_password_valid(self):
        self.assertTrue(starter_code.is_strong_password("learning9"))

    def test_is_strong_password_too_short(self):
        self.assertFalse(starter_code.is_strong_password("abc1"))

    def test_is_strong_password_no_digit(self):
        self.assertFalse(starter_code.is_strong_password("longpassword"))

    def test_format_username_basic(self):
        self.assertEqual(starter_code.format_username("Ada", "Lovelace"), "alovelace")

    def test_format_username_with_spaces(self):
        self.assertEqual(starter_code.format_username("  Grace ", " Hopper  "), "ghopper")


if __name__ == "__main__":
    unittest.main()
