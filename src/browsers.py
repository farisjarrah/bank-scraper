import time
import logging

import pyautogui

import debugSafety
import pwmanager
import config as cfg

def open_new_blink_window():
    # windows 10
    pyautogui.moveTo(128, 1079, duration=cfg.settings["default_duration"])
    pyautogui.rightClick(128, 1065, duration=cfg.settings["default_duration"])
    pyautogui.leftClick(75, 880, duration=cfg.settings["default_duration"])
    time.sleep(cfg.settings["default_duration"])
    pyautogui.hotkey("winleft", "left") # shift window to left half of 1920x1080 window
    time.sleep(cfg.settings["default_duration"])
    pyautogui.press("esc")
    pyautogui.leftClick(205, 25, duration=cfg.settings["default_duration"])
    logging.info('opened new blink family browser window')

def open_new_blink_tab():
    debugSafety.debug_extra_safety()
    pyautogui.hotkey("ctrl", "t")
    pyautogui.leftClick(205, 30, duration=cfg.settings["default_duration"])
    logging.info('opened new blink family browser tab')

def close_blink_window():
    pyautogui.hotkey("ctrl", "shift", "w")
    logging.info('closed blink family browser window')

def close_blink_tab():
    debugSafety.debug_extra_safety()
    pyautogui.hotkey("ctrl" + "w")
    logging.info('closed blink family browser window')

def open_new_window():
    if cfg.settings["default_browser"] in cfg.browsers["blink"]:
        open_new_blink_window()

def close_window():
    if cfg.settings["default_browser"] in cfg.browsers["blink"]:
        close_blink_window()

def open_new_tab():
    if cfg.settings["default_browser"] in cfg.browsers["blink"]:
        open_new_blink_tab()

def close_tab():
    if cfg.settings["default_browser"] in cfg.browsers["blink"]:
        close_blink_tab()

def login_to_site(url):
    open_new_tab()
    debugSafety.debug_extra_safety()
    pyautogui.write(url)
    pyautogui.press("enter")
    time.sleep(1)
    pwmanager.autofill()
    log_entry = f"logged in to {url}"
    logging.info(log_entry)