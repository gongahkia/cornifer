# ----- REQUIRED IMPORTS -----

import helper as he
import holds as ho

# ----- EXECUTION CODE -----

if __name__ == "__main__":
    LOG_FILEPATH = "./../generated_log/log.json"
    he.delete_file(LOG_FILEPATH)
    he.scrape_holds_wrapper(LOG_FILEPATH)
    he.encrypt_json(LOG_FILEPATH, "bouldering")
    # he.decrypt_json(LOG_FILEPATH, "bouldering")
