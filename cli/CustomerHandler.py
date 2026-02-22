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
from consolemenu import PromptUtils
from consolemenu import Screen
from prompt_toolkit import prompt

# Internal system libraries imports
from abstraction.Customer import Customer
from abstraction.AbstractionType import AbstractionType
from setting.Setting import Setting
from cli.MenuDescriptor import MenuDescriptor
from data_handling.JsonManager import JsonManager


class CustomerHandler:
    """
    This module is the interface between the CLI layer and the
    essential Customer entity.
    It performs the following actions:
    1. Create customers.
    2. Displays already created customers then by
       individual selection it:
       2.1 Edit customers.
       2.2 Delete customers.
    """
    def __init__(self):
        pass

    @staticmethod
    def delete_customer(on_record_customer):
        """
        Delete a specific customer artifact out of the system
          Customer object  void
        Args:
            on_record_customer (Customer): customer on system susceptible
            to be dropped.
        Returns:
            void: internal system deletion.
        """
        pu = PromptUtils(Screen())
        pu.clear()
        print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
        print('Customer Removal Process')
        print(f"{on_record_customer.fullname} "
              f"- Client-ID: {on_record_customer.id}")
        print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
        user_input = prompt("Please confirm the customer deletion [Y/N]: ",
                            default="N")
        pu.clear()
        if user_input == "Y":
            JsonManager.delete_data(AbstractionType.CUSTOMER,
                                    on_record_customer.id)
            print("Customer deleted successfully.")
        else:
            print("Removal cancelled.")

        pu.enter_to_continue()

    # Disabled on this fx:
    # (too-many-branches), (too-many-statements) and (too-many-nested-blocks)
    # pylint: disable=R0912, R0915, R1702
    @staticmethod
    def register_customer(is_new, on_record_customer):
        """
        Perform a registration from a customer information typed
        from end-user, it creates the associated objected and
        stores it in the system drive.
        Args:
            is_new (bool): either is a new or already existing customer.
            on_record_customer (Customer): in case of already existing
                                           customer this is the associated
                                           object.
        Returns:
            void: internal system artifact creation.
        """
        pu = PromptUtils(Screen())
        pu.clear()

        print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)

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
                    user_input = prompt(f"Please enter customer's "
                                        f"{customer_field}: ",
                                        default=f"{default_value}")

                    if len(user_input) > 0:
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
                        print("Invalid Field. "
                              "Please enter a valid value.\n\n" +
                              "Or type the phrase:\n\n" +
                              f"\t{Setting.OPEN_TAG} "
                              f"{Setting.CANCEL_OPERATION_PHRASE} "
                              f"{Setting.CLOSE_TAG}\n\n"
                              f"to go back to previous menu.")

                data_values.append(user_input)
                # else:
                #     data_values.append(user_input)

        # customer_ = Customer(data_values[0], data_values[1], data_values[2])

        pu.clear()

        if not is_new:
            customer_.id = on_record_customer.id

        action = ""

        if is_new:
            action = "Creation"
        else:
            action = "Update"

        if do_operation:
            JsonManager.create_data(AbstractionType.CUSTOMER, customer_)
            print(f"Customer {action} Successful.")
            print(customer_)
        else:
            print(f"Customer {action} Cancelled.")

        pu.enter_to_continue()

    @staticmethod
    def handle_customer(customer):
        """
        It receives a customer object and interacts
        with end-user to either modify it or delete it.
        Args:
            customer (Customer): .
        Returns:
           void: internal functions without returning values.
        """
        pu = PromptUtils(Screen())
        pu.clear()
        print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
        print('Customer Administration')
        print(f"{customer.fullname} - Unique Client-ID: {customer.id}")
        print(Setting.COL_WIDTH * Setting.HEAD_SYMBOL)
        default_value = "M"
        user_input = prompt("Please enter:\n"
                            "[M] for Modify the customer or\n"
                            "[D] for Delete the customer: ",
                            default=f"{default_value}")
        if user_input == "D":
            CustomerHandler.delete_customer(customer)
        elif user_input == "M":
            CustomerHandler.register_customer(False, customer)
        else:
            print("Invalid Option System will return to previous menu.")

    @staticmethod
    def do_customer_removed():
        """
        It displayed a helpful message when one customer just previously
        removed is selected.
        Args:
        Returns:
            void: internal system message.
         """
        pu = PromptUtils(Screen())
        pu.clear()
        print("This Customer has been already removed.")
        pu.enter_to_continue()
