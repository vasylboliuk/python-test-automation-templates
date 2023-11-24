import json as json_lib
import logging


LOGGER = logging.getLogger(__name__)


class DtoConverter:

    @staticmethod
    def string_to_pretty_json(str_value: str):
        """
        Convert String to pretty json output
        :param str_value: str as json
        :return: converted string or input data
        """
        result = str_value
        if DtoConverter.is_json(str_value):
            try:
                str_as_json = json_lib.loads(str_value)
                result = json_lib.dumps(str_as_json, indent=4)
            except ValueError as e:
                result = str_value
        return result

    @staticmethod
    def dict_to_pretty_json(input_dict: dict):
        """
        Convert dict to pretty json output
        :param input_dict: dict
        :return: converted string or input dict
        """
        return json_lib.dumps(input_dict, indent=4)


    @staticmethod
    def is_json(myjson: str):
        try:
            json_lib.loads(myjson)
        except ValueError as e:
            return False
        return True