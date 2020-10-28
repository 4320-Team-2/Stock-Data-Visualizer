from UserInput import UserInput

class ChartTypeInput(UserInput):
    
    def __init__(self):

        """Chart Type input constructor"""
            
        # The example txt displayed to the user on input request
        exampletxt =    ("Chart Types\r\n" +
                        "=============\r\n" +
                        "1. Bar\r\n" +
                        "2. Line\r\n")
            
        # Call base constructor initalizing prompt message and example txt
        UserInput.__init__(
            self, 
            "Enter the chart type you want (1, 2)",
            exampletxt)

        def isInputValid(self, input):
            chartType = ""
            if (input == "1"):
                chartType = "Bar"
                return True
            elif (input == "2"):
                chartType = "Line"
                return True
            else:
                print("Please enter 1 or 2")
                __init__
                return False

