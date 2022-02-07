#! python3
import logging

import pyautogui

import config as cfg
import browsers, ally, schwab

# PyAutoGui running options

# pyautogui failsafe
# engage by moving mouse to corner of screen
pyautogui.FAILSAFE = cfg.pyautogui_running_opts["pyautogui_failsafe"]

logging.basicConfig(filename=cfg.settings["program_log"], encoding='utf-8', level=cfg.settings["log_level"], format='%(asctime)s - %(levelname)s - %(message)s')


# main run
def main():
    print('Press Ctrl-C to quit.')
    try:
        browsers.open_new_window()
        ally.ally_run()
        schwab.schwab_run()
        browsers.close_window()
    except KeyboardInterrupt:
        print('KEYBOARD INTERRUPT\n')        

if __name__ == "__main__":
    main()