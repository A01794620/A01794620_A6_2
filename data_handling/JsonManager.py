from pathlib import Path
import json
import os

from abstraction.AbstractionType import AbstractionType
from abstraction.Customer import Customer
from abstraction.Setting import Setting

class JsonManager:

    @staticmethod
    def yield_json(data_type,data):

        src_data = {}

        if data_type == AbstractionType.CUSTOMER:
            src_data = {
                "id": data.id,
                "name": data.name,
                "lastname": data.name,
                "age": 30,
            }
        elif data_type == AbstractionType.HOTEL:
            src_data = {
                "id": data.id,
                "name": data.name,
            }
        elif data_type == AbstractionType.RESERVATION:
            pass
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
        print(full_path)
        src_data = JsonManager.yield_json(data_type, data)

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
    def delete_data(catalog_path, file_id):
        data_path = Path(__file__)
        full_path = str(data_path.parent.parent) + catalog_path + file_id + ".json"
        print(full_path)

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
        # print(full_path)

        json_files = list(full_path.glob('**/*' +  Setting.FILE_EXTENSION))

        for each_file in json_files:
            obj_line = None

            if data_type == AbstractionType.CUSTOMER:
                data_src = JsonManager.load_from_file(each_file)

                if isinstance(data_src, dict):
                    name = str(data_src['name'])
                    id = str(data_src['id'])
                    age = str(data_src['age'])
                    obj_line = Customer(name)
                    obj_line.id = id
                    obj_line.age = age
                    obj_container.append(obj_line)
                    #print(f"Name:={name} Id:={id} Age:={age}")
                else:
                    pass
            elif data_type == AbstractionType.HOTEL:
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

        name = ""
        id = ""
        age = 0
        obj_item = None

        if isinstance(data_src, dict):
            name = str(data_src['name'])
            id = str(data_src['id'])
            age = str(data_src['age'])
            obj_item = Customer(name)
            obj_item.id = id
            obj_item.age = age

        else:
            pass

        # print(data_src)
        # print(full_path)
        return obj_item

