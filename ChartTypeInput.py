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
        """The shared validate input function."""
        if (input == "Test"):
            return True
        else:
            return False