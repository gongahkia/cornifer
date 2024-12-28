# ----- REQUIRED IMPORTS -----

import sight as s
import helper as he
import frontend as f

# ----- EXECUTION CODE -----

if __name__ in {"__main__", "__mp_main__"}:
    IMAGE_INPUT_FILEPATH = "./../corpus/raw/boards_images/"
    IMAGE_OUTPUT_FILEPATH = "./../corpus/clean/boards_images/"
    JSON_OUTPUT_FILEPATH = "./../generated_log/boards_contours_log.json"
    GZIP_OUTPUT_FILEPATH = "./../generated_log/boards_contours_log.gz"

    # result_tuple = s.identify_contours(
    #     he.list_folder_files(IMAGE_INPUT_FILEPATH, ".jpeg"),
    #     IMAGE_INPUT_FILEPATH,
    #     IMAGE_OUTPUT_FILEPATH,
    # )

    # if result_tuple[0]:
    #     print(result_tuple[1])
    # he.json_to_gzip_wrapper(result_tuple[1], GZIP_OUTPUT_FILEPATH)
    # he.gzip_to_json_wrapper(JSON_OUTPUT_FILEPATH, GZIP_OUTPUT_FILEPATH)

    # selection_tuple = s.hold_selection_wrapper(
    #     "./../corpus/clean/boards_images/35301306400930.jpeg",
    #     IMAGE_OUTPUT_FILEPATH,
    #     JSON_OUTPUT_FILEPATH,
    # )

    f.nicegui_frontend_wrapper(IMAGE_OUTPUT_FILEPATH, JSON_OUTPUT_FILEPATH)
