import datetime

def generate_date_stamp():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%dT%H:%M:%S')