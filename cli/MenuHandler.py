from abstraction.Customer import Customer
from cli.MenuCustomer import MenuCustomer
from cli.MenuDescriptor import MenuDescriptor
from data_handling.JsonManager import JsonManager
from abstraction.AbstractionType import AbstractionType
from prompt_toolkit import prompt
from typing import cast
from cli.CustomerHandler import CustomerHandler
from consolemenu import *
from consolemenu.items import *

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
                print("Some other place but in Customer Area still :-_-")
                MenuHandler.menu_dynamic_handler()
            else:
                pass
        else:
            print("in other place")

    @staticmethod
    def show_system_menu(title, sub_title):

        main_menu = ConsoleMenu(title, sub_title)

        for index, sub_branch in enumerate(MenuDescriptor.root_menu):
            submenu_item = ConsoleMenu(f"{sub_branch} Management", sub_branch)
            submenu_item_root = SubmenuItem(f"{sub_branch} Options ...", submenu=submenu_item)

            if index == AbstractionType.CUSTOMER.value:

                for index_item, customer_branch in enumerate(MenuDescriptor.customer_menu):
                    print(customer_branch)
                    args = [str(index) + "-" +  str(index_item)]
                    function_item = FunctionItem(customer_branch, MenuHandler.item_handler, args)
                    submenu_item.append_item(function_item)

            ###
            submenu_item_root.set_menu(main_menu)
            main_menu.append_item(submenu_item_root)

        main_menu.show()


    @staticmethod
    def test_fx():
        enter_data = True

        fields_labels = ["FullName", "Age"]
        fields_values = []

        pu = PromptUtils(Screen())

        index = 0

        while enter_data:
            index += 1
            # PromptUtils.input() returns an InputResult
            result = pu.input(f"Enter {fields_labels[index-1]}")
            pu.println("\nYou entered:", result.input_string, "\n")
            fields_values.append(result.input_string)

            if (index+1) > len(fields_labels):
                enter_data = False
            else:
                print(f"index : {index}")

        c = Customer(fields_values[0])

        JsonManager.create_data(AbstractionType.CUSTOMER, c)
        pu.enter_to_continue()


    @staticmethod
    def file_selection(id_):

        try:
            pu = PromptUtils(Screen())
            pu.clear()
            c = JsonManager.retrieve_data(AbstractionType.CUSTOMER, id_)

            _name = prompt("Name :=", default=c.name)
            _age = prompt("Age  :=", default=c.name)

            print(f"{_name} {_age}")
            print(c)
            print(id_)
            c.name = _name
            c.age = 90
            JsonManager.create_data(AbstractionType.CUSTOMER, c)
            pu.enter_to_continue()
        except AttributeError as e:
            print(f"Another error occurred: {e}")
        except TypeError as e:
            print(f"Another error occurred: {e}")

    @staticmethod
    def menu_dynamic_handler():
        pu = PromptUtils(Screen())
        pu.clear()

        menu = ConsoleMenu(f"Customer List",
                           "Aurora Reservation System\nSelect one ordinal number from the customer list.")

        def add_item(id_):

            for each in menu.items:
                each_i = cast(FunctionItem, each)

                if isinstance(each_i, FunctionItem):

                    if "<Deleted>" in each_i.text:
                        # print("This Customer has been already removed.")
                        return

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

                    # each_i.text = c.name + '^'

                else:
                    pass

            # pu.enter_to_continue()


        obj_container = JsonManager.display_data(AbstractionType.CUSTOMER)


        for customer_ in obj_container:
            item_i = FunctionItem(customer_.fullname, add_item, [customer_.id])
            menu.append_item(item_i)


        menu.show()
