import time
import logging

import pyautogui

import debugSafety
import config as cfg

## Open a fresh microsoft excell online book
def open_new_excell_online_book():
    debugSafety.debug_extra_safety()
    pyautogui.hotkey('ctrl', 't')
    time.sleep(cfg.settings["default_duration"])
    pyautogui.write("https://www.office.com/launch/excel?auth=1")
    time.sleep(cfg.settings["default_duration"])
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.leftClick(240,275,duration=cfg.settings["default_duration"])
    logging.info('opened new excell online workbook')
    time.sleep(14)

def clear_all_text_formatting():
    #excell clear all text formatting
    pyautogui.click(435,75,duration=cfg.settings["default_duration"])
    pyautogui.write("clear formats") # remove any formatting
    time.sleep(cfg.settings["default_duration"])
    pyautogui.press("down")
    time.sleep(cfg.settings["default_duration"])
    pyautogui.press("enter")
    logging.info("cleared all text formatting from excell online selection")
    time.sleep(1)

def remove_all_hyperlinks():
    pyautogui.click(435,75,duration=cfg.settings["default_duration"])
    time.sleep(cfg.settings["default_duration"])
    pyautogui.write("remove hyperlinks")
    time.sleep(cfg.settings["default_duration"])
    pyautogui.press("down")
    time.sleep(cfg.settings["default_duration"])
    pyautogui.press("enter")
    logging.info("removed all hyperlinks from excell online selection")
    time.sleep(1)

def cell_to_clipboard(cell_id):
    pyautogui.leftClick(695,600,duration=cfg.settings["default_duration"]) # random click to reset message box, otherwise edge tweaks out
    pyautogui.leftClick(95,185,duration=cfg.settings["default_duration"])
    pyautogui.write(cell_id)
    time.sleep(cfg.settings["default_duration"])
    pyautogui.press("enter")
    time.sleep(cfg.settings["default_duration"])
    pyautogui.click(242,191, clicks=3, interval=cfg.settings["default_duration"])
    time.sleep(cfg.settings["default_duration"])
    pyautogui.hotkey("ctrl", "c")
    logging.info(f"copied cell to clipboard: {cell_id}")