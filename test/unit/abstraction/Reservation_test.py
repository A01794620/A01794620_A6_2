"""
ReservationTest Unit Test
"""
import sys
import unittest
from pathlib import Path
from setting.Setting import Setting
from abstraction.Reservation import Reservation

_parent_dir = Path(__file__).parent.parent.parent.parent.resolve()
sys.path.insert(0, str(_parent_dir))


# pylint: disable=R0904
class ReservationTest(unittest.TestCase):
    """
    ReservationTest Unit Test
    """
    def setUp(self):
        self.reservation = Reservation()

    # ID
    def test_assert_raises_uuid_value_error(self):
        with self.assertRaises(ValueError):
            self.reservation.id = ""

    def test_assert_true_uuid_value(self):
        self.reservation.id = Setting.SYNTHETIC_DATA_UUID
        self.assertTrue(self.reservation.is_valid_id(),
                        msg="Testing if UUID is Valid")

    def test_assert_false_uuid_value(self):
        self.reservation.id = Setting.NULL_VALUE
        self.assertFalse(self.reservation.is_valid_id(),
                         msg="Testing if UUID is not Valid")

    # Hotel ID
    def test_assert_raises_hotel_id_value_error(self):
        with self.assertRaises(ValueError):
            self.reservation.hotel_id = None
            self.reservation.hotel_id = ""

    def test_assert_true_hotel_uuid_value(self):
        self.reservation.hotel_id = Setting.SYNTHETIC_DATA_UUID
        self.assertTrue(self.reservation.is_valid_hotel_id(),
                        msg="Testing if Hotel UUID is Valid")

    def test_assert_false_hotel_uuid_value(self):
        self.reservation.hotel_id = Setting.NULL_VALUE
        self.assertFalse(self.reservation.is_valid_hotel_id(),
                         msg="Testing if Hotel UUID is not Valid")

    # Room
    def test_assert_raises_room_value_error(self):
        with self.assertRaises(ValueError):
            self.reservation.room = None
            self.reservation.room = ""

    def test_assert_true_room_value(self):
        self.reservation.room = Setting.SYNTHETIC_DATA_ROOM_NUMBER
        self.assertTrue(self.reservation.is_valid_room(),
                        msg="Testing if Room number is Valid")

    def test_assert_false_room_value(self):
        self.reservation.room = Setting.NULL_VALUE
        self.assertFalse(self.reservation.is_valid_room(),
                         msg="Testing if Room number is not Valid")

    # Customer ID
    def test_assert_raises_customer_id_value_error(self):
        with self.assertRaises(ValueError):
            self.reservation.customer_id = None
            self.reservation.customer_id = ""

    def test_assert_true_customer_uuid_value(self):
        self.reservation.customer_id = Setting.SYNTHETIC_DATA_UUID
        self.assertTrue(self.reservation.is_valid_customer_id(),
                        msg="Testing if Customer UUID is Valid")

    def test_assert_false_customer_uuid_value(self):
        self.reservation.customer_id = Setting.NULL_VALUE
        self.assertFalse(self.reservation.is_valid_customer_id(),
                         msg="Testing if Customer UUID is not Valid")

    # Number of Adults in the Room
    def test_assert_true_adult_quantity(self):
        self.reservation.adults_number = Setting.SYNTHETIC_DATA_QUANTITY_NUMBER
        self.assertTrue(self.reservation.is_valid_adult_quantity(),
                        msg="Testing if number of adults in room is valid")

    def test_assert_false_adult_quantity(self):
        self.reservation.adult_quantity = Setting.NULL_NUMBER
        self.assertFalse(self.reservation.is_valid_adult_quantity(),
                         msg="Testing if number of adults "
                             "in room is not valid")

    def test_assert_raises_adults_number_value_error(self):
        with self.assertRaises(ValueError):
            self.reservation.adults_number = None
            self.reservation.adults_number = ""

    # Number of children in the Room
    def test_assert_true_children_quantity(self):
        self.reservation.children_number = (
            Setting.SYNTHETIC_DATA_QUANTITY_NUMBER)

        self.assertTrue(self.reservation.is_valid_children_quantity(),
                        msg="Testing if number of children in room is valid")

    def test_assert_false_children_quantity(self):
        self.reservation.children_number = Setting.NULL_NUMBER
        self.assertFalse(self.reservation.is_valid_children_quantity(),
                         msg="Testing if number of children in "
                             "room is not valid")

    def test_assert_raises_children_number_value_error(self):
        with self.assertRaises(ValueError):
            self.reservation.children_number = None
            self.reservation.children_number = ""

    # Reservation Date
    def test_assert_true_date(self):
        self.reservation.date = Setting.SYNTHETIC_DATA_DATE
        self.assertTrue(self.reservation.is_valid_date(),
                        msg="Testing if booking date is valid")

    def test_assert_false_date(self):
        self.reservation.date = Setting.NULL_VALUE
        self.assertFalse(self.reservation.is_valid_date(),
                         msg="Testing if booking date is not valid")

    def test_assert_raises_date_value_error(self):
        with self.assertRaises(ValueError):
            self.reservation.date = None
            self.reservation.date = ""


if __name__ == '__main__':
    unittest.main()
