import re
import phonenumbers
from datetime import datetime
from setting.Setting import Setting

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
        #print("AA")
        if isinstance(src_str, int):
            #print("BB")
            return True
        else:
            #print("CC")
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
        if re.fullmatch(Setting.EMAIL_PATTERN, src_str):
            return True
        else:
            return False

    @staticmethod
    def is_valid_subject_name(src_str, might_have_space=True, is_address=False):
        if src_str is None:
            return False

        if len(src_str)<=0:
            return False

        if src_str.strip() == '':
            return False

        if might_have_space:
            if " " not in src_str.strip():
             return False

        if Validator.has_min_len(src_str.strip(), 3):

            if is_address:
                if re.match(Setting.ADDRESS_PATTERN,src_str.strip()):
                    return True
                else:
                    return False
            else:
                return src_str.replace(' ', '').isalpha()
        else:
            return False