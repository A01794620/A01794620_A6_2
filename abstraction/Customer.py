import uuid

class Customer:

    def __init__(self, name="", email="", phone=""):
        self._id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return (f"Customer Details:\n"
                f"Id := {self._id}\n"
                f"Name := {self.name}\n"
                f"E-mail := {self._email}\n"
                f"Phone := {self._phone}"
               )

    def create(self, is_screen_out=True):
        print("Customer created!")
        print(self)

    def delete(self, is_screen_out=True):
        print("Customer deleted!")
        print(self)

    def display(self, is_screen_out=True):
        print("Customer displayed!")
        print(self)

    def modify(self, is_screen_out=True):
            print("Customer modified!")
            print(self)

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
    def email(self):
        return f"{self._email}"

    @email.setter
    def email(self, value):
        if not value:
            raise ValueError("Email cannot be empty")
        self._email = value

    @property
    def phone(self):
        return f"{self._phone}"

    @phone.setter
    def phone(self, value):
        if not value:
            raise ValueError("Phone cannot be empty")
        self._phone = value