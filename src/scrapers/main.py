# ----- REQUIRED IMPORTS -----

import helper as he
import holds as ho

# ----- EXECUTION CODE -----

if __name__ == "__main__":
    LOG_FILEPATH = "./../generated_log/log.json"
    he.write_json(ho.scrape_atomik(), LOG_FILEPATH)
    he.write_json(ho.scrape_menagerie(), LOG_FILEPATH)
    he.write_json(ho.scrape_decoy(), LOG_FILEPATH)
