import datetime
import uuid

class Reservation:

    def __init__(self, hotel_id="", customer_id="", room="", date=""):
        self._id = str(uuid.uuid4())
        self._hotel_id = hotel_id
        self._customer_id = customer_id
        self._room = room
        self._date = date
        self._registration_date = datetime.datetime.now()

    def __str__(self):
        return (f"Reservation Details:\n"
                f"Id          := {self._id}\n"
                f"Hotel-Id    := {self._hotel_id}\n"
                f"Room        := {self._room}\n"
                f"Customer-Id := {self._customer_id}\n"
                f"Date        := {self._date}\n"
                f"Reg-Date    := {self._registration_date}\n"
                )

    # def create(self, is_screen_out=True):
    #     print("Reservation created!")
    #     print(self)
    #
    # def cancel(self, is_screen_out=True):
    #     print("Reservation deleted!")
    #     print(self)

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
        return f"{self.hotel_id}"

    @hotel_id.setter
    def hotel_id(self, value):
        if not value:
            raise ValueError("Hotel ID cannot be empty")
        self._hotel_id = value

    @property
    def customer_id(self):
        return f"{self.customer_id}"

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
            raise ValueError("Room cannot be empty")
        self._room = value

    @property
    def date(self):
        return f"{self._date}"

    @date.setter
    def date(self, value):
        if not value:
            raise ValueError("Date cannot be empty")
        self._date = value

    @property
    def registration_date(self):
        return f"{self._registration_date}"
