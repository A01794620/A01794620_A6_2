"""
 Module. AbstractionType. Exercise of Programming 3 and Unity Testing 6.2
 @Motive . Unity Testing
           Code Coverage Evaluation
           PEP8 check with Pylint and Flake8
 @author . Ronald Sandí Quesada
 @Student-ID . A01794620
 @email . A01794620@tec.mx
 @MNA Class . Pruebas de Software y Aseguramiento de la Calidad (TC4017)
 @Professor . PhD Gerardo Padilla Zárate
 @Professor Evaluator and Tutor . PhD Daniel Flores Araiza
 @Period . I Trimester 2026
 @Date: 22 February 2026
"""
import os
import json
from pathlib import Path
from consolemenu import PromptUtils
from consolemenu.screen import Screen
# Local system imports
from setting.Setting import Setting
from abstraction.Hotel import Hotel
from abstraction.Customer import Customer
from abstraction.Reservation import Reservation
from abstraction.AbstractionType import AbstractionType


class JsonManager:
    """
    JsonManager:
    This is the most relevant class for file persistence usage.
    The format of the files are defined in JSON, and in plain UTF8 encoding.
    """

    @staticmethod
    def is_valid_path(file_path):
        """
        It is a generic process of a quantity check to use it as placeholder
        for other quantities checks.
        Args:
            file_path (str): string to be checked.
        Returns:
            bool: evaluates a potential path string.
                  It might be a valid directory in the
                  underline OS file table system.
        """
        if file_path is None:
            return False

        if str(file_path).strip() == "":
            return False

        return Path(file_path).is_dir()

    @staticmethod
    def is_valid_json(src_json):
        """
        Evaluates either a string is or not a valid JSON formed source.
                  The string to be checked	Boolen
        Args:
            src_json (str): string to be checked.
        Returns:
            bool: result of checking the syntactical
                  string structure.
        """
        if Setting.NULL_VALUE in str(src_json):
            return False

        try:
            json.dumps(src_json)
            return True
        except json.JSONDecodeError:
            return False

    @staticmethod
    def get_path(data_type):
        """
        This is a catalyzer of paths as per each essential entity
        in the system. Every entity holds one folder to avoid
        collisions.

        Args:
            data_type (enum): enum item coming from AbstractionTypeClass
            in the abstraction package.
        Returns:
            bool:returns the valid path for a specific artifact in the
            system.
        """
        catalog_path = ""

        if data_type == AbstractionType.CUSTOMER:
            catalog_path = (Setting.SEP_PATH + Setting.DATA_PATH +
                            Setting.SEP_PATH + Setting.CUSTOMER_PATH +
                            Setting.SEP_PATH)
        elif data_type == AbstractionType.HOTEL:
            catalog_path = (Setting.SEP_PATH + Setting.DATA_PATH +
                            Setting.SEP_PATH + Setting.HOTEL_PATH +
                            Setting.SEP_PATH)
        elif data_type == AbstractionType.RESERVATION:
            catalog_path = (Setting.SEP_PATH + Setting.DATA_PATH +
                            Setting.SEP_PATH + Setting.RESERVATION_PATH +
                            Setting.SEP_PATH)
        else:
            pass

        parent_path = Path(__file__)
        full_path = str(parent_path.parent.parent) + catalog_path

        if catalog_path != "":
            return full_path

        return catalog_path

    @staticmethod
    def yield_json(data_type, data):
        """
        JSON factory of source string.
        It is based on the entity type defined in abstaction.AbastractionType
        Args:
            data_type (enum): enum item coming from AbstractionTypeClass in the
                              abstraction package.
            data(object): object of the kind, holding the raw material from
                          where a JSON serialization will be built.
        Returns:
            dict: JSON serialization built, which might be valid format per
            each-kind-of-en.
        """
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

        return src_data

    @staticmethod
    def has_data(data_type, file_id):
        """
        This is a prevention check to make sure that a path actually represents
        a real file in the persistence drive.

        Args:
            data_type (enum): enum item coming from AbstractionTypeClass in the
             abstraction package.
            file_id (str): unique artifact in the system ID having UUID-4
            structure.
        Returns:
            bool: Boolean check to consider the file as exiting in the
                  persistence drive. This can be considerate as a next
                  check level, not a syntactical
             check.
        """
        full_path = (JsonManager.get_path(data_type) + file_id +
                     Setting.FILE_EXTENSION)
        try:
            return os.path.exists(full_path)
            # if os.path.exists(full_path):
            #     return True
            # else:
            #     return False
        except FileNotFoundError:
            print(f"Error: The file '{full_path}' does not exist.")
            return False
        except PermissionError:
            print(
                f"Error: Permission denied to delete the file '{full_path}'. "
                "Ensure the file is not open or read-only.")
            return False
        # except Exception as e:
        #     print(f"An unexpected error occurred: {e}")
        #     return False

    @staticmethod
    def create_data(data_type, data):
        """
        This is a factory for artifacts of the system creation,
        it is the most bordering part of the system interfacing
        with the static persistence layer.
        Args:
            data_type (enum): enum item coming from AbstractionTypeClass in the
            abstraction package.
            data (str): the actual JSON data formatted to be stored in the
                        final end file.
        Returns:
            bool: It actually has a Boolean flag marking or not the
                  artifact creation.
        """
        full_path = (JsonManager.get_path(data_type) + data.id +
                     Setting.FILE_EXTENSION)

        src_data = JsonManager.yield_json(data_type, data)

        if Setting.NULL_VALUE in str(src_data):
            return False

        try:
            with open(full_path, "w", encoding="utf-8") as json_file:
                json.dump(src_data, json_file, indent=4)

            return True
        except FileNotFoundError as file_not_f:
            print(file_not_f)
            return False
        except json.JSONDecodeError as json_model_err:
            print(json_model_err)
            return False

    @staticmethod
    def load_from_file(file_path):
        """
        It extracts an artifact JSON file in the static persistence layer.
        It is the most boundary frontier regarding reading data on the system.
        Args:
            file_path (str): the exact OS path from where information will
            be read.
        Returns:
            str: It actually has a string  containing the artifact data,
                 on where empty data means that the file reding was not
                 fruitful.
        """
        data = ""
        # err_to_print = ""

        try:
            with open(file_path, 'r', encoding="utf-8") as file:
                data = json.load(file)

            return data

        except FileNotFoundError:
            err_to_print = f"File was not found:= {file_path}."
            print(err_to_print)
            return data
        except json.JSONDecodeError:
            err_to_print = ("Error: Could not decode JSON from the file.\n" +
                            "Check for valid JSON syntax.")
            print(err_to_print)
            return data

    @staticmethod
    def retrieve_data(data_type, id_):
        """
        It is the interpretation of the raw JSON data into the system
        native objects.
        It is a translator from system base files to real objects
        that the system can use for communicate in between processes.

        Args:
            data_type (enum): enum item coming from AbstractionTypeClass
            in the abstraction package.

            id_ (st): unique UUID-4 for the artifact, circumscribe
             in the datatype of the kind of the first argument.
        Returns:
            object: object that represents the artifact in the system.
        """
        full_path = (JsonManager.get_path(data_type) + id_ +
                     Setting.FILE_EXTENSION)
        obj_item = None
        data_src = ""

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

    # pylint: disable=R0914
    @staticmethod
    def display_data(data_type):
        """
        This class is a consumer of load_from_files, since it reaches
        every artifact in batch and interpret them into helpful data
        structures objects to be digested by the system user interface.
        Args:
            data_type (enum): enum item coming from AbstractionTypeClass
             in the abstraction package.
            id_ (str): unique UUID-4 for the artifact, circumscribe in
                       the datatype of the kind of the first argument.
        Returns:
            object[]: array of objects of the kind of artifact that
                      represents objects that the system can handle.
        """
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
                    # registration_date = str(data_src['registration_date'])
                    obj_line = Reservation(hotel_id, customer_id, room,
                                           int(adults_number),
                                           int(children_number), date)
                    obj_line.id = id_
                    obj_container.append(obj_line)
                else:
                    pass
            else:
                pass

        return obj_container

    @staticmethod
    def delete_data(data_type, file_id):
        """
        This is an eraser of the system on those circumstances where
        is needed the system.
        By using it, system can disappear individual artifacts.
        Args:
            data_type (enum): enum item coming from AbstractionTypeClass
                              in the abstraction package.
            file_id (str): unique UUID-4 for the artifact, circumscribe
                           in the datatype of the kind of the first argument.
        Returns:
            object[]: flag indicating success or not deletion.

        """
        full_path = (JsonManager.get_path(data_type) + file_id +
                     Setting.FILE_EXTENSION)
        try:
            if os.path.exists(full_path):
                os.remove(full_path)
                return True

            return False
        except FileNotFoundError:
            print(f"Error: The file '{full_path}' does not exist.")
            return False
        except PermissionError:
            print(f"Error: Permission denied to delete the file"
                  f" '{full_path}'.\n"
                  f"Ensure the file is not open or read-only.")
            return False
        # except Exception as e:
        #     print(f"An unexpected error occurred: {e}")
        #     return False
