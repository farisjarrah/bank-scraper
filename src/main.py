import pyautogui

import config as cfg
import banks

# PyAutoGui running options
# pyautogui failsafe
# engage by moving mouse to corner of screen
pyautogui.FAILSAFE = cfg.pyautogui_running_opts["pyautogui_failsafe"]

def main():
    print('Press Ctrl-C to quit.')
    try:
        banks.bank_run()
    except KeyboardInterrupt:
        print('KEYBOARD INTERRUPT\n')        

if __name__ == "__main__":
    main()