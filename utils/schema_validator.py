import json

from pathlib import Path

from jsonschema import validate


class SchemaValidator:

    @staticmethod
    def validate_schema(
            response_body,
            schema_path
    ):

        root_directory = Path(__file__).resolve().parent.parent

        full_schema_path = root_directory / schema_path

        with open(full_schema_path, "r") as schema_file:

            schema = json.load(schema_file)

        validate(
            instance=response_body,
            schema=schema
        )