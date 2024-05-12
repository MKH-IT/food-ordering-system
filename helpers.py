import json


def read_json(file_path) -> dict | list:
    with open(file_path, 'r') as file:
        return json.load(file)
