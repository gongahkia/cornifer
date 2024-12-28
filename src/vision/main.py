# ----- REQUIRED IMPORTS -----

import json
import sight as s
import helper as he

# ----- EXECUTION CODE -----

if __name__ == "__main__":
    ROOT_PATH = "./boards_images/"
    TEST_PATH_ARRAY = he.list_folder_files(ROOT_PATH)
    print(TEST_PATH_ARRAY)
    result_tuple = s.identify_contours(TEST_PATH_ARRAY, ROOT_PATH)
    if result_tuple[0]:
        print(result_tuple[1])
        FINAL = "./nice.json"
        with open(FINAL, "w") as f:
            json.dump(result_tuple[1], f, indent=4)
