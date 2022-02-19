import time
import logging

import pyautogui

import config as cfg

# password manager functions
def bitwarden_autofill():
    time.sleep(.75)
    pyautogui.hotkey("ctrl", "shift", "l")
    time.sleep(.75)
    pyautogui.press("enter")
    logging.info("autofilled entry from bitwarden")
    time.sleep(8)

def autofill(pw_manager=cfg.settings["password_manager"]):
    if pw_manager == "bitwarden":
        bitwarden_autofill()