import unittest
import sys
from pathlib import Path

_parent_dir = Path(__file__).parent.parent.parent.parent.resolve()
sys.path.insert(0, str(_parent_dir))
from abstraction.Hotel import Hotel

class HotelTest(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel()

    def test_assert_raises_name_value_error(self):
       with self.assertRaises(ValueError):
           self.hotel.name = None
           self.hotel.name = ""

    def test_assert_raises_address_value_error(self):
       with self.assertRaises(ValueError):
           self.hotel.address = None
           self.hotel.address= ""

    def test_assert_raises_email_value_error(self):
       with self.assertRaises(ValueError):
           self.hotel.email = None
           self.hotel.email = ""

    def test_assert_raises_phone_value_error(self):
       with self.assertRaises(ValueError):
           self.hotel.phone = None
           self.hotel.phone = ""

if __name__ == '__main__':
    unittest.main()