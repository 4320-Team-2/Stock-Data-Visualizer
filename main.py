import sys
from StockDataVisualizer import StockDataVisualizer

# Main program loop 
# Intializes and executes a stock query then prompts user
# if they want a redo.
while True:
    s = StockDataVisualizer()
    s.gatherUserInput()

    while True:
        again = input("Would you like to view more stock data? ('Y' or 'N'):").lower()
        if(again == 'y'):
            break
        elif(again != 'n'):
            print("'" + again + "' is not a valid value.")
        else:
            sys.exit(0)