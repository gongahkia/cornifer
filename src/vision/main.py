# ----- REQUIRED IMPORTS -----

import sight as s
import helper as he

# ----- EXECUTION CODE -----

if __name__ == "__main__":
    IMAGE_INPUT_FILEPATH = "./../corpus/raw/boards_images/"
    IMAGE_OUTPUT_FILEPATH = "./../corpus/clean/boards_images/"
    JSON_OUTPUT_FILEPATH = "./../generated_log/boards_contours_log.json"
    GZIP_OUTPUT_FILEPATH = "./../generated_log/boards_contours_log.gz"

    result_tuple = s.identify_contours(
        he.list_folder_files(IMAGE_INPUT_FILEPATH, ".jpeg"),
        IMAGE_INPUT_FILEPATH,
        IMAGE_OUTPUT_FILEPATH,
    )

    if result_tuple[0]:
        print(result_tuple[1])
    he.json_to_gzip_wrapper(result_tuple[1], GZIP_OUTPUT_FILEPATH)
    he.gzip_to_json_wrapper(JSON_OUTPUT_FILEPATH, GZIP_OUTPUT_FILEPATH)

    selection_tuple = s.hold_selection_wrapper(
        "./../corpus/clean/boards_images/32115929874594.jpeg",
        IMAGE_OUTPUT_FILEPATH,
        JSON_OUTPUT_FILEPATH,
    )
