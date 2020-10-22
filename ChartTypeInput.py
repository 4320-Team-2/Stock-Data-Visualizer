from UserInput import UserInput

class ChartTypeInput(UserInput):
    
    def __init__(self):
        """Symbol input constructor"""
        exampletxt =    ("Chart Types\r\n" +
                        "=============\r\n" +
                        "1. Bar\r\n" +
                        "2. Line\r\n")
        
        UserInput.__init__(
            self, 
            "Enter the chart type you want (1, 2)",
            exampletxt)

    def validateInput(self, input):
        """The shared validate input function."""
        if (input == "Test"):
            return True
        else:
            return False