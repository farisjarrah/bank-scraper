import toolbox
import browsers
import logger
import logging

###
### Schwab Bank
###
## This is the main schwab bank run. It gathers schwab bank account entry data and output it as a csv for the logger: datestamp,schwab,<account identifier>,$<account balance>
def schwab_run():
    browsers.login_to_site("https://client.schwab.com/Login/SignOn/CustomerCenterLogin.aspx")
    logger.log_csv(toolbox.return_bank_balance("schwab", 162, 793, 134, 806, 783, 786))
    logger.log_csv(toolbox.return_bank_balance("schwab", 238, 835, 130, 855, 784, 837))
    logger.log_csv(toolbox.return_bank_balance("schwab", 182, 889, 132, 900, 783, 882))
    browsers.close_tab() # close schwab tab
    logging.info("successfully completed schwab run")