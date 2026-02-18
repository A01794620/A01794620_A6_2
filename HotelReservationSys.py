from abstraction.AbstractionType import AbstractionType
import cli.MenuHandler
from cli.MenuHandler import MenuHandler
from data_handling.JsonManager import JsonManager
from prompt_toolkit import prompt
from consolemenu import *
from consolemenu.items import *
import datetime
import sys

#
# def update_and_show_menu(menu, new_item_text):
#     """Stops the menu, updates an item, and shows it again."""
#     # global pepe
#     # pepe += 1
#
#     # new_item_text = new_item_text + 1
#     menu.items.clear()
#
#     # In a simple script, you might not need to explicitly stop if it exited normally
#     # If running in a separate thread with menu.start(), use menu.stop() first
#     # Example of adding a new item
#     def new_function():
#         pu = PromptUtils(Screen())
#         ab = str(datetime.datetime.now())
#         print(f"This is the new function {ab}: {new_item_text}")
#         pu.enter_to_continue()
#
#     a = str(datetime.datetime.now())
#
#     new_function_item = FunctionItem(f"Call {a} {new_item_text}", new_function)
#     # menu.add_item(new_function_item)
#     menu.append_item(new_function_item)  # Adds the item to the internal list
#     # Re-display the menu to reflect changes
#     # menu.show() will handle the display logic
#     menu.show()
#
# # global pepe

def update_menu_dynamic():


    menu = ConsoleMenu(f"Dynamic Menu", "Initial Subtitle")

    # Function to add a new item
    def add_item(id_):
        print(id_)
        # ab = str(datetime.datetime.now())
        # new_item = MenuItem(f"New Item {ab} {len(menu.items)}")
        # menu.append_item(new_item)
        #new_item = MenuItem(f"New Item {ab} {len(menu.items)}")
        #menu.append_item(new_item)
        #print(ab)

        #print(menu.items)

        for each in menu.items:
            if str(each.text).startswith(id_):
                print(each.text)
                each.text = each.text + "< --- Found"
            else:
                pass

        #pu = PromptUtils(Screen())
        # pu.clear()
        #pu.enter_to_continue()

        # menu.clear_screen()
        # menu.go_up()
        # menu.show()
        #for each in menu.items:
        #    print(each)
        # menu.items.reverse()
        # The menu automatically handles re-drawing on the next user interaction
        # or you can force a refresh if necessary.

    # Function Item
    # item1 = FunctionItem("Add Item", add_item)
    # menu.append_item(item1)
    # Show the menu
    # menu.join()

    item_list = MenuHandler.list_files()

    for item in item_list:
        # print(item.name)
        item_i = FunctionItem(item.id + "|" + item.name, add_item, [item.id])
        # (FunctionItem)(item_i).get_text()
        menu.append_item(item_i)

    menu.show()


def start(name):
    update_menu_dynamic()
    # Create initial menu
    # menu = ConsoleMenu("Dynamic Menu", "Initial Subtitle")
    # initial_item = update_and_show_menu(menu, "aja")
    # initial_item = update_and_show_menu(menu, "eje")
    # update_and_show_menu(menu, initial_item)
    # global pepe
    # pepe = 1
    # update_and_show_menu(menu, "Pepe")

    #menu.append_item(initial_item)
    #menu.show()

    # To update and show, you would call the function above
    # This is a conceptual example, typical use involves user interaction to trigger the update
    # For instance, the 'initial_item' could call the 'update_and_show_menu' function
    # menu = ConsoleMenu("Customer", "Customer Menu")
    # initial_item = FunctionItem("Initial Function", lambda: print("Initial function called"))
    # menu.append_item(initial_item)
    # print("Hotel created!")
    # MenuHandler.get_menu("Reservation Management System", "For support contact\nA01794620@tec.mx\n(MNA)")
    #submenu_item = ConsoleMenu("Customer", "Customer Menu")
    #submenu_item.clear_screen_before_render = True
    #items = MenuHandler.list_files(submenu_item)
    #submenu_item.append_item(items[0])
    # Show the menu
    #submenu_item.start()
    #submenu_item.join()
    #submenu_item.exit()

    # submenu_item.show()
    # submenu_item.clear_screen()


    # submenu_item.clear_screen()
    # submenu_item.exit()
    # item = JsonManager.retrieve_data(AbstractionType.CUSTOMER, 'b287a73d-dd5f-4317-be3f-07fdbe1721f5')
    print(name)


if __name__ == '__main__':
    start("N")
    # start('Roberto Brenes Mesen')
    # start('Pedro Bull Narito')
    # start("Maria Torres Alberatoe")
    # start("Luis Manual de la Torre")
    # start("Hernan Derbez Pure")
    # start("Eloisa Asofeifa Nuñez")