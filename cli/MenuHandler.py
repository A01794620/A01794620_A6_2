from asyncio import print_call_graph
from operator import index

from consolemenu import *
from consolemenu.items import *
from abstraction.Customer import Customer
from data_handling.JsonManager import JsonManager
from abstraction.AbstractionType import AbstractionType

# from data_handling.JsonManager import JsonManager

class MenuHandler:

    def __init__(self):
        pass

    @staticmethod
    def get_menu(title, subtitle):

        main_menu = ConsoleMenu(title, subtitle)

        # hotel_item = MenuItem("::: Reservation Management System :::")

        function_item = FunctionItem("Create new customer", MenuHandler.test_fx)

        # hotel_selection_sub_menu = SelectionMenu(
        #     [function_item, "Create new customer",
        #      "Delete existing customer",
        #      "Display Customer Information",
        #      "Modify existing customer"
        # ])

        #function_item = FunctionItem("Call a Python function", input, ["Enter an input"])
        #command_item = CommandItem("Run a console command", "touch hello.txt")

        # submenu_item = SubmenuItem("Customers Management", hotel_selection_sub_menu , main_menu)
        submenu_item = ConsoleMenu("Customer", "Customer Menu")
        # sub_menu_item.add_item(function_item)
        submenu_item.append_item(function_item)
        submenu_item_2 = SubmenuItem("Customers Management", submenu=submenu_item)
        submenu_item_2.set_menu(main_menu)

        # menu.append_item(menu_item)
        # menu.append_item(function_item)
        # menu.append_item(command_item)
        main_menu.append_item(submenu_item_2)
        #main_menu.append_item(function_item)
        main_menu.show()
        return True

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

        #print(fields_values)
        print(c.id)
        print(c.name)
        JsonManager.create_data(AbstractionType.CUSTOMER, c)

        pu.enter_to_continue()

    @staticmethod
    def list_files():
        print("OK")

        obj_container = JsonManager.display_data(AbstractionType.CUSTOMER)
        submenu_item = ConsoleMenu("Customer", "Customer Menu")

        for obj in obj_container:
            function_item = FunctionItem(f"Customer {obj.name}", MenuHandler.file_selection, [obj.id])
            submenu_item.append_item(function_item)
            # print(obj)

        submenu_item.show()
        # def display_data(data_type):

    @staticmethod
    def file_selection(id):
        print(id)
        pu = PromptUtils(Screen())
        pu.enter_to_continue()