import os
import json


def file_exists(target_filepath):
    """
    checks whether a file exists at the specified file path
    """
    return os.path.isfile(target_filepath)


def write_json(data, target_filepath):
    """
    writes or appends dictionary data to a specified json file
    """
    try:
        if file_exists(target_filepath):
            with open(target_filepath, "r") as f:
                existing_data = json.load(f)
            existing_data.update(data)
            data = existing_data
        with open(target_filepath, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Success: Data successfully written to {target_filepath}")
        return True
    except Exception as e:
        print(f"Error: Unable to write to {target_filepath}: {e}")
        return False
