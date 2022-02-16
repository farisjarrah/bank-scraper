import debugSafety
import config as cfg

import pyautogui
import pyperclip

def copy():
    pyautogui.hotkey("ctrl", "c")

def copy_and_return_result():
    copy()
    result = pyperclip.paste()
    return result

def highlight_text_area(x_pos, y_pos):
    pyautogui.click(x=x_pos, y=y_pos, clicks=3, interval=.25, duration=.25)

def return_text_area(x_pos, y_pos):
    highlight_text_area(x_pos, y_pos)
    result = copy_and_return_result()
    result_cleaned = " ".join(result.splitlines())
    return result_cleaned

def paste():
    pyautogui.hotkey("ctrl", "v")

def build_account_name(
    account_coordinates_x,
    account_coordinates_y,
    account_num_stub_coordinates_x,
    account_num_stub_coordinates_y
    ):
    account_type = return_text_area(account_coordinates_x, account_coordinates_y)
    account_number_stub = return_text_area(account_num_stub_coordinates_x, account_num_stub_coordinates_y)
    return account_type + account_number_stub

def return_bank_balance(
    bank,
    acct_name_pos_x,
    acct_name_pos_y,
    acct_num_stub_pos_x,
    acct_num_stub_pos_y,
    balance_pos_x,
    balance_pos_y
    ):
    debugSafety.debug_extra_safety()
    account_name = build_account_name(
        acct_name_pos_x,
        acct_name_pos_y,
        acct_num_stub_pos_x,
        acct_num_stub_pos_y
        )
    balance = return_text_area(balance_pos_x, balance_pos_y)
    entry = f"{bank},{account_name},{balance}"
    return entry