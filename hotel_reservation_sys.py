from pathlib import Path

from abstraction.Customer import Customer
# from abstraction.Hotel import Hotel
# from abstraction.Reservation import Reservation
from abstraction.AbstractionType import AbstractionType
from abstraction.Hotel import Hotel
from abstraction.Setting import Setting
from data_handling.JsonManager import JsonManager

def start(name):
    # print(JsonManager.get_path(AbstractionType.RESERVATION))
    # id = "f37d8661-0345-430a-b9b5-ddb758b83342"
    # c = Customer("Pepe Goteras y Black")
    h = Hotel("El Gran Peleé")

    is_saved = JsonManager.create_data(AbstractionType.HOTEL, h)

    # print(c.id)
    # c.id = id
    # print(c.id)
    # is_saved = JsonManager.create_data(c, "\\data_set\\customer\\")
    # is_saved = JsonManager.create_data(c, "\\data_set\\customer\\")
    #JsonManager.display_data("\\data_set\\customer\\")

    # print(Path(__file__))

    # file_folder = Path(__file__).parent.parent.resolve()
    #file_folder = Path(__file__).parent.parent.resolve()
    # c = Customer(name)
    #is_saved = JsonManager.create_data(c, "\\data_set\\customer\\")
    # is_saved = JsonManager.delete_data("\\data_set\\customer\\", '63f2387b-061b-4f9e-92b2-fa7e55aa012e')

    from pathlib import Path

    #if is_saved:
    #    print("Stored")
    #else:
    #    print("Not Stored :-(")

    # c.create() c.delete() c.display() c.modify()
    # h = Hotel(name) h.create() h.delete() h.display() h.modify() h.reserver_room() h.cancel_reservation()
    # r = Reservation(name) r.create() r.cancel()
    # print(name)

if __name__ == '__main__':
    start("")
    # start('Roberto Brenes Mesen')
    # start('Pedro Bull Narito')
    # start("Maria Torres Alberatoe")
    # start("Luis Manual de la Torre")
    # start("Hernan Derbez Pure")
    # start("Eloisa Asofeifa Nuñez")