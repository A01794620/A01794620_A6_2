import unittest
import sys
from pathlib import Path
_parent_dir = Path(__file__).parent.parent.parent.parent.resolve()
sys.path.insert(0, str(_parent_dir))
from data_handling.JsonManager import JsonManager
from abstraction.AbstractionType import AbstractionType
from setting.Setting import Setting
from abstraction.Customer import Customer
from abstraction.Hotel import Hotel
from abstraction.Reservation import Reservation

class JsonManagerTestCreate(unittest.TestCase):
    def setUp(self):

        self.customer = Customer(Setting.SYNTHETIC_DATA_FULLNAME,
                                 Setting.SYNTHETIC_DATA_EMAIL,
                                 Setting.SYNTHETIC_DATA_PHONE_NUMBER)

        self.hotel = Hotel(Setting.SYNTHETIC_DATA_HOTEL_NAME,
                           Setting.SYNTHETIC_DATA_ADDRESS,
                           Setting.SYNTHETIC_DATA_EMAIL,
                           Setting.SYNTHETIC_DATA_PHONE_NUMBER)

        self.reservation = Reservation(
            Setting.SYNTHETIC_DATA_UUID,
            Setting.SYNTHETIC_DATA_UUID,
            Setting.SYNTHETIC_DATA_ROOM_NUMBER,
            Setting.SYNTHETIC_DATA_QUANTITY_NUMBER,
            Setting.SYNTHETIC_DATA_QUANTITY_NUMBER,
            Setting.NULL_DATE_VALUE)

    # Create Data Unity Tests
    def test_assert_true_create_data(self):
        for abs_type in AbstractionType:
            msg_ = f"Testing if data can be created in {abs_type}"

            if abs_type is AbstractionType.CUSTOMER:
                self.customer.id = Setting.SYNTHETIC_DATA_UUID
                self.assertTrue(JsonManager.create_data(AbstractionType.CUSTOMER, self.customer), msg=msg_)
            elif abs_type is AbstractionType.HOTEL:
                self.hotel.id = Setting.SYNTHETIC_DATA_UUID
                self.assertTrue(JsonManager.create_data(AbstractionType.HOTEL, self.hotel), msg=msg_)
            elif abs_type is AbstractionType.RESERVATION:
                self.reservation.id = Setting.SYNTHETIC_DATA_UUID
                self.assertTrue(JsonManager.create_data(AbstractionType.RESERVATION, self.reservation), msg=msg_)
            else:
                pass

    def test_assert_false_create_data(self):
        self.assertFalse(JsonManager.create_data(Setting.SYNTHETIC_DATA_INVALID_TYPE, self.hotel),
                         msg="Testing if data can not be created")

if __name__ == '__main__':
    unittest.main()