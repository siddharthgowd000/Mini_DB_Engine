import unittest
from db_engine import validate_input

class TestValidation(unittest.TestCase):
    def test_int(self):
        self.assertEqual(validate_input("5", "int"), 5)

    def test_float(self):
        self.assertEqual(validate_input("5.5", "float"), 5.5)

    def test_bool(self):
        self.assertTrue(validate_input("true", "bool"))
        self.assertFalse(validate_input("false", "bool"))

    def test_str(self):
        self.assertEqual(validate_input("hello", "str"), "hello")

if __name__ == '__main__':
    unittest.main()
