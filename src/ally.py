import logging
import toolbox
import browsers
import logger

###
### Ally Bank
###

def ally_run():
    browsers.login_to_site("https://secure.ally.com/")
    logger.log_csv(toolbox.return_bank_balance("ally", 217, 451, 150, 480, 415, 452))
    logger.log_csv(toolbox.return_bank_balance("ally", 252, 625, 151, 647, 417, 620))
    browsers.close_tab() # close ally tab
    logging.info("successfully completed ally run")