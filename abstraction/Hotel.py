from setting.Setting import Setting
from setting.UuidHandler import UuidHandler

class Hotel:

    def __init__(self, name=None, address=None, email=None, phone=None):
        # self._id = str(uuid.uuid4())
        self._id = UuidHandler.get_next_id()
        self._name = Setting.NULL_VALUE if name is None else name
        self._address = Setting.NULL_VALUE if address is None else address
        self._email = Setting.NULL_VALUE if email is None else email
        self._phone = Setting.NULL_VALUE if phone is None else phone

    def __str__(self):
        head_line = Setting.HEAD_SYMBOL * Setting.COL_WIDTH

        return (head_line + '\n' +
                f"Hotel Details:\n" +
                head_line  + '\n' +
                f"ID      := {self.id}\n"
                f"Name    := {self.name}\n"
                f"Address := {self.address}\n"
                f"E-mail  := {self.email}\n"
                f"Phone   := {self.phone}\n" +
                head_line
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
    def name(self):
        return f"{self._name}"

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def address(self):
        return f"{self._address}"

    @address.setter
    def address(self, value):
        if not value:
            raise ValueError("Address cannot be empty")
        self._address = value

    @property
    def email(self):
        return f"{self._email}"

    @email.setter
    def email(self, value):
        if not value:
            raise ValueError("E-mail cannot be empty")
        self._email= value

    @property
    def phone(self):
        return f"{self._phone}"

    @phone.setter
    def phone(self, value):
        if not value:
            raise ValueError("Phone cannot be empty")
        self._phone = value