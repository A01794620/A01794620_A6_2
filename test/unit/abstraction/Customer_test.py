"""
CustomerTest Unit Test
"""
import sys
import unittest
from pathlib import Path
from abstraction.Customer import Customer
from setting.Setting import Setting

_parent_dir = Path(__file__).parent.parent.parent.parent.resolve()
sys.path.insert(0, str(_parent_dir))


class CustomerTest(unittest.TestCase):
    """
    CustomerTest Unit Test
    """
    def setUp(self):
        self.customer = Customer()

    # ID
    def test_assert_raises_uuid_value_error(self):
        with self.assertRaises(ValueError):
            self.customer.id = ""

    def test_assert_true_uuid_value(self):
        self.customer.id = Setting.SYNTHETIC_DATA_UUID
        self.assertTrue(self.customer.is_valid_id(),
                        msg="Testing if UUID is Valid")

    # Fullname
    def test_assert_raises_fullname_value_error(self):
        with self.assertRaises(ValueError):
            self.customer.fullname = None
            self.customer.fullname = ""

    def test_assert_true_fullname_value(self):
        self.customer.fullname = Setting.SYNTHETIC_DATA_FULLNAME
        self.assertTrue(self.customer.is_valid_fullname(),
                        msg="Testing if Fullname is Valid")

    def test_assert_false_fullname_value(self):
        self.customer.fullname = Setting.NULL_VALUE
        self.assertFalse(self.customer.is_valid_fullname(),
                         msg="Testing if Fullname is not Valid")

    # E-mail
    def test_assert_raises_email_value_error(self):
        with self.assertRaises(ValueError):
            self.customer.email = None
            self.customer.email = ""

    def test_assert_true_valid_email_id(self):
        self.customer.email = Setting.SYNTHETIC_DATA_EMAIL
        self.assertTrue(self.customer.is_valid_email(),
                        msg="Testing if E-mail ID is valid")

    def test_assert_false_valid_email_id(self):
        self.customer.email = Setting.NULL_VALUE
        self.assertFalse(self.customer.is_valid_email(),
                         msg="Testing if E-mail ID is not valid")

    # Phone
    def test_assert_raises_phone_value_error(self):
        with self.assertRaises(ValueError):
            self.customer.phone = None
            self.customer.phone = ""

    def test_assert_true_valid_phone_number(self):
        self.customer.phone = Setting.SYNTHETIC_DATA_PHONE_NUMBER
        # print(self.customer)
        self.assertTrue(self.customer.is_valid_phone(),
                        msg="Testing if phone number is valid")

    def test_assert_false_valid_phone_number(self):
        self.customer.phone = Setting.NULL_VALUE
        # print(self.customer)
        self.assertFalse(self.customer.is_valid_phone(),
                         msg="Testing if phone number is not valid")


if __name__ == '__main__':
    unittest.main()
