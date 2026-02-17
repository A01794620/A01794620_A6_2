import uuid

class Hotel:


    def __init__(self, name=""):
        self.name = name
        self._id = str(uuid.uuid4())

    def __str__(self):
        return (f"Hotel Details:\n"
                f"Name := {self.name}\n"
                )

    def create(self):
        print("Hotel created!")
        print(self)

    def delete(self):
        print("Hotel deleted!")
        print(self)

    def display(self):
        print("Hotel displayed!")
        print(self)

    def modify(self):
            print("Hotel modified!")
            print(self)

    def reserver_room(self):
        print("Room Reserved!")
        print(self)

    def cancel_reservation(self):
            print("Reservation Cancelled!")
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