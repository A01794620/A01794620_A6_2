from abstraction.Reservation import Reservation
from cli.MenuDescriptor import MenuDescriptor
from setting.Setting import Setting
from data_handling.JsonManager import JsonManager
from abstraction.AbstractionType import AbstractionType
from consolemenu import SelectionMenu
from typing import cast
from consolemenu import PromptUtils
from consolemenu.screen import Screen
from prompt_toolkit import prompt

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

        # for index, customer_field in enumerate(MenuDescriptor.reservation_fields):
        #     default_value = ""
        #     user_input = prompt(f"Please enter Reservation's {customer_field}: ", default=f"{default_value}")
        #     data_values.append(user_input)

        #############################################
        reservation_ = Reservation()
        do_operation = True

        for index, reservation_field in enumerate(MenuDescriptor.reservation_fields):
            if do_operation:

                default_value = ""

                # Validation until
                user_input = ""

                is_good_value = False

                while do_operation and not is_good_value:

                    user_input = prompt(f"Please enter customer's {reservation_field}: ",
                                        default=f"{default_value}")

                    if len(user_input) > 0:
                        default_value = user_input

                        if user_input == Setting.CANCEL_OPERATION_PHRASE:
                            do_operation = False
                        else:
                            if index == 0:
                                reservation_.room = user_input
                                is_good_value = reservation_.is_valid_room()

                            elif index == 1:
                                if user_input.isnumeric():
                                    reservation_.adults_number = int(user_input)
                                    is_good_value = reservation_.is_valid_adult_quantity()
                            elif index == 2:
                                if user_input.isnumeric():
                                    reservation_.children_number = int(user_input)
                                    is_good_value = reservation_.is_valid_children_quantity()
                                #else:
                                #    pu.enter_to_continue()
                                #    print("M")
                                #    print(user_input)
                                #    pu.enter_to_continue()
                            elif index == 3:
                                reservation_.date = user_input
                                is_good_value = reservation_.is_valid_date()
                    else:
                        pass

                    if not is_good_value:
                        # pu.clear()
                        print("Invalid Field. Please enter a valid value.\n\n" +
                              "Or type the phrase:\n\n" +
                              f"\t{Setting.OPEN_TAG} {Setting.CANCEL_OPERATION_PHRASE} "
                              f"{Setting.CLOSE_TAG}\n\nto go back to previous menu.")

                data_values.append(user_input)
        #############################################


        #pu.enter_to_continue()

        # print("." * 40)
        # print(ids_hotel_items[selection_hotel])
        # print(ids_items[selection])
        # print(data_values[0])
        # print(data_values[1])
        # print(data_values[2])
        # print(data_values[3])
        # print("." * 40)
        #pu.enter_to_continue()

        # reservation = Reservation(ids_hotel_items[selection_hotel], ids_items[selection], data_values[0], data_values[1], data_values[2], data_values[3])
        # print(reservation)

        pu.clear()

        if do_operation:
            reservation_.hotel_id = ids_hotel_items[selection_hotel]
            reservation_.customer_id = ids_items[selection]

            JsonManager.create_data(AbstractionType.RESERVATION, reservation_)
            pu.clear()
            print(f"Reservation created successfully:")
            print(f"New Reservation-ID: {reservation_.id}")
            print(reservation_)
        else:
            print(f"Reservation Creation Cancelled.")

        pu.enter_to_continue()


    @staticmethod
    def display_cancel_reservations():
        pu = PromptUtils(Screen())
        pu.clear()

        reservations = JsonManager.display_data(AbstractionType.RESERVATION)
        # pu.enter_to_continue()
        reservations_lines = []


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
        # pu.clear()

        if user_input == "Y":
            JsonManager.delete_data(AbstractionType.RESERVATION, reservation.id)
            print("Reservation cancelled successfully.")
        elif user_input == "M":
            print("Deletion process has been cancelled.")
        else:
            print("Deletion process has been cancelled.")

        pu.enter_to_continue()