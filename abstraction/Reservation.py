"""
 Module. AbstractionType. Exercise of Programming 3 and Unity Testing 6.2
 @Motive . Unity Testing
           Code Coverage Evaluation
           PEP8 check with Pylint and Flake8
 @author . Ronald Sandí Quesada
 @Student-ID . A01794620
 @email . A01794620@tec.mx
 @MNA Class . Pruebas de Software y Aseguramiento de la Calidad (TC4017)
 @Professor . PhD Gerardo Padilla Zárate
 @Professor Evaluator and Tutor . PhD Daniel Flores Araiza
 @Period . I Trimester 2026
 @Date: 22 February 2026
"""
import datetime
from setting.Setting import Setting
from setting.Validator import Validator
from setting.UuidHandler import UuidHandler


# pylint: disable=too-many-instance-attributes
# Disabled R0902: Too many instance attributes
class Reservation:
    """
    Reservation.
    This entity represents the action executed by a Customer
    into a Hotel. A reservation warrantee that one customer
    can stay in a room in a specific hotel.
    Due to the time constraint, this system on it version
    (1.0.0) only supports reservation registration and cancel
    registrations.
    Nevertheless, in a full-fledged complaint system the
    availability of a room in time and number of occupants
    might be checked before warranty reservation.
    Also, reservation in a full system might include
    price, and application of vanity points, bonus, payment
    media and specific amenities accommodations to warrantee
    customers satisfaction.
    All those important points are voided for time restrictions
    on this deliverable.
    """

    # pylint: disable=R0913, R0917
    def __init__(self, hotel_id=None, customer_id=None,
                 room=None, adults_number=None,
                 children_number=None,  date=None):
        self._id = UuidHandler.get_next_id()
        self._registration_date = datetime.datetime.now()

        self.hotel_id = Setting.NULL_VALUE if hotel_id is None else hotel_id
        self.customer_id = Setting.NULL_VALUE \
            if customer_id is None else customer_id
        self.room = Setting.NULL_VALUE if room is None else room
        self.adults_number = Setting.NULL_NUMBER \
            if adults_number is None else adults_number
        self.children_number = Setting.NULL_NUMBER \
            if children_number is None else children_number
        self.date = Setting.NULL_VALUE if date is None else date

    def __str__(self):
        head_line = Setting.HEAD_SYMBOL * Setting.COL_WIDTH

        return (head_line + '\n' +
                "Reservation Details:\n" +
                head_line + '\n' +
                f"ID          := {self._id}\n"
                f"Hotel-ID    := {self._hotel_id}\n"
                f"Room        := {self._room}\n"
                f"Customer-ID := {self._customer_id}\n"
                f"Adults   #  := {self._adults_number}\n"
                f"Children #  := {self._children_number}\n"
                f"Date        := {self._date}\n"
                f"Reg-Date    := {self._registration_date}\n" +
                head_line
                )

    def is_valid_id(self):
        """
        It validates if the Reservation ID is a valid UUID 4 string.
        Args:
            (void): It checks in the same object.
            Returns:
                bool: evaluation if UUID is valid or not.
        """
        return UuidHandler.is_valid_id(self.id)

    def is_valid_hotel_id(self):
        """
        It validates if the Hotel ID is a valid UUID 4 string.
        Args:
            (void): It checks in the same object.
            Returns:
                bool: evaluation if UUID is valid or not.
        """
        return UuidHandler.is_valid_id(self.hotel_id)

    def is_valid_customer_id(self):
        """
        It validates if the customer ID is a valid UUID 4 string.
        Args:
            (void): It checks in the same object.
        Returns:
                bool: evaluation if UUID is valid or not.
        """
        return UuidHandler.is_valid_id(self.customer_id)

    def is_valid_room(self):
        """
        Checks if the number has or not the valid format.
        Even when it indicates a number, on practice can contain
        letters as well (room A1 o F11-2).
        Args:
            (void): Validation of room syntax.
        Returns:
            bool: right evaluation of room syntax.
        """
        if self.room == Setting.NULL_VALUE:
            return False

        return Validator.has_min_len(self.room, 1)

    def is_valid_date(self):
        """
        Validation of the booking Date.
        It uses a conventional Datetime python library to checks weather
        the string is a valid date or not.
        Args:
            (void): It checks in the same object.
        Returns:
            bool: date validation.
        """
        if self.date == Setting.NULL_VALUE:
            return False

        return Validator.is_valid_date(self.date)

    def is_valid_adult_quantity(self):
        """
        Validates that the number of adults in a room in specific booking
        is right.
        Args:
            (void): It checks in the same object.
        Returns:
            bool: adult quantity validation.
        """
        return Reservation.is_valid_quantity(self.adults_number, 1)

    def is_valid_children_quantity(self):
        """
        Validates that the number of children in a room in specific booking
        is right.
        Args:
            (void): It checks in the same object.
        Returns:
            bool: children quantity validation.
        """
        return Reservation.is_valid_quantity(self.children_number,
                                             0)

    @staticmethod
    def is_valid_quantity(quantity, min_quantity):
        """
        It is a generic process of a quantity check to use it as placeholder
        for other quantities checks.
        Args:
            quantity (int): quantity to be checked.
            min_quantity (int): minimum quantity value accepted on
                                the validation case.
        Returns:
            bool: Truth if the evaluation is right; a neutral or
            positive quantity depending on the parameters.
        """
        if Validator.is_valid_quantity(quantity):
            return quantity >= min_quantity
        return False

    @property
    def id(self):
        """
        Get or set Reservation ID, which must be a UUID 4 string.
        """
        return f"{self._id}"

    @id.setter
    def id(self, value):
        if not value:
            raise ValueError("ID cannot be empty")
        self._id = value

    @property
    def hotel_id(self):
        """
        Get or set hotel ID, which must be a UUID 4 string.
        """
        return f"{self._hotel_id}"

    @hotel_id.setter
    def hotel_id(self, value):
        if not value:
            raise ValueError("Hotel ID cannot be empty")
        self._hotel_id = value

    @property
    def customer_id(self):
        """
        Get or set customer ID, which must be a UUID 4 string.
        """
        return f"{self._customer_id}"

    @customer_id.setter
    def customer_id(self, value):
        if not value:
            raise ValueError("Customer ID cannot be empty")
        self._customer_id = value

    @property
    def room(self):
        """
        Get or set Room ID.
        """
        return f"{self._room}"

    @room.setter
    def room(self, value):
        if not value:
            raise ValueError("Room Number cannot be empty")
        self._room = value

    @property
    def date(self):
        """
        Get or set date of the booking to be used.
        """
        return f"{self._date}"

    @date.setter
    def date(self, value):
        if not value:
            raise ValueError("Date cannot be empty")
        self._date = value

    @property
    def registration_date(self):
        """
        Get or set transaction Date.
        """
        return f"{self._registration_date}"

    @property
    def adults_number(self):
        """
        Get or set number of adults in a room in specific booking.
        """
        return self._adults_number

    @adults_number.setter
    def adults_number(self, value):
        if not Validator.is_valid_quantity(value):
            raise ValueError("Adults Number must be a digit")

        self._adults_number = value

    @property
    def children_number(self):
        """
        Get or set number of children in a room in specific booking.
        """
        return self._children_number

    @children_number.setter
    def children_number(self, value):
        if not Validator.is_valid_quantity(value):
            raise ValueError("Children Number must be a digit")
        self._children_number = value
