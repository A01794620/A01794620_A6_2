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
import re
from datetime import datetime
import phonenumbers
from setting.Setting import Setting


class Validator:
    """
    Class as a manner of handy tool for
    rest of classes regarding syntactical
    validations
    """
    @staticmethod
    def has_min_len(src_str, length):
        """
        It checks if the provided strig has the
        minimum predefined length.
        Args:
            src_str (str): proposed string to be checked.
            length (int): length that the string must have.
          Returns:
              bool: Truth upon proper validation.
        """
        if src_str is not None:
            return len(str(src_str)) >= length

        return False

    @staticmethod
    def is_valid_date(src_str):
        """
        It checks if the provided strig has the
        date format.
        Args:
            src_str (str): proposed string to be checked.
          Returns:
              bool: Truth upon proper validation, if
                    the date format is available inside
                    the string.
        """
        try:
            datetime.strptime(src_str, Setting.DATE_FORMAT)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_valid_quantity(src_str):
        """
        It checks if the provided strig has a
        quantity format.
        Args:
            src_str (str): proposed string to be checked.
        Returns:
            bool: Truth upon proper validation, if
                  the quantity format is available
                  inside the provided string to check.
        """
        return isinstance(src_str, int)
        # if isinstance(src_str, int):
        #     return True
        # else:
        #     return False

    @staticmethod
    def is_valid_phone_number(src_str):
        """
         It checks if the provided strig has a
         phone format.
         Args:
             src_str (str): proposed string to be checked.
         Returns:
             bool: Truth upon proper validation, if
                   the telephone format is available
                   inside the provided string to check.
         """
        try:
            parsed_number = phonenumbers.parse(src_str)
            is_valid = phonenumbers.is_valid_number(parsed_number)
            is_possible = phonenumbers.is_possible_number(parsed_number)

            if is_valid or is_possible:
                return True

            return False

            # if is_valid:
            #     return True
            # elif is_possible:
            #     return True
            # else:
            #     return False
        except phonenumbers.phonenumberutil.NumberParseException as e:
            # print(f"Error parsing number: {e}")
            return False

    @staticmethod
    def is_valid_email(src_str):
        """
         It checks if the provided strig has an
         E-mail format.
         Args:
             src_str (str): proposed string to be checked.
         Returns:
             bool: Truth upon proper validation, if
                   the E-mail format is available
                   inside the provided string to check.
         """
        return re.fullmatch(Setting.EMAIL_PATTERN, src_str)

        # if re.fullmatch(Setting.EMAIL_PATTERN, src_str):
        #     return True
        # else:
        #     return False

    @staticmethod
    def is_valid_subject_name(src_str, might_have_space=True,
                              is_address=False):
        """
         It checks if the provided strig has a
         sort of basic format to be considered
         as subject.
         Args:
             src_str (str): proposed string to be checked.
             might_have_space (bool): might or might not
                                      have space.
             is_address (bool): if it is actually an address
                                to be checked or not.
         Returns:
             bool: Truth upon proper validation, if
                   the subject format is available
                   inside the provided string to check.
        """
        if (src_str is None) or (len(src_str) <= 0) or (src_str.strip() == ''):
            return False

        # if src_str is None:
        #     return False
        #
        # if len(src_str)<=0:
        #     return False
        #
        # if src_str.strip() == '':
        #     return False

        if might_have_space:
            if " " not in src_str.strip():
                return False

        if Validator.has_min_len(src_str.strip(), 3):

            if is_address:
                if re.match(Setting.ADDRESS_PATTERN, src_str.strip()):
                    return True

                return False

            return src_str.replace(' ', '').isalpha()

        return False
