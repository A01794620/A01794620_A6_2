import datetime
from setting.Setting import Setting
from setting.UuidHandler import UuidHandler
from setting.Validator import Validator

class Reservation:

    def __init__(self, hotel_id=None, customer_id=None, room=None, adults_number=None, children_number=None,  date=None):
        self._id = UuidHandler.get_next_id()
        self._registration_date = datetime.datetime.now()

        self.hotel_id = Setting.NULL_VALUE if hotel_id is None else hotel_id
        self.customer_id = Setting.NULL_VALUE if customer_id is None else customer_id
        self.room = Setting.NULL_VALUE if room is None else room
        self.adults_number = Setting.NULL_NUMBER if adults_number is None else adults_number
        self.children_number = Setting.NULL_NUMBER if children_number is None else children_number
        self.date = Setting.NULL_VALUE if date is None else date

    def __str__(self):
        head_line = Setting.HEAD_SYMBOL * Setting.COL_WIDTH

        return (head_line + '\n' +
                f"Reservation Details:\n" +
                head_line + '\n' +
                f"ID          := {self._id}\n"
                f"Hotel-ID    := {self._hotel_id}\n"
                f"Room        := {self._room}\n"
                f"Customer-ID := {self._customer_id}\n"
                f"Adults   #  := {self._adults_number}\n"
                f"Children #  := {self._children_number}\n"
                f"Date        := {self._date}\n"
                f"Reg-Date    := {self._registration_date}\n" +
                head_line
                )

    def is_valid_room(self):
        if self.room == Setting.NULL_VALUE:
            return False
        else:
            return Validator.has_min_len(self.room, 1)

    def is_valid_date(self):
        if self.date == Setting.NULL_VALUE:
            return False
        else:
            return Validator.is_valid_date(self.date)

    def is_valid_adult_quantity(self):
        return Reservation.is_valid_quantity(self.adults_number,1)

    def is_valid_children_quantity(self):
        return Reservation.is_valid_quantity(self.children_number,0)

    @staticmethod
    def is_valid_quantity(quantity, min_quantity):

        if Validator.is_valid_quantity(quantity):
            if quantity >= min_quantity:
                return True
            else:
                return False
        else:
            return False

    @property
    def id(self):
        return f"{self._id}"

    @id.setter
    def id(self, value):
        if not value:
            raise ValueError("ID cannot be empty")
        self._id = value


    @property
    def hotel_id(self):
        return f"{self._hotel_id}"

    @hotel_id.setter
    def hotel_id(self, value):
        if not value:
            raise ValueError("Hotel ID cannot be empty")
        self._hotel_id = value

    @property
    def customer_id(self):
        return f"{self._customer_id}"

    @customer_id.setter
    def customer_id(self, value):
        if not value:
            raise ValueError("Customer ID cannot be empty")
        self._customer_id = value

    @property
    def room(self):
        return f"{self._room}"

    @room.setter
    def room(self, value):
        if not value:
            raise ValueError("Room Number cannot be empty")
        self._room = value

    @property
    def date(self):
        return f"{self._date}"

    @date.setter
    def date(self, value):
        if not value:
            raise ValueError("Date cannot be empty")
        self._date= value

    @property
    def registration_date(self):
        return f"{self._registration_date}"

    @property
    def adults_number(self):
        return self._adults_number

    @adults_number.setter
    def adults_number(self, value):
        if not value:
            raise ValueError("Adults Number cannot be empty")
        self._adults_number= value

    @property
    def children_number(self):
        return self._children_number

    @children_number.setter
    def children_number(self, value):
        if not value:
            raise ValueError("Children Number cannot be empty")
        self._children_number = value