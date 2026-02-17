import uuid


class Customer:


    def __init__(self, name=""):
        self.name = name
        self._id = str(uuid.uuid4())

    def __str__(self):
        return (f"Customer Details:\n"
                f"Name := {self.name}\n"
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

    @property
    def name(self):
        return f"{self._name}"

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value