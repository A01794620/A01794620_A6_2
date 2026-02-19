import datetime
import uuid

class Reservation:

    def __init__(self, hotel_id="", customer_id="", room="", adults_number=0, children_number=0,  date=""):
        self._id = str(uuid.uuid4())
        self.hotel_id = hotel_id
        self.customer_id = customer_id
        self.room = room
        self.adults_number = adults_number
        self.children_number = children_number
        self.date = date
        self._registration_date = datetime.datetime.now()

    def __str__(self):
        return (f"Reservation Details:\n"
                f"Id          := {self._id}\n"
                f"Hotel-Id    := {self._hotel_id}\n"
                f"Room        := {self._room}\n"
                f"Customer-Id := {self._customer_id}\n"
                f"Adults #    := {self._adults_number}\n"
                f"Children #  := {self._children_number}\n"
                f"Date        := {self._date}\n"
                f"Reg-Date    := {self._registration_date}\n"
                )

    @property
    def id(self):
        return f"{self._id}"

    @id.setter
    def id(self, value):
        if not value:
            raise ValueError("Id cannot be empty")
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
        return f"{self._adults_number}"

    @adults_number.setter
    def adults_number(self, value):
        if not value:
            raise ValueError("Adults Number cannot be empty")
        self._adults_number= value

    @property
    def children_number(self):
        return f"{self._children_number}"

    @children_number.setter
    def children_number(self, value):
        if not value:
            raise ValueError("Adults Number cannot be empty")
        self._children_number = value
