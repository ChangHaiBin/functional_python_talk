
from functional_util import then, keep, remove, change, sumby
import math
import datetime

def dummy_sql_fetchall(query):
    return [
        (200, 'SG'),
        (160, 'my'),
        (300, 'sg'),
        (500, 'sG'),
        (222, 'USA')
    ]

today = datetime.datetime.utcnow()

def country_to_upper(tp):
    return tp[0], tp[1].upper()

commission = \
    "select * from salesDB where date = '%Y-%m-%d'" \
    | then | today.strftime \
    | then | dummy_sql_fetchall \
    | then | change(country_to_upper) \
    | then | keep(lambda row: row[1] == 'SG') \
    | then | sumby(lambda row: row[0]) \
    | then | (lambda totalsale: totalsale * 0.2)

print(commission)

