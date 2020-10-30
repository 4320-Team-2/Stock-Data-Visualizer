import datetime
from UserInput import UserInput
def startDateinput:
    date_entry = input('Enter a date in YYYY-MM-DD format')
    year, month, day = map(int, date_entry.split('-'))
    date1 = datetime.date(year, month, day)