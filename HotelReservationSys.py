from cli.MenuHandler import MenuHandler
from abstraction.AbstractionType import AbstractionType
from consolemenu import SelectionMenu



def start(name):

    # a_list = ["Option One", "Option Two", "Option Three"]
    # selection = SelectionMenu.get_selection(a_list, title="", subtitle="", show_exit_option=False)
    # print(f"You selected: {a_list[selection]}")
    MenuHandler.show_system_menu("Aurora Reservation System", "An Aurora Group Company")
    # result = MenuHandler.menu_dynamic_handler(AbstractionType.CUSTOMER, False)
    # print(result)
    # Rerv = Reservation("hotel_id", "customer_id", room="1243", date="18/02/2026")
    # print(Rerv)

if __name__ == '__main__':
    names = [
        'Roberto Brenes Mesen', 'Pedro Bull Narito', 'Maria Torres Alberatoe',
        'Luis Manual de la Torre', 'Hernan Derbez Pure', 'Eloisa Asofeifa Nuñez'
    ]
    start(".")