from pathlib import Path
import csv

def profit_loss_function():
    """
    - This function detects three types of trends in data: increasing, decreasing, and fluctuating. 
      For increasing trends it calculates the highest increment in NET PROFIT and the day it happened
      While for decreasing trends, it calculates the highest decrement in NET PROFIT and the day it happened
      When faced with the fluctuating data trend the function will calculate the top 3 highest NET PROFIT deficits and also calculate all the NET PROFIT deficits

    - No parameters needed 
    """
    # Creating file path to the cash on hand file
    fp = Path.cwd()/"csv_reports"/"Profits_and_Loss.csv"
    # Checking if file path exists
    print(fp.exists()) 

    # read the csv file.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        # Create empty list to put the difference data and all the deficit values
        difference_in_net_profit = []
        total_deficit=[]

        # Create lists for the top 3 deficits with 0 deficit values to allow for loop function to run through
        first_deficit=['day', 0]
        second_deficit=['day', 0]
        third_deficit=['day', 0]

        # Create lists for highest increment and decrement with 0 values to allow for loop function to run through
        highest_increment = ['day', 0]
        highest_decrement = ['day', 0]

        # Process the first data row to set the initial previous net profit
        first_data_row= next(reader) # skip header 
        previous_net_profit = float(first_data_row[4])

        # Loop through the rows to calculate daily net profit differences
        for row in reader:
            day = row[0]
            current_net_profit = float(row[4])
            # Calculate the difference and append it to the list
            difference = current_net_profit - previous_net_profit
            difference_in_net_profit.append([day, difference])  # Store the day and difference as a list

            # Update previous net profit with current net profit
            previous_net_profit = current_net_profit


