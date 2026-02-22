from abstraction.AbstractionType import AbstractionType
from abstraction.Hotel import Hotel
from cli.MenuDescriptor import MenuDescriptor
from setting.Setting import Setting
from prompt_toolkit import prompt
from data_handling.JsonManager import JsonManager
from consolemenu import PromptUtils
from consolemenu import Screen

class HotelHandler:

    def __init__(self):
        pass

    @staticmethod
    def delete_hotel(on_record_hotel):
        pu = PromptUtils(Screen())
        pu.clear()
        print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
        print('Hotel Removal Process')
        print(f"{on_record_hotel.name} - Hotel-ID: {on_record_hotel.id}")
        print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
        user_input = prompt(f"Please confirm the Hotel deletion [Y/N]: ", default=f"N")
        pu.clear()

        if user_input == "Y":
            JsonManager.delete_data(AbstractionType.HOTEL, on_record_hotel.id)
            print(f"Hotel deleted successfully.")
        else:
            print(f"Removal cancelled.")

        pu.enter_to_continue()

    @staticmethod
    def register_hotel(is_new, on_record_hotel):

        pu = PromptUtils(Screen())
        pu.clear()

        print( Setting.COL_WIDTH * Setting.HEAD_SYMBOL)

        if is_new:
            print('Create a new Hotel')
        else:
            print('Edit an existing Hotel')

        print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
        data_values = []

        hotel_ = Hotel()
        do_operation = True


        for index, hotel_field in enumerate(MenuDescriptor.hotel_fields):
            if do_operation:
                default_value = ""

                if is_new:
                    default_value = ""
                else:
                    if index == 0:
                        default_value = on_record_hotel.name
                    elif index == 1:
                        default_value = on_record_hotel.address
                    elif index == 2:
                        default_value = on_record_hotel.email
                    elif index == 3:
                        default_value = on_record_hotel.phone
                    else:
                        default_value = ""

                # Validation until
                user_input = ""
                is_good_value = False
                while do_operation and not is_good_value:
                ########################################
                    user_input = prompt(f"Please enter hotel's {hotel_field}: ", default=f"{default_value}")

                    if len(user_input) > 0:
                        default_value = user_input

                        if user_input == Setting.CANCEL_OPERATION_PHRASE:
                            do_operation = False
                        else:
                            # print(f"Index:={index}")
                            if index == 0:
                                hotel_.name = user_input
                                is_good_value = hotel_.is_valid_name()
                            elif index == 1:
                                hotel_.address = user_input
                                is_good_value = hotel_.is_valid_address()
                            elif index == 2:
                                hotel_.email = user_input
                                is_good_value = hotel_.is_valid_email()
                                pu.clear()
                            elif index == 3:
                                hotel_.phone = user_input
                                is_good_value = hotel_.is_valid_phone()
                                pu.clear()
                    else:
                        pass

                    if not is_good_value:
                        # pu.clear()
                        print("Invalid Field. Please enter a valid value.\n\n" +
                              "Or type the phrase:\n\n" +
                              f"\t{Setting.OPEN_TAG} {Setting.CANCEL_OPERATION_PHRASE} "
                              f"{Setting.CLOSE_TAG}\n\nto go back to previous menu.\n")

                ######################################

                # user_input = prompt(f"Please enter hotel's {hotel_field}: ", default=f"{default_value}")
                data_values.append(user_input)


        # hotel_ = Hotel(data_values[0], data_values[1], data_values[2], data_values[3])

        # pu.enter_to_continue()
        # return

        pu.clear()

        if not is_new:
            hotel_.id = on_record_hotel.id

        action = ""

        if is_new:
            action = "Creation"
        else:
            action = "Update"

        if do_operation:
            JsonManager.create_data(AbstractionType.HOTEL, hotel_)
            print(f"Hotel {action} Successful.")
            print(hotel_)
        else:
            print(f"Hotel {action} Cancelled.")

        pu.enter_to_continue()

    @staticmethod
    def handle_hotel(hotel):
        pu = PromptUtils(Screen())
        pu.clear()
        print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
        print('Hotel Administration')
        print(f"{hotel.name} - Unique Hotel-ID: {hotel.id}")
        print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
        default_value = "M"
        user_input = prompt(f"Please enter [D] for Delete the Hotel or [M] for Modify the Hotel: ", default=f"{default_value}")

        if user_input == "D":
            HotelHandler.delete_hotel(hotel)
        elif user_input == "M":
            HotelHandler.register_hotel(False, hotel)
        else:
            print("Invalid Option System will return to previous menu.")

    @staticmethod
    def do_hotel_removed():
        pu = PromptUtils(Screen())
        pu.clear()
        print("This Hotel has been already removed.")
        pu.enter_to_continue()