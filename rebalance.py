from enum import Enum
from functools import partial

def annual():
    print('annual.')


def semi_annual():
    print('semi_annual.')


def quarterly():
    print('quarterly.')


def monthly():
    print('monthly.')


def get_date(fnc, rebalance):
    fnc


class period(Enum):
    annual = 1
    semi_annual = 2
    quarterly = 3
    monthly = 4



class Rebalance:
    def __init__(self, period_start):
        self.period_start = period_start


def entry(period):
    if period == period.annual: get_date(annual(), rebalance)
    if period == period.semi_annual: get_date(semi_annual(), rebalance)
if __name__ == '__main__':
    rebalance = Rebalance('2')
    entry(period.annual)
    entry(period.semi_annual)
  #

