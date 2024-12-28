# ----- REQUIRED IMPORTS -----

import helper as he
import holds as ho
import boards as bo

# ----- EXECUTION CODE -----

if __name__ == "__main__":
    ENCRYPTION_SALT = "bouldering"
    HOLDS_LOG_FILEPATH = "./../generated_log/holds_log.json"
    BOARDS_LOG_FILEPATH = "./../generated_log/boards_log.json"
    HOLDS_IMAGE_FILEPATH = "./../corpus/raw/holds_images/"
    BOARDS_IMAGE_FILEPATH = "./../corpus/raw/boards_images/"

    # he.delete_file(HOLDS_LOG_FILEPATH)
    # he.delete_file(BOARDS_LOG_FILEPATH)

    # ho.scrape_holds_wrapper(HOLDS_LOG_FILEPATH)
    # bo.scrape_boards_wrapper(BOARDS_LOG_FILEPATH)

    # he.encrypt_json(HOLDS_LOG_FILEPATH, ENCRYPTION_SALT)
    # he.encrypt_json(BOARDS_LOG_FILEPATH, ENCRYPTION_SALT)

    he.download_holds_images_wrapper(HOLDS_IMAGE_FILEPATH, HOLDS_LOG_FILEPATH)
    he.download_board_images_wrapper(BOARDS_IMAGE_FILEPATH, BOARDS_LOG_FILEPATH)

    # he.decrypt_json(HOLDS_LOG_FILEPATH, ENCRYPTION_SALT)
    # he.decrypt_json(BOARDS_LOG_FILEPATH, ENCRYPTION_SALT)
