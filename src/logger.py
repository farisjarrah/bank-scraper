import datetime
import logging
#import sqlite3

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
 
 # def log_json(entry_string):

#con = sqlite3.connect(cfg.settings["db_name"])
#def db_init():
#    try:
#        cur = con.cursor()
#        cur.execute("""CREATE TABLE IF NOT EXISTS balances(
#            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
#            bank TEXT,
#            balance REAL);""")
#        con.commit()
#    except:
#        logging.critical("Failed to initialize the db!")
#        con.rollback()
#        con.close()
#
#def check_if_table_exists(table_name):
#    cur = con.cursor()
#    if cur.execute(f"SELECT count(*) FROM sqlite_master WHERE type='table' and name=?;", table_name).fetchone()[0] == 1:
#        return True
#    else:
#        return False
