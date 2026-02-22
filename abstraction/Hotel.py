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
from setting.Setting import Setting
from setting.UuidHandler import UuidHandler
from setting.Validator import Validator

class Hotel:
    """
    Hotel:
    This class holds the Hotel entity structure linked to
    the physical places to be booked.
    This entity is the gold of the Customers, who are
    looking towards find a room in a hotel as a reservation.
    """
    def __init__(self, name=None, address=None, email=None, phone=None):
        self._id = UuidHandler.get_next_id()
        self._name = Setting.NULL_VALUE if name is None else name
        self._address = Setting.NULL_VALUE if address is None else address
        self._email = Setting.NULL_VALUE if email is None else email
        self._phone = Setting.NULL_VALUE if phone is None else phone

    def __str__(self):
        head_line = Setting.HEAD_SYMBOL * Setting.COL_WIDTH

        return (head_line + '\n' +
                "Hotel Details:\n" +
                head_line  + '\n' +
                f"ID      := {self.id}\n"
                f"Name    := {self.name}\n"
                f"Address := {self.address}\n"
                f"E-mail  := {self.email}\n"
                f"Phone   := {self.phone}\n" +
                head_line
               )

    def is_valid_id(self):
        """
        It validates if the Hotel ID is a valid UUID 4 string.
        Args:
            (void): It checks in the same object.
            Returns:
                bool: evaluation if UUID is valid or not.
        """
        return UuidHandler.is_valid_id(self.id)

    def is_valid_name(self):
        """
        Checks if the hotel’s name holds the minimum length and spaces requirements.
        Args:
            (void): It checks in the same object.
        Returns:
            bool: evaluation of the correctness of the Hotel's name.
        """
        return Validator.is_valid_subject_name(self.name, False, False)

    def is_valid_address(self):
        """
        Evaluates the physical address of the Hotel using a Regular expression.
        Args:
            (void): it checks in the same object.
        Returns:
            bool: check about the right format of the physical address.
            It does not do a formal verification against any
            Address verification system (AVS).
        """
        return Validator.is_valid_subject_name(self.address, False, is_address=True)

    def is_valid_phone(self):
        """
        It evaluates if the actual set phone is a valid string or not as per its structure.
        Args:
            (void): It checks in the same object.
        Returns:
            bool: Use the evaluation class to discover whether the phone is valid or not.
                  Uses Google's Phone Number library, originally written in Java Language.
                  It does not do any PBX (Private Branch Exchange) check again a real phone call.
        """
        return Validator.is_valid_phone_number(self.phone)

    def is_valid_email(self):
        """
        Evaluates e-mail format validity.
        Args:
            (void): It checks in the same object.
        Returns:
            bool: Evaluation either the email is well formatted or not.
                  It checks using a Regular Expression, about the right
                  format of the e-mail.
                  It does not do a real online send/received message
                  verification since this is out of the boundaries of
                  this system version (1.0.0).
        """
        return Validator.is_valid_email(self.email)

    @property
    def id(self):
        """
        Get or set Hotel ID, which must be a UUID 4 string.
        """
        return f"{self._id}"

    @id.setter
    def id(self, value):
        if not value:
            raise ValueError("Id cannot be empty")
        self._id = value

    @property
    def name(self):
        """
        Get or set name of the Hotel.
        """
        return f"{self._name}"

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def address(self):
        """
        Get or set customer Physical Hotel Address.
        """
        return f"{self._address}"

    @address.setter
    def address(self, value):
        if not value:
            raise ValueError("Address cannot be empty")
        self._address = value

    @property
    def email(self):
        """
        Get or set primary email of the Hotel.
        """
        return f"{self._email}"

    @email.setter
    def email(self, value):
        if not value:
            raise ValueError("E-mail cannot be empty")
        self._email= value

    @property
    def phone(self):
        """
         Get or set contact phone of the Hotel.
         """
        return f"{self._phone}"

    @phone.setter
    def phone(self, value):
        if not value:
            raise ValueError("Phone cannot be empty")
        self._phone = value
