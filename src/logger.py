import datetime
import logging

import config as cfg

logging.basicConfig(filename=cfg.settings["program_log"], encoding='utf-8', level=cfg.settings["log_level"], format='%(asctime)s - %(levelname)s - %(message)s')

def generate_date_stamp():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%dT%H:%M:%S.%S')

def log_csv(entry_string):
    datestamp = generate_date_stamp()
    # entry string should just be: <bankName>,<accountID>,<balance>
    # adding balances to csv: <date>,<bankName>,<accountID>,<balance>\n
    balances_csv=open(cfg.settings["log_file"], "a")  # append only to log file
    balances_csv.write(f"{datestamp},{entry_string}\n")
    balances_csv.close()
    logging.info(f"generated entry string for csv: {entry_string}")