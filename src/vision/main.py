# ----- REQUIRED IMPORTS -----

import sight as s
import helper as he

# ----- EXECUTION CODE -----

if __name__ == "__main__":
    ROOT_PATH = "./boards_images/"
    TEST_PATH_ARRAY = he.list_folder_files(ROOT_PATH)
    print(TEST_PATH_ARRAY)
    s.identify_contours(TEST_PATH_ARRAY, ROOT_PATH)
