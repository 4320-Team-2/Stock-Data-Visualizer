class UserInput:
    def __init__(self, promptMsg, optionsTxt=""):
        self.promptMsg = promptMsg
        self.optionsTxt = optionsTxt
        self.value = None

    def trySetValue(self, input):
        if (self.validateInput(input)):
            self.value = input
            return True
        else:
            return False

    def validateInput(self, input):
        """Given the input invokes the specified validate function returning true if input is valid."""
        pass
    
