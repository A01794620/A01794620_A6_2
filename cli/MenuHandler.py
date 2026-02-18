from abstraction.Customer import Customer
from cli.MenuCustomer import MenuCustomer
from cli.MenuDescriptor import MenuDescriptor
from data_handling.JsonManager import JsonManager
from abstraction.AbstractionType import AbstractionType
from prompt_toolkit import prompt
from typing import cast
from cli.CustomerHandler import CustomerHandler
# from consolemenu import ConsoleMenu
# from consolemenu.items import FunctionItem
from consolemenu import *
from consolemenu.items import *


class MenuHandler:

    def __init__(self):
        pass
    @staticmethod
    def item_handler(args_):
        # pu = PromptUtils(Screen())
        # pu.clear()
        values = args_.split("-")
        item_root = int(values[0])
        item_branch = int(values[1])

        if item_root == AbstractionType.CUSTOMER.value:
            # print("ON Customer")
            if item_branch == MenuCustomer.CREATE.value:
                CustomerHandler.create_new_customer()
                # CustomerHandler.create_new_customer()
                # CustomerHandler.create_new_customer()
                # print("ON Create Customer")
            else:
                print("Some other place but in Customer Area still :-_-")
        else:
            print("in other place")

        # pu.enter_to_continue()

    @staticmethod
    def show_system_menu(title, sub_title):

        main_menu = ConsoleMenu(title, sub_title)

        for index, sub_branch in enumerate(MenuDescriptor.root_menu):
            # for sub_branch in MenuDescriptor.root_menu:
            submenu_item = ConsoleMenu(f"{sub_branch} Management", sub_branch)
            submenu_item_root = SubmenuItem(f"{sub_branch} Options ...", submenu=submenu_item)
            ###

            # print(index)

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

    # @staticmethod
    # def get_menu(title, subtitle):
    #     main_menu = ConsoleMenu(title, subtitle)
    #     # hotel_item = MenuItem("::: Reservation Management System :::")
    #     function_item = FunctionItem("Create new customer", MenuHandler.test_fx)
    #     # hotel_selection_sub_menu = SelectionMenu(
    #     #     [function_item, "Create new customer",
    #     #      "Delete existing customer",
    #     #      "Display Customer Information",
    #     #      "Modify existing customer"
    #     # ])
    #     #function_item = FunctionItem("Call a Python function", input, ["Enter an input"])
    #     #command_item = CommandItem("Run a console command", "touch hello.txt")
    #     # submenu_item = SubmenuItem("Customers Management", hotel_selection_sub_menu , main_menu)
    #     submenu_item = ConsoleMenu("Customer", "Customer Menu")
    #     # sub_menu_item.add_item(function_item)
    #     submenu_item.append_item(function_item)
    #     submenu_item_2 = SubmenuItem("Customers Management", submenu=submenu_item)
    #     submenu_item_2.set_menu(main_menu)
    #     # menu.append_item(menu_item)
    #     # menu.append_item(function_item)
    #     # menu.append_item(command_item)
    #     main_menu.append_item(submenu_item_2)
    #     #main_menu.append_item(function_item)
    #     main_menu.show()
    #     return True

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
        # print("OK")
        obj_container = JsonManager.display_data(AbstractionType.CUSTOMER)
        #submenu_item = ConsoleMenu("Customer", "Customer Menu")
        items = []

        for obj in obj_container:
            c = Customer(obj.name)
            c.id = obj.id
            c.name = obj.name
            items.append(obj)

        #    function_item = FunctionItem(f"{obj.name}", MenuHandler.file_selection, [obj.id])
        #    items.append(function_item)
        # submenu_item.append_item(function_item)
        # print(obj)

        # return submenu_item
        # submenu_item.show()
        # def display_data(data_type):
        return items


    @staticmethod
    def file_selection(id_):

        try:
            pu = PromptUtils(Screen())
            pu.clear()
            # print(type(handler))
            c = JsonManager.retrieve_data(AbstractionType.CUSTOMER, id_)
            _name = prompt("Name :=", default=c.name)
            _age = prompt("Age  :=", default=c.name)
            print(f"{_name} {_age}")
            print(c)
            print(id_)
            c.name = _name
            c.age = 90
            JsonManager.create_data(AbstractionType.CUSTOMER, c)
            # print(handler)
            #print(type(handler))
            pu.enter_to_continue()
            #handler.show()

            #ConsoleMenu(handler).

            # sys.exit()
            # pu.enter_to_continue()
            # handler.items.clear()
            #handler.clear_screen()
            # handler.exit()
        except AttributeError as e:
            print(f"Another error occurred: {e}")
        except TypeError as e:
            print(f"Another error occurred: {e}")

    @staticmethod
    def menu_dynamic_handler():
        menu = ConsoleMenu(f"Dynamic Menu", "Initial Subtitle")

        def add_item(id_):
            for each in menu.items:
                each_i = cast(FunctionItem, each)

                if isinstance(each_i, FunctionItem):
                    if each_i.args[0] == id_:
                        c = JsonManager.retrieve_data(AbstractionType.CUSTOMER, each_i.args[0])
                        each_i.text = c.name + '^'
                    else:
                        pass
                else:
                    pass

        item_list = MenuHandler.list_files()

        for item in item_list:
            item_i = FunctionItem(item.name, add_item, [item.id])
            menu.append_item(item_i)

        menu.show()