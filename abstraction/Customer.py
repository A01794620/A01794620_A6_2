from setting.Setting import Setting
from setting.UuidHandler import UuidHandler
from setting.Validator import Validator

class Customer:

    def __init__(self, fullname=None, email=None, phone=None):
        self._id = UuidHandler.get_next_id()
        self.fullname = Setting.NULL_VALUE if fullname is None else fullname
        self.email = Setting.NULL_VALUE if email is None else email
        self.phone = Setting.NULL_VALUE if phone is None else phone

    def __str__(self):
        head_line = Setting.HEAD_SYMBOL * Setting.COL_WIDTH
        return (head_line + '\n' +
                f"Customer Details:\n" +
                head_line + '\n' +
                f"ID      := {self._id}\n"
                f"Name    := {self._fullname}\n"
                f"E-mail  := {self._email}\n"
                f"Phone   := {self._phone}\n" +
                head_line
               )

    def is_valid_id(self):
        return UuidHandler.is_valid_id(self.id)

    def is_valid_phone(self):
        return Validator.is_valid_phone_number(self.phone)

    def is_valid_email(self):
        return Validator.is_valid_email(self.email)

    def is_valid_fullname(self):
        return Validator.is_valid_subject_name(self.fullname)

    @property
    def id(self):
        return f"{self._id}"

    @id.setter
    def id(self, value):
        if not value:
            raise ValueError("ID cannot be empty")
        self._id = value

    @property
    def fullname(self):
        return f"{self._fullname}"

    @fullname.setter
    def fullname(self, value):
        if not value:
            raise ValueError("Fullname cannot be empty")
        self._fullname = value

    @property
    def email(self):
        return f"{self._email}"

    @email.setter
    def email(self, value):
        if not value:
            raise ValueError("E-mail cannot be empty")
        self._email = value

    @property
    def phone(self):
        return f"{self._phone}"

    @phone.setter
    def phone(self, value):
        if not value:
            raise ValueError("Phone cannot be empty")
        self._phone = value