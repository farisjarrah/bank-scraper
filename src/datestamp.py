import datetime

def generate_date_stamp():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%dT%H:%M:%S.%f')

## TODO DELETE THIS FILE, its only being used in ally and schwab, we can move all the functionality to the logger.py