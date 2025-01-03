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


def read_json(target_filepath):
    """
    safely load data from a JSON file
    """
    try:
        with open(target_filepath, "r") as f:
            data = json.load(f)
        print(f"Success: JSON file at {target_filepath} succesfully read")
        return (True, data)
    except FileNotFoundError:
        print("Error: The file was not found")
        return (False, None)
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON")
        return (False, None)
    except Exception as e:
        print(f"Error: Unable to read from {target_filepath}: {e}")
        return (False, None)


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


def json_to_gzip_wrapper(json_data, gzip_output_filepath):
    """
    wrapper function to compress a json to a gzip and write it
    """
    try:
        compression_tuple = compress_json(json_data)
        if compression_tuple[0]:
            unsafe_write_gzip(compression_tuple[1], gzip_output_filepath)
            print("Success: JSON successfully compressed")
            return True
        else:
            print("Error: Unable to compress JSON")
            return False
    except Exception as e:
        print(f"Error: Unable to compress JSON: {e}")
        return False


def gzip_to_json_wrapper(json_output_filepath, gzip_output_filepath):
    """
    wrapper function to decompress a gzip to a json and write it
    """
    try:
        read_gzip_tuple = read_gzip(gzip_output_filepath)
        if read_gzip_tuple[0]:
            decompression_tuple = decompress_gzip(read_gzip_tuple[1])
            if decompression_tuple[0]:
                unsafe_write_json(decompression_tuple[1], json_output_filepath)
                print("Success: JSON successfully decompressed")
                return True
            else:
                print("Error: Unable to decompress JSON")
                return False
    except Exception as e:
        print(f"Error: Unable to decompress JSON: {e}")
        return False
