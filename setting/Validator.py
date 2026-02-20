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
        if isinstance(src_str, int):
            return True
        else:
            return False