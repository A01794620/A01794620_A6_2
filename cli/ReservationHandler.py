from abstraction.Reservation import Reservation
from cli.MenuDescriptor import MenuDescriptor
from abstraction.Setting import Setting
from prompt_toolkit import prompt
from data_handling.JsonManager import JsonManager
from consolemenu import PromptUtils
from abstraction.AbstractionType import AbstractionType
from consolemenu import SelectionMenu
from typing import cast
from consolemenu.screen import Screen

class ReservationHandler:

    def __init__(self):
        pass

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
        print(f"Hotel Selected  : {hotel_items[selection_hotel]}")
        print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)

        data_values = []

        for index, customer_field in enumerate(MenuDescriptor.reservation_fields):
            default_value = ""
            user_input = prompt(f"Please enter Reservation's {customer_field}: ", default=f"{default_value}")
            data_values.append(user_input)

        reservation = Reservation(ids_hotel_items[selection_hotel], ids_items[selection], data_values[0], data_values[1], data_values[2], data_values[3])
        print(reservation)

        JsonManager.create_data(AbstractionType.RESERVATION, reservation)
        pu.clear()
        print(f"Reservation created successfully:")
        print(f"New Reservation-ID: {reservation.id}")
        pu.enter_to_continue()

    @staticmethod
    def display_cancel_reservations():
        reservations = JsonManager.display_data(AbstractionType.RESERVATION)
        reservations_lines = []
        pu = PromptUtils(Screen())
        pu.clear()

        for each_reservation in reservations:
            reservation = cast(Reservation, each_reservation)
            customer = JsonManager.retrieve_data(AbstractionType.CUSTOMER, reservation.customer_id)
            hotel = JsonManager.retrieve_data(AbstractionType.HOTEL, reservation.hotel_id)
            reservation_parts = reservation.id.split('-')

            reservation_line = f"¬{reservation_parts[0]}¬ {customer.fullname} in {hotel.name}, {reservation.room} on {reservation.date}"

            reservations_lines.append(reservation_line)

        print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)

        selection = SelectionMenu.get_selection(reservations_lines, title="Select the Reservation to be cancelled.",
                                                subtitle="Type a valid ordinal number to select the specific Reservation\n"
                                                         "Confirmation will be prompted before deleting the Reservation."
                                                , show_exit_option=False)

        reservation = cast(Reservation, reservations[selection])
        customer = JsonManager.retrieve_data(AbstractionType.CUSTOMER, reservation.customer_id)
        hotel = JsonManager.retrieve_data(AbstractionType.HOTEL, reservation.hotel_id)
        print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
        print("You have selected this reservation to be cancelled:")
        print(f"Unique Reservation ID:{reservation.id}")
        print(f"Customer:{customer.fullname}")
        print(f"Hotel:{hotel.name}")
        print(f"Date:{reservation.date}")

        print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)

        user_input = prompt(f"Enter [Y] for Delete the Reservation or [N] to cancel the deletion. ", default="N")
        pu.clear()

        if user_input == "Y":
            JsonManager.delete_data(AbstractionType.RESERVATION, reservation.id)
            print("Reservation cancelled successfully:.")
        elif user_input == "M":
            print("Deletion process has been cancelled.")
        else:
            print("Deletion process has been cancelled.")

        pu.enter_to_continue()