from pathlib import Path
import json
# from colorama import init, Fore
# init(autoreset=True)

class JsonManager:

    @staticmethod
    def save_data(data, catalog_path):
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
