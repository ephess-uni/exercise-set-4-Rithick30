""" ex_4_2.py """
from datetime import datetime


def logstamp_to_datetime(datestr):
    """INPUT-> datestr as string
        OUTPUT-> date object"""
    bad_guy = datestr
    good_guy = '%Y-%m-%dT%H:%M:%S'
    return datetime.strptime(bad_guy, good_guy)


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    test_date = '2022-12-01T01:02:03'
    print(f'{logstamp_to_datetime(test_date)=}')
