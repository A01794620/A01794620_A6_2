from cli.MenuHandler import MenuHandler
from cli.ReservationHandler import ReservationHandler

def start(name):
    # ReservationHandler.display_reservations()
    MenuHandler.show_system_menu("Aurora Reservation System", "An Aurora Group Company")

if __name__ == '__main__':
    names = [
        'Roberto Brenes Mesen', 'Pedro Bull Narito', 'Maria Torres Alberatoe',
        'Luis Manual de la Torre', 'Hernan Derbez Pure', 'Eloisa Asofeifa Nuñez'
    ]
    start(".")