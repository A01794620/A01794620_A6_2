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
    def create_new_customer():
        pu = PromptUtils(Screen())
        pu.clear()

        print( Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
        print('Create a new Customer')
        print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
        data_values = []
        for customer_field in MenuDescriptor.customer_fields:
            default_value = ""
            user_input = prompt(f"Please enter customer's {customer_field}: ", default=f"{default_value}")
            data_values.append(user_input)

        c = Customer(data_values[0], data_values[1], data_values[2])
        # print(c)
        JsonManager.create_data(AbstractionType.CUSTOMER, c)
        print(f"Customer created successfully:")
        print(f"{c.name} - New Client-ID: {c.id}")
        pu.enter_to_continue()

    @staticmethod
    def list_customers():
        pu = PromptUtils(Screen())
        pu.clear()
        print("Displaying all Customers")
        pu.enter_to_continue()