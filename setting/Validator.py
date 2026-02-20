from datetime import datetime

import setting
from setting.Setting import Setting
import phonenumbers
import re

class Validator:

    @staticmethod
    def has_min_len(src_str, length):
        if src_str is not None:
            return len(str(src_str)) >= length
        else:
            return False

    @staticmethod
    def is_valid_date(src_str):
        try:
            datetime.strptime(src_str, Setting.DATE_FORMAT)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_valid_quantity(src_str):
        if isinstance(src_str, int):
            return True
        else:
            return False

    @staticmethod
    def is_valid_phone_number(src_str):
        try:
            parsed_number = phonenumbers.parse(src_str)
            is_valid = phonenumbers.is_valid_number(parsed_number)
            is_possible = phonenumbers.is_possible_number(parsed_number)

            if is_valid:
                print('net valid')
                return True
            elif is_possible:
                print('possible')
                return True
            else:
                print('not valid not even in 100 years')
                return False
        except phonenumbers.phonenumberutil.NumberParseException as e:
            print(f"Error parsing number: {e}")
            return False
    @staticmethod
    def is_valid_email(src_str):
        # print("^" * 10)
        # print(Setting.EMAIL_PATTERN)
        # print(src_str)
        # print("^" * 10)

        if re.fullmatch(Setting.EMAIL_PATTERN, src_str):
            return True
        else:
            return False