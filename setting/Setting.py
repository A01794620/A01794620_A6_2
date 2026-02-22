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


# pylint: disable=R0903
class Setting:
    """
    Setting:
    This is global system settings, which are default and
    essential for system to start (bootstrapping).
    """
    # System Core Settings
    SYSTEM_MAIN_MENU = "Main Menu"
    CANCEL_OPERATION_PHRASE = "CANCEL-OPERATION"
    SYSTEM_CANONICAL = "Aurora Reservations System"
    SYSTEM_MISSION = "Trustable Reservations Since 1970"
    SYSTEM_SUPPORT_EMAIL = "Tech Support: A01794620@tec.mx"
    # System file handling Settings
    SEP_PATH = "\\"
    HOTEL_PATH = "hotel"
    DATA_PATH = "data_set"
    FILE_EXTENSION = ".json"
    CUSTOMER_PATH = "customer"
    RESERVATION_PATH = "reservation"
    # System CLI usage format Settings
    OPEN_TAG = "«"
    CLOSE_TAG = "»"
    COL_WIDTH = 60
    NULL_VALUE = "Ø"
    NULL_NUMBER = -1
    HEAD_SYMBOL = "—"
    NULL_DATE_VALUE = "1970-01-01"
    # System Format evaluation Settings
    DATE_FORMAT = "%m-%d-%Y"
    ADDRESS_PATTERN = r"^\s*\S+(\s+\S+){0,19}\s*$"
    EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # System Synthetic data needed to try the
    # Unity testing and default values
    SYNTHETIC_DATA_INVALID_TYPE = 4
    SYNTHETIC_DATA_QUANTITY_NUMBER = 2
    SYNTHETIC_DATA_DATE = "1-1-2027"
    SYNTHETIC_DATA_ROOM_NUMBER = "D149"
    SYNTHETIC_DATA_PHONE_NUMBER = "+506 88785054"
    SYNTHETIC_DATA_EMAIL = "rsandi@gmail.com"
    SYNTHETIC_DATA_FULLNAME = "Ronald Sandí Quesada"
    SYNTHETIC_DATA_HOTEL_NAME = "Hotel the Green Bag In"
    SYNTHETIC_DATA_UUID = "afb4b554-6c0c-4c70-873c-9de1321bb55d"
    SYNTHETIC_FILE_ID_CREATE = \
        "3e3c9df2-c209-4cf7-913b-26227823f803"
    SYNTHETIC_DATA_UUID_WRONG = "afb4b554-cccc-4c70-cccc-9de1321bb55d"
    SYNTHETIC_DATA_ADDRESS = \
        "Av. Vasco de Quiroga N 3800 Col. Lomas de Santa Fe"
