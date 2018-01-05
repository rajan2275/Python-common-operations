# ----------------------------------------------------------------------------------------------
# Using CustomBusinessDay, finds previous working day, if today is holiday, else returns today.
# --------------------------------------------------------------------------------------------
from pandas.tseries.offsets import CustomBusinessDay
from datetime import datetime

cust_business_day = CustomBusinessDay(holidays=[datetime.date(datetime(2018, 1, 4)),
                                                datetime.date(datetime(2018, 1, 3)),
                                                datetime.date(datetime(2018, 1, 1)),
                                                datetime.date(datetime(2017, 12, 29))],
                                                weekmask='Mon Tue Wed Thu Fri')

#date = datetime.date(datetime(2018, 1, 5))
date = datetime.date(datetime(2017, 12, 30))


def _get_working_day(date, cust_business_day):
   if (date in cust_business_day.holidays or date.weekday()> 4):
         date = (date - 1 * cust_business_day).date()
   return date

date = _get_working_day(date, cust_business_day)

print(str(date))







