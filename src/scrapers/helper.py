import os
import json
import hmac
import hashlib
import base64
import urllib.request
from cryptography.fernet import Fernet


def file_exists(target_filepath):
    """
    checks whether a file exists at the specified file path
    """
    return os.path.isfile(target_filepath)


def delete_file(target_filepath):
    """
    deletes the file at the given filepath if it exists
    """
    if file_exists(target_filepath):
        os.remove(target_filepath)
        print(f"Success: File at filepath {target_filepath} deleted successfully.")
        return True
    else:
        print(f"Error: File at filepath {target_filepath}' does not exist.")
        return False


def load_json(target_filepath):
    """
    load json data from a specified file to a dictionary
    """
    try:
        with open(target_filepath, "r") as file:
            data = json.load(file)
        print(f"Success: JSON file at {target_filepath} succesfully read")
        return (True, data)
    except FileNotFoundError:
        print("Error: The file was not found")
        return (False, None)
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON")
        return (False, None)


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


def generate_fernet_key(salt_phrase):
    """
    generates a fernet key from the given salt phrase
    """
    key = hashlib.sha256(salt_phrase.encode()).digest()
    encoded_key = base64.urlsafe_b64encode(key).decode("utf-8")
    return encoded_key


def encrypt_json(target_filepath, salt_phrase):
    """
    encrypts a json file using fernet encryption
    """
    try:
        with open(target_filepath, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {target_filepath}")
    key = generate_fernet_key(salt_phrase)
    f = Fernet(key)
    encrypted_data = f.encrypt(json.dumps(data).encode())
    encrypted_filepath = target_filepath + ".enc"
    with open(encrypted_filepath, "wb") as f:
        f.write(encrypted_data)
    return encrypted_filepath


def decrypt_json(target_filepath, salt_phrase):
    """
    decrypts a json file using fernet encryption
    """
    try:
        modified_target_filepath = f"{target_filepath}.enc"
        with open(modified_target_filepath, "rb") as f:
            encrypted_data = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(
            f"ValueError: File not found: {modified_target_filepath}"
        )
    key = generate_fernet_key(salt_phrase)
    f = Fernet(key)
    try:
        decrypted_data = f.decrypt(encrypted_data)
    except cryptography.fernet.InvalidSignature as e:
        raise ValueError(f"ValueError: Decryption failed: Invalid signature ({e})")
    with open(target_filepath, "w") as f:
        json.dump(json.loads(decrypted_data.decode()), f, indent=4)
    return target_filepath


def download_image(image_url, target_filepath):
    """
    downloads an image from the specified url and saves it to the specified file path
    """
    try:
        directory = os.path.dirname(target_filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)
        urllib.request.urlretrieve(image_url, target_filepath)
        print(f"Success: Image downloaded successfully and saved to {target_filepath}")
    except Exception as e:
        print(f"Error: Unable to download image: {e}")


def download_board_images_wrapper(boards_image_filepath, boards_log_filepath):
    """
    downloads all board images from json file
    """
    try:
        board_map_tuple = load_json(boards_log_filepath)
        if board_map_tuple[0]:
            board_map = board_map_tuple[1]
            [
                download_image(
                    board["image_source"],
                    f"{boards_image_filepath}{board['image_id'].strip().replace(' ', '_')}.jpeg",
                )
                for board_array in board_map.values()
                for board in board_array
            ]
            print("Success: Downloaded all board images")
            return True
    except:
        print("Error: Unable to download all board images")
        return False


def download_holds_images_wrapper(holds_image_filepath, holds_log_filepath):
    """
    downloads all hold images from json file
    """
    try:
        hold_map_tuple = load_json(holds_log_filepath)
        if hold_map_tuple[0]:
            hold_map = hold_map_tuple[1]
            [
                download_image(
                    hold["image_source"],
                    f"{holds_image_filepath}{hold['image_id'].strip().replace(' ', '_')}.jpeg",
                )
                for hold_array in hold_map.values()
                for hold in hold_array
            ]
            print("Success: Downloaded all hold images")
            return True
    except:
        print("Error: Unable to download all hold images")
        return False
