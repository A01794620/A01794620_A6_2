from pathlib import Path
import json
import os
from abstraction.AbstractionType import AbstractionType
from abstraction.Customer import Customer
from abstraction.Hotel import Hotel
from abstraction.Reservation import Reservation
from setting.Setting import Setting
from consolemenu import PromptUtils
from consolemenu.screen import Screen
from prompt_toolkit import prompt

class JsonManager:
    @staticmethod
    def is_valid_path(file_path):

        if file_path is None:
            return False

        if str(file_path).strip() == "":
            return False
        else:
            return Path(file_path).is_dir()

    @staticmethod
    def is_valid_json(src_json):

        if Setting.NULL_VALUE in str(src_json):
            return False

        try:
            json.dumps(src_json)
            return True
        except json.JSONDecodeError:
            return False

    @staticmethod
    def get_path(data_type):
        catalog_path = ""

        if data_type == AbstractionType.CUSTOMER:
            catalog_path =  Setting.SEP_PATH + Setting.DATA_PATH + Setting.SEP_PATH + Setting.CUSTOMER_PATH + Setting.SEP_PATH
        elif data_type == AbstractionType.HOTEL:
            catalog_path = Setting.SEP_PATH + Setting.DATA_PATH + Setting.SEP_PATH + Setting.HOTEL_PATH + Setting.SEP_PATH
        elif data_type == AbstractionType.RESERVATION:
            catalog_path = Setting.SEP_PATH + Setting.DATA_PATH + Setting.SEP_PATH + Setting.RESERVATION_PATH + Setting.SEP_PATH
        else:
            pass

        parent_path = Path(__file__)
        full_path = str(parent_path.parent.parent) + catalog_path

        if catalog_path!="":
            return full_path
        else:
            return catalog_path

    @staticmethod
    def yield_json(data_type,data):

        src_data = {}

        if data_type == AbstractionType.CUSTOMER:
            src_data = {
                "id": data.id,
                "fullname": data.fullname,
                "email": data.email,
                "phone": data.phone
            }
        elif data_type == AbstractionType.HOTEL:
            src_data = {
                "id": data.id,
                "name": data.name,
                "address": data.address,
                "email": data.email,
                "phone": data.phone
            }
        elif data_type == AbstractionType.RESERVATION:
            src_data = {
                "id": data.id,
                "customer_id": data.customer_id,
                "hotel_id": data.hotel_id,
                "room": data.room,
                "adults_number": data.adults_number,
                "children_number": data.children_number,
                "date": data.date,
                "registration_date": data.registration_date,
            }
        else:
            src_data = {"null": Setting.NULL_VALUE}
            pass

        return src_data

    @staticmethod
    def has_data(data_type, file_id):
        full_path = JsonManager.get_path(data_type) + file_id + Setting.FILE_EXTENSION

        # print(full_path)

        try:
            if os.path.exists(full_path):
                return True
            else:
                return False
        except FileNotFoundError:
            print(f"Error: The file '{full_path}' does not exist.")
            return False
        except PermissionError:
            print(
                f"Error: Permission denied to delete the file '{full_path}'. Ensure the file is not open or read-only.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False


    @staticmethod
    def create_data(data_type, data):
        full_path = JsonManager.get_path(data_type) + data.id + Setting.FILE_EXTENSION
        src_data = JsonManager.yield_json(data_type, data)

        # print("-----------------------")
        # print(full_path)
        # print("-----------------------")

        if Setting.NULL_VALUE in str(src_data):
            return False

        try:
            with open(full_path, "w") as json_file:
                json.dump(src_data, json_file, indent=4)

            return True
        except FileNotFoundError as FileNFE:
            print(FileNFE)
            return False
        except json.JSONDecodeError as JSONMODEL:
            print(JSONMODEL)
            return False

    @staticmethod
    def load_from_file(file_path):
        data = ""
        err_to_print = ""

        try:
            with open(file_path, 'r', encoding="utf-8") as file:
                data = json.load(file)

            return data

        except FileNotFoundError:
            err_to_print = f"File was not found:= {file_path}."
            return data
        except json.JSONDecodeError:
            err_to_print = ("Error: Could not decode JSON from the file.\n" +
                            "Check for valid JSON syntax.")
            return data

    @staticmethod
    def retrieve_data(data_type, id_):

        full_path = JsonManager.get_path(data_type) + id_ + Setting.FILE_EXTENSION
        obj_item = None
        data_src = ""

        # print(full_path)

        if JsonManager.has_data(data_type, id_):
            data_src = JsonManager.load_from_file(full_path)

        if data_src != "":
            if isinstance(data_src, dict):
                if data_type == AbstractionType.CUSTOMER:
                    full_name = str(data_src['fullname'])
                    id_ = str(data_src['id'])
                    email = str(data_src['email'])
                    phone = str(data_src['phone'])

                    obj_item = Customer(full_name, email, phone)
                    obj_item.id = id_
                elif data_type == AbstractionType.HOTEL:
                    id_ = str(data_src['id'])
                    name = str(data_src['name'])
                    address = str(data_src['address'])
                    email = str(data_src['email'])
                    phone = str(data_src['phone'])
                    obj_item = Hotel(name, address, email, phone)
                    obj_item.id = id_
                else:
                    pass
            else:
                pass
        else:
            # File is empty, removed or not found
            pass

        return obj_item

    @staticmethod
    def display_data(data_type):

        pu = PromptUtils(Screen())
        pu.clear()


        obj_container = []
        obj_line = None
        full_path = Path(JsonManager.get_path(data_type))
        json_files = list(full_path.glob('**/*' + Setting.FILE_EXTENSION))


        for each_file in json_files:
            obj_line = None

            if data_type == AbstractionType.CUSTOMER:

                data_src = JsonManager.load_from_file(each_file)

                if isinstance(data_src, dict):
                    id_ = str(data_src['id'])
                    full_name = str(data_src['fullname'])
                    email = str(data_src['email'])
                    phone = str(data_src['phone'])
                    obj_line = Customer(full_name, email, phone)
                    obj_line.id = id_
                    obj_container.append(obj_line)
                else:
                    pass
            elif data_type == AbstractionType.HOTEL:

                data_src = JsonManager.load_from_file(each_file)

                if isinstance(data_src, dict):
                    id_ = str(data_src['id'])
                    name = str(data_src['name'])
                    address = str(data_src['address'])
                    email = str(data_src['email'])
                    phone = str(data_src['phone'])

                    obj_line = Hotel(name, address, email, phone)
                    obj_line.id = id_
                    obj_container.append(obj_line)

            elif data_type == AbstractionType.RESERVATION:

                data_src = JsonManager.load_from_file(each_file)

                if isinstance(data_src, dict):

                    id_ = str(data_src['id'])
                    customer_id = str(data_src['customer_id'])
                    hotel_id = str(data_src['hotel_id'])
                    room = str(data_src['room'])
                    adults_number = str(data_src['adults_number'])
                    children_number = str(data_src['children_number'])
                    date = str(data_src['date'])
                    registration_date = str(data_src['registration_date'])

                    # print(f"id {id_}")
                    # print(f"hotel_id {hotel_id}")
                    # print(f"customer_id {customer_id}")
                    # print(f"room {room}")
                    # print(f"adults_number {adults_number}")
                    # print(f"children_number {children_number}")
                    # print(f"date {date}")
                    # print(f"registration_date {registration_date}")


                    obj_line = Reservation(hotel_id, customer_id, room, int(adults_number), int(children_number), date)
                    # pu.enter_to_continue()

                    obj_line.id = id_
                    obj_container.append(obj_line)
                else:
                    pass
            else:
                pass

        return obj_container

    @staticmethod
    def delete_data(data_type, file_id):
        full_path = JsonManager.get_path(data_type) + file_id + Setting.FILE_EXTENSION
        try:
            if os.path.exists(full_path):
                os.remove(full_path)
                return True
            else:
                #print("The file " + full_path + " does not exist.")
                return False
        except FileNotFoundError:
            print(f"Error: The file '{full_path}' does not exist.")
            return False
        except PermissionError:
            print(f"Error: Permission denied to delete the file '{full_path}'.\nEnsure the file is not open or read-only.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False