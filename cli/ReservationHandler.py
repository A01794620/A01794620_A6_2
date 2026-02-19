from abstraction.AbstractionType import AbstractionType
from abstraction.Reservation import Reservation
from cli.MenuDescriptor import MenuDescriptor
from abstraction.Setting import Setting
from prompt_toolkit import prompt
from data_handling.JsonManager import JsonManager
from consolemenu import *
# from cli.MenuHandler import MenuHandler
from abstraction.AbstractionType import AbstractionType
from consolemenu import SelectionMenu

class ReservationHandler:

    def __init__(self):
        pass

    # @staticmethod
    # def delete_customer(on_record_customer):
    #     pu = PromptUtils(Screen())
    #     pu.clear()
    #     print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
    #     print('Customer Removal Process')
    #     print(f"{on_record_customer.fullname} - Client-ID: {on_record_customer.id}")
    #     print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
    #     user_input = prompt(f"Please confirm the customer deletion [Y/N]:", default=f"N")
    #
    #     if user_input == "Y":
    #         JsonManager.delete_data(AbstractionType.CUSTOMER, on_record_customer.id)
    #         print(f"Customer deleted successfully.")
    #     else:
    #         print(f"Removal cancelled.")
    #
    #     pu.enter_to_continue()
    #

    @staticmethod
    def register_reservation():

        pu = PromptUtils(Screen())
        pu.clear()

        print( Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
        print('Create a new Reservation')
        customers = JsonManager.display_data(AbstractionType.CUSTOMER)

        customer_items = []
        ids_items = []

        for customer in customers:
            customer_items.append(f"{customer.fullname}")
            ids_items.append(customer.id)

        print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
        selection = SelectionMenu.get_selection(customer_items, title="Select the Customer for the Reservation", subtitle="Type a valid ordinal number to select the specific Customer.", show_exit_option=False)
        hotels = JsonManager.display_data(AbstractionType.HOTEL)
        hotel_items = []
        ids_hotel_items = []

        for hotel in hotels:
            hotel_items.append(f"{hotel.name}")
            ids_hotel_items.append(hotel.id)

        selection_hotel = SelectionMenu.get_selection(hotel_items, title="Select the Hotel for the Reservation", subtitle="Type a valid ordinal number to select the specific Hotel", show_exit_option=False)
        pu.clear()

        print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
        print(f"Customer Selected  : {customer_items[selection]}")
        #print(f"ID Selected Mapped := {ids_items[selection]}")
        print(f"Hotel Selected  : {hotel_items[selection_hotel]}")
        # print(f"ID Selected Mapped := {ids_hotel_items[selection_hotel]}")
        print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)

        data_values = []

        for index, customer_field in enumerate(MenuDescriptor.reservation_fields):
            default_value = ""
            user_input = prompt(f"Please enter Reservation's {customer_field}: ", default=f"{default_value}")
            data_values.append(user_input)

        reservation = Reservation(ids_hotel_items[selection_hotel], ids_items[selection], data_values[0], data_values[1])

        print(reservation)

        JsonManager.create_data(AbstractionType.RESERVATION, reservation)
        print(f"Reservation created successfully:")
        print(f"New Reservation-ID: {reservation.id}")
        pu.enter_to_continue()

    # @staticmethod
    # def handle_customer(customer):
    #     pu = PromptUtils(Screen())
    #     pu.clear()
    #     print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
    #     print('Customer Administration')
    #     print(f"{customer.fullname} - Unique Client-ID: {customer.id}")
    #     print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
    #     default_value = "M"
    #     user_input = prompt(f"Please enter [D] for Delete the customer or [M] for Modify the customer: ", default=f"{default_value}")
    #
    #     if user_input == "D":
    #         # print("We will delete the customer.")
    #         CustomerHandler.delete_customer(customer)
    #     elif user_input == "M":
    #         # print("We will modify the customer.")
    #         CustomerHandler.register_customer(False, customer)
    #     else:
    #         print("Invalid Option System will return to previous menu.")
    #
    # @staticmethod
    # def do_customer_removed():
    #     pu = PromptUtils(Screen())
    #     pu.clear()
    #     print("This Customer has been already removed.")
    #     pu.enter_to_continue()