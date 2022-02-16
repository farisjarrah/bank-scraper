import pyautogui

import config as cfg
import browsers, ally, schwab

# PyAutoGui running options
# pyautogui failsafe
# engage by moving mouse to corner of screen
pyautogui.FAILSAFE = cfg.pyautogui_running_opts["pyautogui_failsafe"]

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