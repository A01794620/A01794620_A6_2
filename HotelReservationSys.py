# # https://console-menu.readthedocs.io/en/latest/installation.html
from cli.MenuHandler import MenuHandler


def start(name):
    MenuHandler.show_system_menu("Aurora Reservation System", "An Aurora Group Company")

if __name__ == '__main__':
    names = [
        'Roberto Brenes Mesen', 'Pedro Bull Narito', 'Maria Torres Alberatoe',
        'Luis Manual de la Torre', 'Hernan Derbez Pure', 'Eloisa Asofeifa Nuñez'
    ]
    start(".")