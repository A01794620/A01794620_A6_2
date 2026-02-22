import uuid
# This is the only valid factory to generate and to
# validate IDs
class UuidHandler(object):
    @staticmethod
    def is_valid_id(uuid_):
        try:
            uuid_obj = uuid.UUID(uuid_, version=4)
        except ValueError:
            return False

        return str(uuid_obj) == uuid_

    @staticmethod
    def get_next_id():
        return str(uuid.uuid4())
