# ----- REQUIRED IMPORTS -----

import os
import cv2
import sight as s
from nicegui import ui

# ----- HELPER FUNCTIONS -----


def load_images_from_folder(folder):
    """
    load all images from the specified folder
    """
    images = []
    for filename in os.listdir(folder):
        if filename.endswith(".jpeg") or filename.endswith(".jpg"):
            images.append(os.path.join(folder, filename))
    return images


def select_image(image_folder_path, image_output_filepath, json_output_filepath):
    """
    handle image selection
    """

    print(f"Selected image: {image_folder_path}")
    try:
        selection_tuple = s.hold_selection_wrapper(
            image_folder_path,
            image_output_filepath,
            json_output_filepath,
        )
        print(selection_tuple)
        if selection_tuple[0]:
            print("Success: Holds selected!")
            ui.notify("Success: Holds selected!")
            ui.run(close=True)
        else:
            print("Error: Unable to select holds.")
            ui.notify("Error: Unable to select holds.")
            ui.run(close=True)
    except Exception as e:
        print(f"Error: Unable to select holds: {e}")
        ui.notify(f"Error: Cannot select holds due to the error: {str(e)}")
        ui.run(close=True)


def nicegui_frontend_wrapper(
    image_folder_path, image_output_filepath, json_output_filepath
):
    """
    wrapper function to run the nicegui frontend
    """
    with ui.row():
        ui.label("Choose an image will ya").style(
            "font: 'Comic Sans MS'; font-size: 24px; font-weight: bold;"
        )
    for img in load_images_from_folder(image_folder_path):
        ui.button(
            img,
            on_click=lambda img=img: select_image(
                img, image_output_filepath, json_output_filepath
            ),
        )
    ui.run()


# ----- EXECUTION CODE -------

if __name__ in {"__main__", "__mp_main__"}:
    IMAGE_FOLDER_PATH = "./../corpus/clean/boards_images/"
    IMAGE_OUTPUT_FILEPATH = "./../corpus/clean/boards_images/"
    JSON_OUTPUT_FILEPATH = "./../generated_log/boards_contours_log.json"
    nicegui_frontend_wrapper(
        IMAGE_FOLDER_PATH, IMAGE_OUTPUT_FILEPATH, JSON_OUTPUT_FILEPATH
    )
