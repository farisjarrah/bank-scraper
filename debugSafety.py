import time

import pyautogui

import config as cfg

def debug_extra_safety():
    if cfg.settings["debug_extra_safety"] == True:
        # FOR DEBUGGING: Click on the window before doing actions
        pyautogui.click(cfg.settings["safe_space_x"], cfg.settings["safe_space_y"])
        time.sleep(0.5)