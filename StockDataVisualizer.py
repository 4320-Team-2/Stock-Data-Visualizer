from SymbolInput import SymbolInput
from ChartTypeInput import ChartTypeInput
from Constants import Constants

class StockDataVisualizer:
    def __init__(self):

        self.userInputs = {
            Constants.SYMBOL: SymbolInput(),
            Constants.CHARTTYPE: ChartTypeInput()
        }

    def gatherUserInput(self):
        """ 
        Using the required self.userInputs, prompts user for required inputs and validates provided values. 
        Valid inputs are stored in the respective self.userInputs[i].value 
        """

        for field in self.userInputs:
            ui = self.userInputs[field]
            while True:
                print(ui.optionsTxt)
                userInput = input(ui.promptMsg + ":")
                if(ui.trySetValue(userInput)):
                    break
                else:
                    print("Value '" + userInput + "' is not valid.")

    def queryStockData(self):
        #TODO: make API call for stock data using self.userInputs[i].values
        raise Exception("unimplemented")