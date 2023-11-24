import io
import json
from pathlib import Path
import logging
import yaml


class FileUtil:

    @staticmethod
    def get_project_root():
        return Path(__file__).absolute().parent.parent.parent

    @staticmethod
    def read_file_as_string(file_path):
        logging.info("Read file from path: [{}]".format(file_path))
        file = io.open(str(file_path), mode="r", encoding="utf-8")
        line = file.read()
        file.close()
        return line

    @staticmethod
    def read_yaml_file(file_path):
        with open(file_path, 'r') as f:
            file_data = yaml.safe_load(f.read())
        return file_data

    @staticmethod
    def read_json_file(file_path):
        with open(file_path, 'r') as f:
            file_data = json.loads(f.read())
        return file_data

