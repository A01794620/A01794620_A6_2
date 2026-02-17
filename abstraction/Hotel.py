class Hotel:


    def __init__(self, name=""):
        self.name = name

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
    def name(self):
        return f"{self._name}"

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value