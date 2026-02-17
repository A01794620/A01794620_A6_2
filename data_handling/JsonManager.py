from pathlib import Path
import json
import os

# from colorama import init, Fore
# init(autoreset=True)

class JsonManager:

    @staticmethod
    def create_data(data, catalog_path):
        data_path = Path(__file__)
        full_path = str(data_path.parent.parent) + catalog_path + data.id + ".json"
        print(full_path)
        data = {
            "id": data.id,
            "name": data.name,
            "lastname": data.name,
            "age": 30,
        }

        try:

            with open(full_path, "w") as json_file:
                json.dump(data, json_file, indent=4)
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
    def display_data(catalog_path):
        data_path = Path(__file__)
        full_path = Path(str(data_path.parent.parent) + catalog_path)
        json_files = list(full_path.glob('**/*.json'))
        for each_file in json_files:
            customer_src = JsonManager.load_from_file(each_file)
            name = str(customer_src['name'])
            id = str(customer_src['id'])
            age = str(customer_src['age'])
            print(f"Name:={name} Id:={id} Age:={age}")




