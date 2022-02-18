import logging
import toolbox
import browsers
import logger

def bank_run():
    browsers.open_new_window()
    ally()
    schwab()
    browsers.close_window()

### Ally Bank
def ally():
    browsers.login_to_site("https://secure.ally.com/")
    logger.log_csv(toolbox.return_bank_balance("ally", 217, 451, 150, 480, 415, 452))
    logger.log_csv(toolbox.return_bank_balance("ally", 252, 625, 151, 647, 417, 620))
    browsers.close_tab() # close ally tab
    logging.info("successfully completed ally run")

### Schwab Bank
def schwab():
    browsers.login_to_site("https://client.schwab.com/Login/SignOn/CustomerCenterLogin.aspx")
    logger.log_csv(toolbox.return_bank_balance("schwab", 162, 793, 134, 806, 783, 786))
    logger.log_csv(toolbox.return_bank_balance("schwab", 238, 835, 130, 855, 784, 837))
    logger.log_csv(toolbox.return_bank_balance("schwab", 182, 889, 132, 900, 783, 882))
    browsers.close_tab() # close schwab tab
    logging.info("successfully completed schwab run")