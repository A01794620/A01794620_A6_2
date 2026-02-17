class Reservation:


    def __init__(self, id=""):
        self.id = id

    def __str__(self):
        return (f"Reservation Details:\n"
                f"ID := {self.id}\n"
                )

    def create(self, is_screen_out=True):
        print("Reservation created!")
        print(self)

    def cancel(self, is_screen_out=True):
        print("Reservation deleted!")
        print(self)

    @property
    def id(self):
        return f"{self._id}"

    @id.setter
    def id(self, value):
        if not value:
            raise ValueError("ID cannot be empty")
        self._id = value