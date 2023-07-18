""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<

def time_between_shutdowns(logfile):
    """INPUT-> name of the file
        OUTPUT-> timedelta OBJECT of the difference"""
    x = get_shutdown_events(logfile)
    y = list()
    for i in x:
        u = i.split()[1]
        y.append(logstamp_to_datetime(u))
    return y[-1]-y[0]


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
