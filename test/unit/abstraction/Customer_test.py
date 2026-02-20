import unittest
import sys
from pathlib import Path

_parent_dir = Path(__file__).parent.parent.parent.parent.resolve()
sys.path.insert(0, str(_parent_dir))
from abstraction.Customer import Customer

class CustomerTest(unittest.TestCase):
    def setUp(self):
        self.customer = Customer()

    def test_assert_raises_fullname_value_error(self):
       with self.assertRaises(ValueError):
           self.customer.fullname = None
           self.customer.fullname = ""

    def test_assert_raises_email_value_error(self):
       with self.assertRaises(ValueError):
           self.customer.email = None
           self.customer.email = ""

    def test_assert_raises_phone_value_error(self):
       with self.assertRaises(ValueError):
           self.customer.phone = None
           self.customer.phone = ""

if __name__ == '__main__':
    unittest.main()