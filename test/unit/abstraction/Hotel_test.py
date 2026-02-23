"""
HotelTest Unit Test
"""
import sys
import unittest
from pathlib import Path
from abstraction.Hotel import Hotel
from setting.Setting import Setting

_parent_dir = Path(__file__).parent.parent.parent.parent.resolve()
sys.path.insert(0, str(_parent_dir))


class HotelTest(unittest.TestCase):
    """
    HotelTest Unit Test
    """

    def setUp(self):
        self.hotel = Hotel()

    # ID
    def test_assert_raises_uuid_value_error(self):
        with self.assertRaises(ValueError):
            self.hotel.id = ""

    def test_assert_true_uuid_value(self):
        self.hotel.id = Setting.SYNTHETIC_DATA_UUID
        self.assertTrue(self.hotel.is_valid_id(),
                        msg="Testing if UUID is Valid")

    # Hotel Name
    def test_assert_raises_name_value_error(self):
        with self.assertRaises(ValueError):
            self.hotel.name = None
            self.hotel.name = ""

    def test_assert_true_name_value(self):
        self.hotel.name = Setting.SYNTHETIC_DATA_HOTEL_NAME
        self.assertTrue(self.hotel.is_valid_name(),
                        msg="Testing if Hotel Name is Valid")

    def test_assert_false_name_value(self):
        self.hotel.name = Setting.NULL_VALUE
        self.assertFalse(self.hotel.is_valid_name(),
                         msg="Testing if Hotel Name is not Valid")

    # Address
    def test_assert_raises_address_value_error(self):
        with self.assertRaises(ValueError):
            self.hotel.address = None
            self.hotel.address = ""

    def test_assert_true_address_value(self):
        self.hotel.address = Setting.SYNTHETIC_DATA_ADDRESS
        self.assertTrue(self.hotel.is_valid_address(),
                        msg="Testing if Hotel's Address is Valid")

    def test_assert_false_address_value(self):
        self.hotel.address = Setting.NULL_VALUE
        self.assertFalse(self.hotel.is_valid_address(),
                         msg="Testing if Hotel's Address is not Valid")

    # E-mail
    def test_assert_raises_email_value_error(self):
        with self.assertRaises(ValueError):
            self.hotel.email = None
            self.hotel.email = ""

    def test_assert_true_valid_email_id(self):
        self.hotel.email = Setting.SYNTHETIC_DATA_EMAIL
        self.assertTrue(self.hotel.is_valid_email(),
                        msg="Testing if E-mail ID is valid")

    def test_assert_false_valid_email_id(self):
        self.hotel.email = Setting.NULL_VALUE
        self.assertFalse(self.hotel.is_valid_email(),
                         msg="Testing if E-mail ID is not valid")

    # Phone
    def test_assert_raises_phone_value_error(self):
        with self.assertRaises(ValueError):
            self.hotel.phone = None
            self.hotel.phone = ""

    def test_assert_true_valid_phone_number(self):
        self.hotel.phone = Setting.SYNTHETIC_DATA_PHONE_NUMBER
        self.assertTrue(self.hotel.is_valid_phone(),
                        msg="Testing if phone number is valid")

    def test_assert_false_valid_phone_number(self):
        self.hotel.phone = Setting.NULL_VALUE
        self.assertFalse(self.hotel.is_valid_phone(),
                         msg="Testing if phone number is not valid")


if __name__ == '__main__':
    unittest.main()
