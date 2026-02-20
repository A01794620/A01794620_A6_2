from abstraction.AbstractionType import AbstractionType
from abstraction.Hotel import Hotel
from cli.MenuDescriptor import MenuDescriptor
from abstraction.Setting import Setting
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

        for index, hotel_field in enumerate(MenuDescriptor.hotel_fields):

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

            user_input = prompt(f"Please enter hotel's {hotel_field}: ", default=f"{default_value}")
            data_values.append(user_input)


        hotel_ = Hotel(data_values[0], data_values[1], data_values[2], data_values[3])

        if not is_new:
            hotel_.id = on_record_hotel.id

        JsonManager.create_data(AbstractionType.HOTEL, hotel_)

        pu.clear()

        if is_new:
            print(f"Hotel created successfully:")
            print(f"{hotel_.name} - New Hotel-ID: {hotel_.id}")
        else:
            print(f"Hotel updated successfully:")
            print(f"{hotel_.name} - Hotel-ID: {hotel_.id}")

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