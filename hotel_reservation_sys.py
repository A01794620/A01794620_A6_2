from pathlib import Path

from abstraction.Customer import Customer
# from abstraction.Hotel import Hotel
# from abstraction.Reservation import Reservation
from data_handling.JsonManager import JsonManager

def start(name):
    c = Customer(name)
    # print(Path(__file__))




    # file_folder = Path(__file__).parent.parent.resolve()

    #file_folder = Path(__file__).parent.parent.resolve()
    is_saved = JsonManager.save_data(c, "\\data_set\\customer\\")
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
    start('Roberto Brenes Mesen')