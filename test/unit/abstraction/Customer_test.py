import unittest
import sys
from pathlib import Path

_parent_dir = Path(__file__).parent.parent.parent.parent.resolve()
sys.path.insert(0, str(_parent_dir))
from abstraction.Customer import Customer
from setting.Setting import Setting

class CustomerTest(unittest.TestCase):
    def setUp(self):
        self.customer = Customer()

    # def test_assert_raises_fullname_value_error(self):
    #    with self.assertRaises(ValueError):
    #        self.customer.fullname = None
    #        self.customer.fullname = ""
    #
    # def test_assert_raises_email_value_error(self):
    #    with self.assertRaises(ValueError):
    #        self.customer.email = None
    #        self.customer.email = ""
    #
    # def test_assert_raises_phone_value_error(self):
    #    with self.assertRaises(ValueError):
    #        self.customer.phone = None
    #        self.customer.phone = ""

    # def test_assert_true_valid_phone_number(self):
    #     self.customer.phone = Setting.SYNTHETIC_DATA_PHONE_NUMBER
    #     print(self.customer)
    #     self.assertTrue(self.customer.is_valid_phone(), msg="Testing if phone number is valid")
    #
    # def test_assert_false_valid_phone_number(self):
    #     self.customer.phone = Setting.NULL_VALUE
    #     print(self.customer)
    #     self.assertFalse(self.customer.is_valid_phone(), msg="Testing if phone number is not valid")

    def test_assert_true_valid_email_id(self):
        self.customer.email = Setting.SYNTHETIC_DATA_EMAIL
        # print(self.customer)
        self.assertTrue(self.customer.is_valid_email(), msg="Testing if E-mail ID is valid")

    def test_assert_false_valid_email_id(self):
        self.customer.email = Setting.NULL_VALUE
        # print(self.customer)
        self.assertFalse(self.customer.is_valid_email(), msg="Testing if E-mail ID is not valid")

if __name__ == '__main__':
    unittest.main()