from cli.MenuCustomer import MenuCustomer
from cli.MenuDescriptor import MenuDescriptor
from cli.MenuHotel import MenuHotel
from cli.MenuReservation import MenuReservation
from data_handling.JsonManager import JsonManager
from abstraction.AbstractionType import AbstractionType
from typing import cast
from cli.CustomerHandler import CustomerHandler
from consolemenu import *
from consolemenu.items import *
from cli.HotelHandler import HotelHandler
from cli.ReservationHandler import ReservationHandler

class MenuHandler:

    def __init__(self):
        pass

    @staticmethod
    def item_handler(args_):
        values = args_.split("-")
        item_root = int(values[0])
        item_branch = int(values[1])

        if item_root == AbstractionType.CUSTOMER.value:
            if item_branch == MenuCustomer.CREATE.value:
                CustomerHandler.register_customer(True, None)
            elif item_branch == MenuCustomer.DISPLAY.value:
                MenuHandler.menu_dynamic_handler(AbstractionType.CUSTOMER)
            else:
                pass
        elif item_root == AbstractionType.HOTEL.value:
            if item_branch == MenuHotel.CREATE.value:
                HotelHandler.register_hotel(True, None)
            elif item_branch == MenuHotel.DISPLAY.value:
                MenuHandler.menu_dynamic_handler(AbstractionType.HOTEL)
            else:
                pass
        elif item_root == AbstractionType.RESERVATION.value:
            if item_branch == MenuReservation.CREATE.value:
                ReservationHandler.register_reservation()
            elif item_branch == MenuHotel.DISPLAY.value:
                ReservationHandler.display_cancel_reservations()
            else:
                pass
        else:
            pass

    @staticmethod
    def show_system_menu(title, sub_title):
        main_menu = ConsoleMenu(title, sub_title)

        for index, sub_branch in enumerate(MenuDescriptor.root_menu):
            submenu_item = ConsoleMenu(f"{sub_branch} Management", sub_branch)
            submenu_item_root = SubmenuItem(f"{sub_branch} Operations", submenu=submenu_item)

            if index == AbstractionType.CUSTOMER.value:
                for index_item, customer_branch in enumerate(MenuDescriptor.customer_menu):
                    # print(customer_branch)
                    args = [str(index) + "-" +  str(index_item)]
                    function_item = FunctionItem(customer_branch, MenuHandler.item_handler, args)
                    submenu_item.append_item(function_item)
            elif index == AbstractionType.HOTEL.value:
                for index_item, hotel_branch in enumerate(MenuDescriptor.hotel_menu):
                    # print(hotel_branch)
                    args = [str(index) + "-" +  str(index_item)]
                    function_item = FunctionItem(hotel_branch, MenuHandler.item_handler, args)
                    submenu_item.append_item(function_item)
            elif index == AbstractionType.RESERVATION.value:
                for index_item, reservation_branch in enumerate(MenuDescriptor.reservation_menu):
                    args = [str(index) + "-" +  str(index_item)]
                    function_item = FunctionItem(reservation_branch, MenuHandler.item_handler, args)
                    submenu_item.append_item(function_item)

            submenu_item_root.set_menu(main_menu)
            main_menu.append_item(submenu_item_root)

        main_menu.show()

    @staticmethod
    def menu_dynamic_handler(data_type):
        pu = PromptUtils(Screen())
        pu.clear()

        menu = ConsoleMenu(f"List",
                           "Aurora Reservation System\n"
                           "Select one ordinal number from the list.")

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
                                customer = JsonManager.retrieve_data(AbstractionType.CUSTOMER, each_i.args[0])
                                CustomerHandler.handle_customer(customer)

                                if JsonManager.has_data(AbstractionType.CUSTOMER, each_i.args[0]):
                                    customer_retrieved = JsonManager.retrieve_data(AbstractionType.CUSTOMER, id_)
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
                                hotel = JsonManager.retrieve_data(AbstractionType.HOTEL, each_i.args[0])
                                HotelHandler.handle_hotel(hotel)

                                if JsonManager.has_data(AbstractionType.HOTEL, each_i.args[0]):
                                    hotel_retrieved = JsonManager.retrieve_data(AbstractionType.HOTEL, id_)
                                    each_i.text = hotel_retrieved.name
                                else:
                                    each_i.text += " <Deleted>"
                            else:
                                print("")

                        pass
                    else:
                        pass

                else:
                    pass

        obj_container = JsonManager.display_data(data_type)

        if data_type == AbstractionType.CUSTOMER:
            for customer_ in obj_container:
                item_i = FunctionItem(customer_.fullname, add_item, [customer_.id])
                menu.append_item(item_i)
        elif data_type == AbstractionType.HOTEL:
            for hotel_ in obj_container:
                item_i = FunctionItem(hotel_.name, add_item, [hotel_.id])
                menu.append_item(item_i)
        else:
            print("not implemented yet")

        menu.show()