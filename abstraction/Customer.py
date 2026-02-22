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
from setting.Validator import Validator
from setting.UuidHandler import UuidHandler


class Customer:
    """
    Customer:
    One of the three pillars of the solution.
    It holds all the information about the customer who pursues
    reservations in hotels.
    It holds a unique ID, one full name, his/her e-mail address
    and the telephone.
    """

    def __init__(self, fullname=None, email=None, phone=None):
        self._id = UuidHandler.get_next_id()
        self.fullname = Setting.NULL_VALUE if fullname is None else fullname
        self.email = Setting.NULL_VALUE if email is None else email
        self.phone = Setting.NULL_VALUE if phone is None else phone

    def __str__(self):
        head_line = Setting.HEAD_SYMBOL * Setting.COL_WIDTH
        return (
                head_line + '\n' +
                "Customer Details:\n" +
                head_line + '\n' +
                f"ID      := {self._id}\n"
                f"Name    := {self._fullname}\n"
                f"E-mail  := {self._email}\n"
                f"Phone   := {self._phone}\n" +
                head_line)

    def is_valid_id(self):
        """
        It validates if the customer ID is a valid UUID 4 string.
        Args:
            (void): It checks in the same object.
            Returns:
                bool: evaluation if UUID is valid or not.
        """
        return UuidHandler.is_valid_id(self.id)

    def is_valid_phone(self):
        """
        It evaluates if the actual set phone is a valid string or not.
        Args:
            (void): It checks in the same object.
        Returns:
            bool: Use the evaluation class to discover whether the phone
                  is valid or not.
                  Uses Google's 'libphonenumber' library originally
                  written in Java Language.
        """
        return Validator.is_valid_phone_number(self.phone)

    def is_valid_email(self):
        """
        It evaluates if the E-mail id represents a valid formatted string.
        Args:
            (void): It checks in the same object.
        Returns:
            bool: Evaluation either the email is
                  well formatted or not.
        """
        return Validator.is_valid_email(self.email)

    def is_valid_fullname(self):
        """
        It evaluates if the Fullname has the minimum standard to be valid.
        Args:
            (void): It checks in the same object.
        Returns:
            bool: evaluation of the correctness of the fullname.
        """
        return Validator.is_valid_subject_name(self.fullname,
                                               might_have_space=True,
                                               is_address=False)

    @property
    def id(self):
        """
        Get or set customer ID, which must be a UUID 4 string.
        """
        return f"{self._id}"

    @id.setter
    def id(self, value):
        if not value:
            raise ValueError("ID cannot be empty")
        self._id = value

    @property
    def fullname(self):
        """
        Get or set customer Fullname.
        """
        return f"{self._fullname}"

    @fullname.setter
    def fullname(self, value):
        if not value:
            raise ValueError("Fullname cannot be empty")
        self._fullname = value

    @property
    def email(self):
        """
        Get or set email of the customer.
        """
        return f"{self._email}"

    @email.setter
    def email(self, value):
        if not value:
            raise ValueError("E-mail cannot be empty")
        self._email = value

    @property
    def phone(self):
        """
        Get or set phone of the customer.
        """
        return f"{self._phone}"

    @phone.setter
    def phone(self, value):
        if not value:
            raise ValueError("Phone cannot be empty")
        self._phone = value
