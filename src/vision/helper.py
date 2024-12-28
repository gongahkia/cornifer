import os


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
