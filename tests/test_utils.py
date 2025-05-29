import unittest
from skillswap.utils import validate_non_empty_string, validate_email, find_by_attribute

class TestUtils(unittest.TestCase):

    def test_validate_non_empty_string(self):
        with self.assertRaises(ValueError):
            validate_non_empty_string("", "Name")
        with self.assertRaises(ValueError):
            validate_non_empty_string("   ", "Name")
        self.assertIsNone(validate_non_empty_string("Valid", "Name"))

    def test_validate_email(self):
        with self.assertRaises(ValueError):
            validate_email("invalidemail")
        with self.assertRaises(ValueError):
            validate_email("@example.com")
        self.assertIsNone(validate_email("valid@example.com"))

    def test_find_by_attribute(self):
        objects = [
            type("MockObject", (object,), {"id": "1", "name": "Alice"})(),
            type("MockObject", (object,), {"id": "2", "name": "Bob"})()
        ]
        self.assertEqual(find_by_attribute(objects, "id", "1").name, "Alice")
        self.assertEqual(find_by_attribute(objects, "name", "Bob").id, "2")
        self.assertIsNone(find_by_attribute(objects, "id", "3"))

if __name__ == "__main__":
    unittest.main()