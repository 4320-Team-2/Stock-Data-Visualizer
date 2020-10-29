from SymbolInput import SymbolInput
from ChartTypeInput import ChartTypeInput
from Constants import Constants

class StockDataVisualizer:
    
    def __init__(self, inputData):
        """ Initalizes a stock data visualizer with the given dictionary where key is input constant and value is the user input. """
        self.inputData = inputData

    def queryStockData(self):
        """ Given a set of inputs performs a stock query """
        #TODO: make API call for stock data using self.inputData[Constants.SYMBOL]
        #raise Exception("unimplemented")