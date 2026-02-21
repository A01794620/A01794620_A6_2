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
import json

class JsonManagerTest(unittest.TestCase):
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
            Setting.SYNTHETIC_DATA_QUANTITY_NUMBER)



    # def test_assert_true_valid_path(self):
    #     for abs_type in AbstractionType:
    #         self.assertTrue(JsonManager.is_valid_path(JsonManager.get_path(abs_type)),
    #                         msg="Testing if Path for customer is Valid")
    #
    # def test_assert_false_valid_path(self):
    #     self.assertFalse(JsonManager.is_valid_path(JsonManager.get_path(Setting.SYNTHETIC_DATA_INVALID_TYPE)),
    #                       msg="Testing if Path for customer is not Valid")
    #

    # def test_assert_true_valid_json(self):
    #     for abs_type in AbstractionType:
    #         json_to_try = ""
    #
    #         if abs_type is AbstractionType.CUSTOMER:
    #             json_to_try = JsonManager.yield_json(AbstractionType.CUSTOMER, self.customer)
    #         elif abs_type is AbstractionType.HOTEL:
    #             json_to_try = JsonManager.yield_json(AbstractionType.HOTEL, self.hotel)
    #         elif abs_type is AbstractionType.RESERVATION:
    #             json_to_try = JsonManager.yield_json(AbstractionType.RESERVATION, self.reservation)
    #
    #         self.assertTrue(JsonManager.is_valid_json(json_to_try), msg=f"Testing if JSON for {abs_type} is Valid")

    # def test_assert_false_valid_json(self):
    #     json_to_try = JsonManager.yield_json(Setting.SYNTHETIC_DATA_INVALID_TYPE, self.customer)
    #     self.assertFalse(JsonManager.is_valid_json(json_to_try), msg=f"Testing if JSON for {Setting.SYNTHETIC_DATA_INVALID_TYPE} is not Valid")


    #def test_assert_false_valid_json(self):
    #    json_to_try = JsonManager.yield_json(Setting.SYNTHETIC_DATA_INVALID_TYPE, self.customer)
    #    self.assertFalse(JsonManager.is_valid_json(json_to_try), msg=f"Testing if JSON for {Setting.SYNTHETIC_DATA_INVALID_TYPE} is not Valid")

    # def test_assert_true_has_data_path(self):
    #     self.assertTrue(JsonManager.has_data(AbstractionType.CUSTOMER, Setting.SYNTHETIC_FILE_ID),
    #                         msg="Testing if the Path has Valid data")
    #
    # def test_assert_false_has_data_path(self):
    #     self.assertFalse(JsonManager.has_data(AbstractionType.HOTEL, Setting.SYNTHETIC_FILE_ID),
    #                         msg="Testing if the Path has not Valid data")

    # def test_assert_true_create_data(self):
    #     self.assertTrue(JsonManager.create_data(AbstractionType.HOTEL, self.hotel),
    #                         msg="Testing if data can be created")
    #
    # def test_assert_false_create_data(self):
    #     self.assertFalse(JsonManager.create_data(Setting.SYNTHETIC_DATA_INVALID_TYPE, self.hotel),
    #                     msg="Testing if data can not be created")

    # def test_assert_is_instance_load_data(self):
    #     full_path = JsonManager.get_path(AbstractionType.CUSTOMER) + Setting.SYNTHETIC_FILE_ID + Setting.FILE_EXTENSION
    #     self.assertIsInstance(JsonManager.load_from_file(full_path), dict)
    #
    # def test_assert_is_not_instance_load_data(self):
    #     full_path = JsonManager.get_path(AbstractionType.CUSTOMER) + Setting.SYNTHETIC_FILE_ID_WRONG + Setting.FILE_EXTENSION
    #     self.assertNotIsInstance(JsonManager.load_from_file(full_path), dict)

    # def test_assert_is_instance_retrieve_data(self):
    #     self.assertIsInstance(JsonManager.retrieve_data(AbstractionType.CUSTOMER, Setting.SYNTHETIC_FILE_ID), Customer)
    #
    # def test_assert_is_not_instance_retrieve_data(self):
    #     self.assertNotIsInstance(JsonManager.retrieve_data(AbstractionType.CUSTOMER, Setting.SYNTHETIC_FILE_ID), Hotel)

    # def test_assert_is_instance_display_data(self):
    #     customers = JsonManager.display_data(AbstractionType.CUSTOMER)
    #     self.assertIsInstance(customers, list)
    #     self.assertIsInstance(customers[0], Customer)

    # def test_assert_items_equal_display_data_empty(self):
    #     customers = JsonManager.display_data(Setting.SYNTHETIC_DATA_INVALID_TYPE)
    #     self.assertListEqual(customers, [])


    # def test_assert_true_delete_data(self):
    #     self.assertTrue(JsonManager.delete_data(AbstractionType.CUSTOMER, Setting.SYNTHETIC_FILE_ID),
    #                         msg="Testing if data can be removed")

    def test_assert_false_delete_data(self):
        self.assertFalse(JsonManager.delete_data(AbstractionType.HOTEL, Setting.SYNTHETIC_FILE_ID_WRONG),
                            msg="Testing if data can be removed")


if __name__ == '__main__':
    unittest.main()