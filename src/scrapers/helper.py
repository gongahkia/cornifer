import os
import json
import hashlib
import hmac
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


def encrypt_json(target_filepath, salt_phrase):
    """
    encrypts a json file using fernet encryption
    """
    try:
        with open(target_filepath, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {target_filepath}")
    key = hashlib.sha256(salt_phrase.encode()).digest()
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
        with open(target_filepath, "rb") as f:
            encrypted_data = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File not found: {target_filepath}")
    key = hashlib.sha256(salt_phrase.encode()).digest()
    f = Fernet(key)
    try:
        decrypted_data = f.decrypt(encrypted_data)
    except Exception as e:
        raise ValueError(f"Error: Decryption failed: {e}")
    decrypted_filepath = target_filepath[:-4]
    with open(decrypted_filepath, "w") as f:
        json.dump(json.loads(decrypted_data.decode()), f, indent=4)
    return decrypted_filepath
