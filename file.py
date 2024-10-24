import json
from textwrap import indent


def func_write_to_json(json_file_name: str, json_dict: dict):
    with open(json_file_name, "w") as f:
        json.dump(json_dict, f, indent=4)

def func_write_to_file(file_name: str, msg:str, mode: str = "w"):
    with open(file_name, mode) as f:
        f.write(msg)