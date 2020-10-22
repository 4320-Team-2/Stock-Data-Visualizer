from UserInput import UserInput

class SymbolInput(UserInput):
    
    def __init__(self):
        """Symbol input constructor"""
        UserInput.__init__(
            self, 
            "Enter the stock symbol you are looking for")

    def validateInput(self, input):
        """The shared validate input function."""
        if (input == "Test"):
            return True
        else:
            return False
