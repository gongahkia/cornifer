# ----- REQUIRED IMPORTS -----

import json
import sight as s
import helper as he

# ----- EXECUTION CODE -----

if __name__ == "__main__":
    IMAGE_INPUT_FILEPATH = "./../corpus/raw/boards_images/"
    IMAGE_OUTPUT_FILEPATH = "./../corpus/clean/boards_images/"
    JSON_OUTPUT_FILEPATH = "./../corpus/clean/boards_images/boards_hold_contours.json"
    GZIP_OUTPUT_FILEPATH = "./../corpus/clean/boards_images/boards_hold_contours.gz"

    result_tuple = s.identify_contours(
        he.list_folder_files(IMAGE_INPUT_FILEPATH),
        IMAGE_INPUT_FILEPATH,
        IMAGE_OUTPUT_FILEPATH,
    )

    if result_tuple[0]:
        print(result_tuple[1])
        compression_tuple = he.compress_json(result_tuple[1])
        if compression_tuple[0]:
            he.unsafe_write_gzip(compression_tuple[1], GZIP_OUTPUT_FILEPATH)
        decompression_tuple = he.decompress_gzip(he.read_gzip(GZIP_OUTPUT_FILEPATH))
        if decompression_tuple[0]:
            he.write_json(decompression_tuple[1], JSON_OUTPUT_FILEPATH)

    # s.hold_selection_wrapper("./identified/32115929874594.jpeg")
