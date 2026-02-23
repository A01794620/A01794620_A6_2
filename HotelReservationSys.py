"""
    Req 1. Implement a set of classes in Python that implements
           three abstractions:
           1. Hotel
           2. Reservation
           3. Customers
    Req 2. Implement a set of methods to handle the next
           persistent behaviors (stored in files):

           1. Hotels
            a. Create Hotel
            b. Delete Hotel
            c. Display Hotel information
            d. Modify Hotel Information
            e. Reserve a Room
            f. Cancel a Reservation

            2. Customer
            a. Create Customer
            b. Delete a Customer
            c. Display Customer Information
            d. Modify Customer Information

            3. Reservation
            a. Create a Reservation (Customer, Hotel)
            b. Cancel a Reservation

        You are free to decide the attributes within each class
        that enable the required behavior.

    Req 3. Implement unit test cases to exercise the methods in each class.
           Use the unittest module in Python.
    Req 4. The code coverage for all unittests should accumulate at
           least 85% of line coverage.
    Req 5. The program shall include the mechanism to handle invalid data in the file.
           Errors should be displayed in the console and the execution must continue.
    Req 6. Be compliant with PEP8.
    Req 7. The source code must show no warnings using Fleak and PyLint.
"""
from setting.Setting import Setting
from cli.MenuHandler import MenuHandler


if __name__ == '__main__':
    MenuHandler.show_system_menu(Setting.SYSTEM_CANONICAL, Setting.SYSTEM_MISSION + "\n" + Setting.SYSTEM_SUPPORT_EMAIL)