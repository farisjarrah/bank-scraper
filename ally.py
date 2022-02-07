import time
import logging

import pyautogui
import pyperclip

import debugSafety
import datestamp
import browsers
import pwmanager
import logger
import excell
import config as cfg

###
### Ally Bank
###
## This is the main ally bank run. It gathers ally bank account entry data and output it as a csv for the logger: datestamp,ally,<account identifier>,$<account balance>
def ally_run():
    browsers.open_new_tab()
    login_ally()
    get_ally_balances_raw()
    excell.open_new_excell_online_book()
    paste_and_clean_ally_acct_data()
    # get account data and append it to the log
    logger.log_csv(construct_individual_ally_acct_balance(datestamp.generate_date_stamp(), "ally", "A2", "A3", "B2"))
    logger.log_csv(construct_individual_ally_acct_balance(datestamp.generate_date_stamp(), "ally", "A6", "A7", "B6"))
    browsers.close_tab() # close excel online tab
    browsers.close_tab() # close ally tab
    logging.info('successfully completed ally run')

def login_ally():
    debugSafety.debug_extra_safety()
    pyautogui.write("https://secure.ally.com/")
    pyautogui.press("enter")
    time.sleep(1)
    pwmanager.autofill()
    logging.info("logged into ally")

def get_ally_balances_raw():
    """
    Must be logged in to perform this function.
    Uses Edge browser's control+shift+x hotkey to select text.
    """
    debugSafety.debug_extra_safety()
    pyautogui.click(90, 410, duration=cfg.settings["default_duration"])
    pyautogui.hotkey("ctrl", "shift", "x") # edge x select feature - generalize out for other browsers
    pyautogui.dragTo(900, 700, button="left")
    time.sleep(cfg.settings["default_duration"])
    pyautogui.hotkey("ctrl", "c")
    logging.info("copied ally raw data to edge clipboard")

def paste_and_clean_ally_acct_data():
    debugSafety.debug_extra_safety()
    pyautogui.click(115,240,duration=cfg.settings["default_duration"])
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "v") # paste the raw copied ally bank text into excell online
    time.sleep(0.5)
    excell.clear_all_text_formatting()
    excell.remove_all_hyperlinks()
    logging.info("pasted ally data into excell online window removed text formatting and hyperlinking")

def construct_individual_ally_acct_balance(date_stamp, bank_name, name_a_cell, name_b_cell, balance_cell):
    """
    Runs as part of ally_run() function.
    """
    debugSafety.debug_extra_safety()
    # grab first part of bank name identifier
    excell.cell_to_clipboard(name_a_cell)
    acct_type_constructed=pyperclip.paste()
    # add account num stub to name identifier
    excell.cell_to_clipboard(name_b_cell)
    acct_num_stub=pyperclip.paste()
    acct_type_constructed=acct_type_constructed+acct_num_stub
    # get balance
    excell.cell_to_clipboard(balance_cell)
    balance_constructed=pyperclip.paste()
    logging.info(f"ally account name: {acct_type_constructed}, ally account balance: {balance_constructed}")
    return f"{date_stamp},{bank_name},{acct_type_constructed},{balance_constructed}\n"