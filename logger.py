import logging

import config as cfg

def log_csv(entry_string):
    # adding balances to csv: <date>,<bankName>,<accountID>,<balance>\n
    balances_csv=open(cfg.settings["log_file"], "a")  # append only to log file
    balances_csv.write(entry_string)
    balances_csv.close()
    logging.info(f"generated entry string for csv: {entry_string}")

#def log_json():