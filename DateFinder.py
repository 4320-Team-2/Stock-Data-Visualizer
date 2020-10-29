#This program finds the dates inbetween the START_DATE and END_DATE provided by the user.
from datetime import date, timedelta, datetime
import Constants

start = datetime.strptime(Constants.START_DATE, "%Y-%m-%d")
end = datetime.strptime(Constants.END_DATE, "%Y-%m-%d")

#Start Date
sdate = start
#End Date
edate = end

#Time Delta
delta = edate - sdate

stockDates = []

# Finds the dates inbetween the start and end dates, they're formated as a date time and will need to be casted as strings.
for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    stockDates.append(day)


date_strings = []

# Casting the list contents into strings.
for dt in stockDates:
    date_strings.append(dt.strftime("%Y-%m-%d"))
