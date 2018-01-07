from enum import Enum


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
    annual = annual()
    semi_annual = semi_annual()
    quarterly = quarterly()
    monthly = monthly()



class Rebalance:
    def __init__(self, period_start):
        self.period_start = period_start


if __name__ == '__main__':
    rebalance = Rebalance('2')
    print(get_date(period.annual, rebalance))
