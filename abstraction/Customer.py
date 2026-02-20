import uuid
from abstraction.Setting import Setting

class Customer:

    def __init__(self, fullname="", email="", phone=""):
        self._id = str(uuid.uuid4())
        self.fullname = fullname
        self.email = email
        self.phone = phone

    def __str__(self):
        head_line = Setting.HEAD_SYMBOL * Setting.COL_WIDTH
        return (head_line +
                f"Customer Details:\n" +
                head_line +
                f"ID := {self._id}\n"
                f"Name := {self._fullname}\n"
                f"E-mail := {self._email}\n"
                f"Phone := {self._phone}\n" +
                head_line
               )

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