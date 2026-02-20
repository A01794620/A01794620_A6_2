import unittest
import sys
from pathlib import Path

_parent_dir = Path(__file__).parent.parent.parent.parent.resolve()
sys.path.insert(0, str(_parent_dir))
from abstraction.Reservation import Reservation
from setting.UuidHandler import UuidHandler
from setting.Setting import Setting

class ReservationTest(unittest.TestCase):
    def setUp(self):
         self.reservation = Reservation()

    # def test_assert_raises_uuid_value_error(self):
    #     with self.assertRaises(ValueError):
    #          self.reservation.id = ""
    #
    # def test_assert_true_uuid_value(self):
    #     self.reservation.id = Setting.SYNTHETIC_DATA_UUID
    #     self.assertTrue(UuidHandler.is_valid_id(self.reservation.id), msg="Testing if UUID is Valid")
    #
    # def test_assert_true_room_value(self):
    #     self.reservation.room = Setting.SYNTHETIC_DATA_ROOM_NUMBER
    #     self.assertTrue(self.reservation.is_valid_room(), msg="Testing if Room number is Valid")
    #
    # def test_assert_false_room_value(self):
    #     self.assertFalse(self.reservation.is_valid_room(), msg="Testing if Room number is not Valid")
    #

    # def test_assert_true_date(self):
    #     # print("TestOnTrue")
    #     self.reservation.date = Setting.SYNTHETIC_DATA_DATE
    #     # print(self.reservation)
    #     self.assertTrue(self.reservation.is_valid_date(), msg="Testing if booking date is valid")
    #
    # def test_assert_false_date(self):
    #     # print("TestOnFalse")
    #     # print(self.reservation)
    #     self.assertFalse(self.reservation.is_valid_date(), msg="Testing if booking date is not valid")

    def test_assert_true_adult_quantity(self):
        self.reservation.adults_number = Setting.SYNTHETIC_DATA_QUANTITY_NUMBER
        # print(self.reservation)
        self.assertTrue(self.reservation.is_valid_adult_quantity(), msg="Testing if number of adults in room is valid")

    def test_assert_false_adult_quantity(self):
        self.reservation.adult_quantity = Setting.NULL_NUMBER
        self.assertFalse(self.reservation.is_valid_adult_quantity(), msg="Testing if number of adults in room is not valid")

    def test_assert_true_children_quantity(self):
        self.reservation.children_number = Setting.SYNTHETIC_DATA_QUANTITY_NUMBER
        self.assertTrue(self.reservation.is_valid_children_quantity(), msg="Testing if number of children in room is valid")

    def test_assert_false_children_quantity(self):
        self.reservation.children_number = Setting.NULL_NUMBER
        self.assertFalse(self.reservation.is_valid_children_quantity(), msg="Testing if number of children in room is not valid")


    # def test_assert_raises_hotel_id_value_error(self):
    #     with self.assertRaises(ValueError):
    #         self.reservation.hotel_id = None
    #         self.reservation.hotel_id = ""
    #
    # def test_assert_raises_customer_id_value_error(self):
    #     with self.assertRaises(ValueError):
    #         self.reservation.customer_id = None
    #         self.reservation.customer_id = ""
    #
    # def test_assert_raises_room_value_error(self):
    #     with self.assertRaises(ValueError):
    #         self.reservation.room = None
    #         self.reservation.room = ""
    #
    # def test_assert_raises_date_value_error(self):
    #     with self.assertRaises(ValueError):
    #         self.reservation.date = None
    #         self.reservation.date = ""
    #
    # def test_assert_raises_adults_number_value_error(self):
    #     with self.assertRaises(ValueError):
    #         self.reservation.adults_number = None
    #         self.reservation.adults_number = ""
    #
    # def test_assert_raises_children_number_value_error(self):
    #     with self.assertRaises(ValueError):
    #         self.reservation.children_number = None
    #         self.reservation.children_number = ""

if __name__ == '__main__':
    unittest.main()