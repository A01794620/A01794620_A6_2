from abstraction.AbstractionType import AbstractionType
from abstraction.Customer import Customer
from cli.MenuDescriptor import MenuDescriptor
from setting.Setting import Setting
from prompt_toolkit import prompt
from data_handling.JsonManager import JsonManager
from consolemenu import PromptUtils
from consolemenu import Screen

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
        user_input = prompt(f"Please confirm the customer deletion [Y/N]: ", default=f"N")
        pu.clear()
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

        customer_ = Customer()
        do_operation = True


        for index, customer_field in enumerate(MenuDescriptor.customer_fields):
            if do_operation:
                default_value = ""

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
                        default_value = ""

                # Validation until
                user_input = ""

                # if index == 0 or index == 1 or index == 2:

                is_good_value = False

                while do_operation and not is_good_value:
                    user_input = prompt(f"Please enter customer's {customer_field}: ", default=f"{default_value}")

                    if len(user_input)> 0:
                        default_value = user_input

                        if user_input == Setting.CANCEL_OPERATION_PHRASE:
                            do_operation = False
                        else:

                            if index == 0:
                                customer_.fullname = user_input
                                is_good_value = customer_.is_valid_fullname()
                            elif index == 1:
                                customer_.email = user_input
                                is_good_value = customer_.is_valid_email()
                            elif index == 2:
                                customer_.phone = user_input
                                is_good_value = customer_.is_valid_phone()
                                pu.clear()
                    else:
                        pass

                    if not is_good_value:
                        pu.clear()
                        print("Invalid Field. Please enter a valid value.\n\n" +
                              "Or type the phrase:\n\n" +
                              f"\t{Setting.OPEN_TAG} {Setting.CANCEL_OPERATION_PHRASE } "
                              f"{Setting.CLOSE_TAG}\n\nto go back to previous menu.")

                data_values.append(user_input)
                # else:
                #     data_values.append(user_input)

        # customer_ = Customer(data_values[0], data_values[1], data_values[2])


        if not is_new:
            customer_.id = on_record_customer.id

        JsonManager.create_data(AbstractionType.CUSTOMER, customer_)

        pu.clear()
        action = ""
        if is_new:
            action = "created"
            #print(f"Customer  successfully:")
            # print(f"{customer_.fullname} - New Client-ID: {customer_.id}")
            #print(customer_)
        else:
            action = "updated"
            #print(f"Customer updated successfully:")
            # print(f"{customer_.fullname} - Client-ID: {customer_.id}")
            # print(customer_)

        print(f"Customer {action} successfully:")
        print(customer_)
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
            CustomerHandler.delete_customer(customer)
        elif user_input == "M":
            CustomerHandler.register_customer(False, customer)
        else:
            print("Invalid Option System will return to previous menu.")

    @staticmethod
    def do_customer_removed():
        pu = PromptUtils(Screen())
        pu.clear()
        print("This Customer has been already removed.")
        pu.enter_to_continue()