import json

from pathlib import Path


class JsonReader:

    @staticmethod
    def read_json_file(file_path):

        root_directory = Path(__file__).resolve().parent.parent

        full_path = root_directory / file_path

        with open(full_path, "r") as json_file:

            return json.load(json_file)