import unittest
import sys
from pathlib import Path

_parent_dir = Path(__file__).parent.parent.parent.parent.resolve()
sys.path.insert(0, str(_parent_dir))
from abstraction.Reservation import Reservation
from setting.UuidHandler import UuidHandler
from setting.Setting import Setting

class CustomerTest(unittest.TestCase):
    def setUp(self):
        self.reservation = Reservation()

    def test_assert_raises_uuid_value_error(self):
        with self.assertRaises(ValueError):
             self.reservation.id = ""

    def test_assert_true_uuid_value(self):
        self.id = Setting.SYNTHETIC_DATA_UUID
        self.assertTrue(UuidHandler.is_valid_id(self.id), msg="Testing if UUID is Valid")

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