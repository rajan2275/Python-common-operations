from enum import Enum


def annual():
    print('annual.')


def semi_annual():
    print('semi_annual.')


def quarterly():
    print('quarterly.')


def monthly():
    print('monthly.')


def get_date(rebalance):
    rebalance.period()


class period(Enum):
    annual = annual()
    semi_annual = semi_annual()
    quarterly = quarterly()
    monthly = monthly()



class Rebalance:
    def __init__(self, period, period_start):
        self.period = period
        self.period_start = period_start


if __name__ == '__main__':
    rebalance = Rebalance(period.annual, '2')
    print(get_date(rebalance))
