#Time Series Function Input

while(1):
    try:
        selection = int(input("Select the Time Series of the chart you want to Generate \n--------------------------------------------------------\n1. Intraday \n2. Daily \n3. Weekly \n4. Monthly\n\nEnter time series option (1, 2, 3, 4):  "))
        if(selection < 1 or selection > 4):
            print("\nThe input you entered is invalid. Please enter one of the four options.\n")
            continue
    except ValueError:
        print("\nThe value you entered is not an integer. Please enter one of the four options.\n")
    else:
        break
