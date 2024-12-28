import os
import json
import gzip


def unsafe_write_json(data, target_filepath):
    """
    indiscriminately writes dictionary data to a specified json file without checking
    """
    try:
        with open(target_filepath, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Success: Data successfully written to {target_filepath}")
        return True
    except:
        print(f"Error: Unable to write to {target_filepath}")
        return False


def unsafe_write_gzip(gzip_data, target_filepath):
    """
    indiscriminately writes gzip data to a gzip file without checking
    """
    try:
        with open(target_filepath, "wb") as f:
            f.write(gzip_data)
        print(f"Success: Data successfully written to {target_filepath}")
        return True
    except:
        print(f"Error: Unable to write to {target_filepath}")
        return False


def read_gzip(target_filepath):
    """
    reads gzip data from a gzip file
    """
    try:
        with open(target_filepath, "rb") as f:
            gzip_data = f.read()
        print(f"Success: Data successfully read from {target_filepath}")
        return (True, gzip_data)
    except:
        print(f"Error: Unable to read from {target_filepath}")
        return (False, None)


def list_folder_files(target_folderpath, file_extension=None):
    """
    list all files in the specified folder
    """
    if not os.path.isdir(target_folderpath):
        raise ValueError(
            f"Error: The specified path at {target_folderpath} is not a valid directory."
        )
    file_list = []
    for filename in os.listdir(target_folderpath):
        file_path = os.path.join(target_folderpath, filename)
        if os.path.isfile(file_path):
            if file_extension is None or filename.endswith(file_extension):
                file_list.append(file_path)
    return file_list


def compress_json(data):
    """
    compresses a JSON object using Gzip
    """
    try:
        json_str = json.dumps(data)
        compressed_data = gzip.compress(json_str.encode("utf-8"))
        print(f"Success: JSON successfully compressed")
        return (True, compressed_data)
    except Exception as e:
        print(f"Error: Unable to compress JSON: {e}")
        return (False, None)


def decompress_gzip(compressed_data):
    """
    decompresses Gzip-compressed JSON data back into a JSON object
    """
    try:
        json_str = gzip.decompress(compressed_data).decode("utf-8")
        data = json.loads(json_str)
        return (True, data)
    except Exception as e:
        print(f"Error: Unable to decompress JSON: {e}")
        return (False, None)
