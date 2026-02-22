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
from typing import cast
from consolemenu import ConsoleMenu
from consolemenu import Screen
from consolemenu import PromptUtils
from consolemenu.items import FunctionItem
from consolemenu.items import SubmenuItem
# Local system imported libraries
from setting.Setting import Setting

from cli.MenuType import MenuType
from cli.HotelHandler import HotelHandler
from cli.MenuDescriptor import MenuDescriptor
from cli.CustomerHandler import CustomerHandler
from cli.ReservationHandler import ReservationHandler

from data_handling.JsonManager import JsonManager
from abstraction.AbstractionType import AbstractionType


class MenuHandler:
    """
    Every handler is articulated by a super handler component
    which is the MenuHandler, which holds all the deployed
    system functions.
    """
    def __init__(self):
        pass

    @staticmethod
    def show_system_menu(title, sub_title):
        """
        It shows the main system menu to start using the system.
        Args:
            title (str): title of the system.
            sub_title (str): subtitle of the system
        Returns:
            void: internal system function to show.
        """
        main_menu = ConsoleMenu(title, sub_title)

        for index, sub_branch in enumerate(MenuDescriptor.root_menu):
            submenu_item = ConsoleMenu(Setting.SYSTEM_CANONICAL +
                                       '\n' + Setting.SYSTEM_MISSION,
                                       f"{sub_branch} Management")

            submenu_item_root = (
                                 SubmenuItem(
                                     f"{sub_branch} Operations",
                                     submenu=submenu_item)
                                )

            if index == AbstractionType.CUSTOMER.value:

                for (index_item,
                     customer_branch) in (
                        enumerate(MenuDescriptor.customer_menu)):

                    args = [str(index) + "-" + str(index_item)]

                    function_item = FunctionItem(
                        customer_branch,
                        MenuHandler.item_handler,
                        args)

                    submenu_item.append_item(function_item)

                submenu_item.exit_item.text = (f"Return to"
                                               f" {Setting.SYSTEM_MAIN_MENU} "
                                               f"{Setting.OPEN_TAG * 2}")

            elif index == AbstractionType.HOTEL.value:

                for (index_item,
                     hotel_branch) in enumerate(MenuDescriptor.hotel_menu):
                    args = [str(index) + "-" + str(index_item)]
                    function_item = (
                        FunctionItem(hotel_branch,
                                     MenuHandler.item_handler,
                                     args))
                    submenu_item.append_item(function_item)

                submenu_item.exit_item.text = (f"Return to"
                                               f" {Setting.SYSTEM_MAIN_MENU}"
                                               f" {Setting.OPEN_TAG * 2}")

            elif index == AbstractionType.RESERVATION.value:

                for (
                        index_item,
                        reservation_branch
                     ) in (
                        enumerate(MenuDescriptor.reservation_menu)
                ):

                    args = [str(index) + "-" + str(index_item)]
                    function_item = FunctionItem(reservation_branch,
                                                 MenuHandler.item_handler,
                                                 args)
                    submenu_item.append_item(function_item)
                submenu_item.exit_item.text = (f"Return to "
                                               f"{Setting.SYSTEM_MAIN_MENU} "
                                               f"{Setting.OPEN_TAG * 2}")

            submenu_item_root.set_menu(main_menu)
            main_menu.append_item(submenu_item_root)

        main_menu.show()

    # Disabled on this fx:
    # (too-many-branches), (too-many-statements),
    # (too-many-nested-blocks) and (too-many-locals)
    # pylint: disable=R0912, R0915, R1702, R0914
    @staticmethod
    def item_handler(args_):
        """
        It is a builder for all the menu options.
        Args:
            args_ (str[]): Array of String holding two parts:
                           - Sub_branch of the menu.
                           - Item id in the menu for easy tracking.
        Returns:
            void: internal system function to show.
        """
        values = args_.split("-")
        item_root = int(values[0])
        item_branch = int(values[1])

        if item_root == AbstractionType.CUSTOMER.value:
            if item_branch == MenuType.CREATE.value:
                CustomerHandler.register_customer(True, None)
            elif item_branch == MenuType.DISPLAY.value:
                MenuHandler.menu_dynamic_handler(AbstractionType.CUSTOMER)
            else:
                pass
        elif item_root == AbstractionType.HOTEL.value:
            if item_branch == MenuType.CREATE.value:
                HotelHandler.register_hotel(True, None)
            elif item_branch == MenuType.DISPLAY.value:
                MenuHandler.menu_dynamic_handler(AbstractionType.HOTEL)
            else:
                pass
        elif item_root == AbstractionType.RESERVATION.value:
            if item_branch == MenuType.CREATE.value:
                ReservationHandler.register_reservation()
            elif item_branch == MenuType.DISPLAY.value:
                ReservationHandler.display_cancel_reservations()
            else:
                pass
        else:
            pass

    # pylint: disable=C0301
    @staticmethod
    def menu_dynamic_handler(data_type):
        """
         It is a layer to interacts between each
         abstraction handler and the main menu.

        Args:
            data_type (enum): The type of abstraction
            from abstraction.AbstractionType
        Returns:
            void: internal system function to show.
        """
        pu = PromptUtils(Screen())
        pu.clear()

        label = ""
        if data_type == AbstractionType.CUSTOMER:
            label = "Customer"
        elif data_type == AbstractionType.HOTEL:
            label = "Hotel"
        elif data_type == AbstractionType.RESERVATION:
            label = "Reservation"
        else:
            pass

        menu = ConsoleMenu(Setting.SYSTEM_CANONICAL + '\n' +
                           Setting.SYSTEM_MISSION,
                           f"{label} Administration Module\n" +
                           f"Enter a number from the list below to "
                           f"select the specific {label}.\n"
                           "The last number will return to previous"
                           " menu.\n"
                           "An invalid number selection will"
                           " be voided.")

        def add_item(id_):
            for each in menu.items:
                each_i = cast(FunctionItem, each)

                if isinstance(each_i, FunctionItem):

                    if data_type == AbstractionType.CUSTOMER:

                        if "<Deleted>" in each_i.text:

                            if each_i.args[0] == id_:
                                CustomerHandler.do_customer_removed()

                        else:
                            if each_i.args[0] == id_:

                                customer = (
                                    JsonManager.retrieve_data(
                                        AbstractionType.CUSTOMER,
                                        each_i.args[0]))

                                CustomerHandler.handle_customer(customer)

                                if JsonManager.has_data(AbstractionType.CUSTOMER, each_i.args[0]):  # noqa: E501
                                    customer_retrieved = JsonManager.retrieve_data(AbstractionType.CUSTOMER, id_)  # noqa: E501

                                    each_i.text = customer_retrieved.fullname
                                else:
                                    each_i.text += " <Deleted>"
                            else:
                                print("")

                    elif data_type == AbstractionType.HOTEL:

                        if "<Deleted>" in each_i.text:
                            if each_i.args[0] == id_:
                                HotelHandler.do_hotel_removed()
                        else:
                            if each_i.args[0] == id_:
                                hotel = \
                                    JsonManager.retrieve_data(AbstractionType.HOTEL, each_i.args[0])   # noqa: E501

                                HotelHandler.handle_hotel(hotel)

                                if JsonManager.has_data(AbstractionType.HOTEL,
                                                        each_i.args[0]):
                                    hotel_retrieved = (
                                        JsonManager.retrieve_data(AbstractionType.HOTEL, id_))  # noqa: E501
                                    each_i.text = hotel_retrieved.name
                                else:
                                    each_i.text += " <Deleted>"
                            else:
                                print("")

                    else:
                        pass

                else:
                    pass

        obj_container = JsonManager.display_data(data_type)

        if data_type == AbstractionType.CUSTOMER:
            for customer_ in obj_container:
                item_i = FunctionItem(customer_.fullname,
                                      add_item,
                                      [customer_.id])
                menu.append_item(item_i)
        elif data_type == AbstractionType.HOTEL:
            for hotel_ in obj_container:
                item_i = FunctionItem(hotel_.name, add_item, [hotel_.id])
                menu.append_item(item_i)
        else:
            print("not implemented yet")

        menu.show()
