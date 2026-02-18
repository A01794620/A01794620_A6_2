from abstraction.AbstractionType import AbstractionType
from abstraction.Customer import Customer
from cli.MenuDescriptor import MenuDescriptor
from abstraction.Setting import Setting
from prompt_toolkit import prompt
from data_handling.JsonManager import JsonManager
from consolemenu import *

class CustomerHandler:

    def __init__(self):
        pass

    @staticmethod
    def delete_customer(on_record_customer):
        pu = PromptUtils(Screen())
        pu.clear()
        print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
        print('Customer Removal Process')
        print(f"{on_record_customer.fullname} - Client-ID: {on_record_customer.id}")
        print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
        user_input = prompt(f"Please confirm the customer deletion [Y/N]:", default=f"N")

        if user_input == "Y":
            JsonManager.delete_data(AbstractionType.CUSTOMER, on_record_customer.id)
            print(f"Customer deleted successfully.")
        else:
            print(f"Removal cancelled.")

        pu.enter_to_continue()

    @staticmethod
    def register_customer(is_new, on_record_customer):
        pu = PromptUtils(Screen())
        pu.clear()

        print( Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
        if is_new:
            print('Create a new Customer')
        else:
            print('Edit an existing Customer')

        print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
        data_values = []

        for index, customer_field in enumerate(MenuDescriptor.customer_fields):

            default_value = "<enter a value>"

            if is_new:
                default_value = ""
            else:
                if index == 0:
                    default_value = on_record_customer.fullname
                elif index == 1:
                    default_value = on_record_customer.email
                elif index == 2:
                    default_value = on_record_customer.phone
                else:
                    default_value = "<enter a value>"

            user_input = prompt(f"Please enter customer's {customer_field}: ", default=f"{default_value}")
            data_values.append(user_input)

        customer_ = Customer(data_values[0], data_values[1], data_values[2])

        if not is_new:
            customer_.id = on_record_customer.id

        JsonManager.create_data(AbstractionType.CUSTOMER, customer_)

        if is_new:
            print(f"Customer created successfully:")
            print(f"{customer_.fullname} - New Client-ID: {customer_.id}")
        else:
            print(f"Customer  updated successfully:")
            print(f"{customer_.fullname} - Client-ID: {customer_.id}")

        pu.enter_to_continue()

    @staticmethod
    def handle_customer(customer):
        pu = PromptUtils(Screen())
        pu.clear()
        print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
        print('Customer Administration')
        print(f"{customer.fullname} - Unique Client-ID: {customer.id}")
        print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
        default_value = "M"
        user_input = prompt(f"Please enter [D] for Delete the customer or [M] for Modify the customer: ", default=f"{default_value}")

        if user_input == "D":
            # print("We will delete the customer.")
            CustomerHandler.delete_customer(customer)
        elif user_input == "M":
            # print("We will modify the customer.")
            CustomerHandler.register_customer(False, customer)
        else:
            print("Invalid Option System will return to previous menu.")

        # pu.enter_to_continue()

    # @staticmethod
    # def list_customers():
    #     pu = PromptUtils(Screen())
    #     pu.clear()
    #     print("Displaying all Customers")
    #     pu.enter_to_continue()