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
### Schwab Bank
###
## This is the main schwab bank run. It gathers schwab bank account entry data and output it as a csv for the logger: datestamp,schwab,<account identifier>,$<account balance>
def schwab_run():
    browsers.open_new_tab()
    login_schwab()
    get_schwab_balances_raw()
    excell.open_new_excell_online_book()
    paste_and_clean_schwab_acct_data()
    logger.log_csv(construct_individual_schwab_acct_balance(datestamp.generate_date_stamp(), "schwab", "A1", "A2", "A5"))
    logger.log_csv(construct_individual_schwab_acct_balance(datestamp.generate_date_stamp(), "schwab", "A7", "A8", "A11"))
    logger.log_csv(construct_individual_schwab_acct_balance(datestamp.generate_date_stamp(), "schwab", "A13", "A14", "A17"))
    browsers.close_tab() # close excel online tab
    browsers.close_tab() # close schwab tab
    logging.info("successfully completed schwab run")

def login_schwab():
    debugSafety.debug_extra_safety()
    pyautogui.write("https://client.schwab.com/Login/SignOn/CustomerCenterLogin.aspx")
    pyautogui.press("enter")
    time.sleep(1)
    pwmanager.autofill()
    logging.info("logged into schwab")

def get_schwab_balances_raw():
    """
    Must be logged in to perform this function.
    Uses Edge browser's control+shift+x hotkey to select text.
    """
    debugSafety.debug_extra_safety()
    pyautogui.click(60, 770, duration=cfg.settings["default_duration"])
    pyautogui.hotkey("ctrl", "shift", "x") # edge text select hotkey
    pyautogui.dragTo(800, 960, button="left")
    time.sleep(cfg.settings["default_duration"])
    pyautogui.hotkey("ctrl", "c")
    logging.info("schwab raw balances copied to edge clipboard")

def paste_and_clean_schwab_acct_data():
    debugSafety.debug_extra_safety()
    pyautogui.click(115,240,duration=cfg.settings["default_duration"])
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "v") # paste the raw copied schwab bank text into excell online
    time.sleep(0.5)
    excell.clear_all_text_formatting()
    logging.info("pasted schwab account data and removed text formatting")

def construct_individual_schwab_acct_balance(date_stamp, bank_name, name_a_cell, name_b_cell, balance_cell):
    """
    Runs as part of schwab_run() function.
    """
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
    logging.info(f"schwab account name: {acct_type_constructed}, schwab account balance: {balance_constructed}")
    return f"{date_stamp},{bank_name},{acct_type_constructed},{balance_constructed}\n"