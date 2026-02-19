from pathlib import Path
import json
import os

from abstraction.AbstractionType import AbstractionType
from abstraction.Customer import Customer
from abstraction.Hotel import Hotel
from abstraction.Setting import Setting

class JsonManager:

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
                "hotel_id": data.hotel_id,
                "room": data.room,
                "customer_id": data.customer_id,
                "date": data.date,
                "registration_date": data.registration_date,
            }

        else:
            pass

        return src_data

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
    def create_data(data_type, data):

        full_path = JsonManager.get_path(data_type) + data.id + Setting.FILE_EXTENSION
        src_data = JsonManager.yield_json(data_type, data)
        # print(src_data)
        # print(full_path)

        try:
            with open(full_path, "w") as json_file:
                json.dump(src_data, json_file, indent=4)
            return True
        except FileNotFoundError as FileNFE:
            print(FileNFE)
            return False
        except json.JSONDecodeError as JSONDE:
            print(JSONDE)
            return False

    @staticmethod
    def delete_data(data_type, file_id):
        full_path = JsonManager.get_path(data_type) + file_id + Setting.FILE_EXTENSION

        try:
            if os.path.exists(full_path):
                print("Removing " + full_path + " with no mercy.")
                os.remove(full_path)
            else:
                print("The file " + full_path + " does not exist.")
        except FileNotFoundError:
            print(f"Error: The file '{full_path}' does not exist.")
        except PermissionError:
            print(f"Error: Permission denied to delete the file '{full_path}'. Ensure the file is not open or read-only.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

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
            err_to_print = ("Error: Could not decode JSON from the file. " +
                            "Check for valid JSON syntax.")
            return data

    @staticmethod
    def display_data(data_type):

        obj_container = []
        obj_line = None
        full_path = Path(JsonManager.get_path(data_type))
        json_files = list(full_path.glob('**/*' +  Setting.FILE_EXTENSION))

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
                    id_= str(data_src['id'])
                    name = str(data_src['name'])
                    address = str(data_src['address'])
                    email = str(data_src['email'])
                    phone = str(data_src['phone'])

                    obj_line = Hotel(name, address, email, phone)
                    obj_line.id = id_
                    obj_container.append(obj_line)

                else:
                    pass
            elif data_type == AbstractionType.RESERVATION:

                pass

            else:
                pass

        return obj_container

    @staticmethod
    def retrieve_data(data_type, id_):

        full_path = JsonManager.get_path(data_type) + id_ + Setting.FILE_EXTENSION
        data_src = JsonManager.load_from_file(full_path)

        obj_item = None


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
                obj_item = Hotel(name, address,  email, phone)
                obj_item.id = id_

            else:
                pass

        else:
            pass

        return obj_item

    @staticmethod
    def has_data(data_type, file_id):
        full_path = JsonManager.get_path(data_type) + file_id + Setting.FILE_EXTENSION

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
