from SymbolInput import SymbolInput
from ChartTypeInput import ChartTypeInput
from Constants import Constants

class StockDataVisualizer:
    
    def __init__(self, inputData):
        """ Initalizes a stock data visualizer with the given StockDataVisualizerInputs. """
        self.inputData = inputData
        #TODO: Validate each input data has a set value

    def queryStockData(self):
        """ Given a set of inputs performs a stock query """
        #TODO: make API call for stock data using self.inputData.userInputs[Constants.SYMBOL].value
        #raise Exception("unimplemented")