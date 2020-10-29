import datetime
class dateValidator:
    #passing in the start date provided by user
    def __init__(self, startDate):
        self.startDate = startDate

    def endDate(self):
        #loop until user provides valid input
        while True:
            #try block to catch value errors
            try:
                endDate = input("Enter the end Date (YYYY-MM-DD): ")
                #splitting input to use with datetime module
                d1 = self.startDate.split(('-'))
                d2 = endDate.split('-')
                #creating datetime objects
                start = datetime.datetime(int(d1[0]),int(d1[1]),int(d1[2]))
                end = datetime.datetime(int(d2[0]),int(d2[1]),int(d2[2]))
                #error handling for end date before start date
                if start == end:
                    print("[ERROR] Start date cannot be the same as end date\n")
                elif start > end:
                    print("[ERROR] Start date cannot be after end date\n")
                else:
                    print("Valid date input")
                    return end.date()
                    break
            except ValueError:
                print("[ERROR] Invalid date provided.\n")

#Error checking and example use
#date = dateValidator("1999-06-29")
#endDate = date.endDate()