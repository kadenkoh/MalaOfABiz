from pathlib import Path
import csv

def cash_on_hand_function():
    """
    - This function detects three types of trends in data: increasing, decreasing, and fluctuating. 
      For increasing trends it calculates the highest increment in cash on hand and the day it happened
      While for decreasing trends, it calculates the highest decrement in cash on hand and the day it happened
      When faced with the fluctuating data trend the function will calculate the top 3 highest cash on hand deficits and also calculate all the cash on hand deficits

    - No parameters are needed 
    """
    #Creating file path to the cash on hand file
    fp = Path.cwd()/"csv_reports"/"Cash_on_Hand.csv"
    #Checking if file path exists
    print(fp.exists()) 

    # read the csv file.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        # Create empty list to put the difference data and all the deficit values
        difference_in_cash_on_hand = []
        total_deficit=[]

        # Create lists for the top 3 deficits with 0 deficit values to allow for loop function to run through
        first_deficit=['day', 0]
        second_deficit=['day', 0]
        third_deficit=['day', 0]

        # Create lists for highest increment and decrement with 0 values to allow for loop function to run through
        highest_increment = ['day', 0]
        highest_decrement = ['day', 0]

        # Process the first data row to set the initial previous cash on hand
        first_row_of_data= next(reader)
        previous_cash_on_hand = float(first_row_of_data[1])

        # Loop through the rows to calculate daily cash on hand differences
        for row in reader:
            day = row[0]
            current_cash_on_hand = float(row[1])
            # Calculate the difference and append it to the list 
            difference = current_cash_on_hand - previous_cash_on_hand
            difference_in_cash_on_hand.append([day, difference])  

            # Update previous cash on hand with current cash on hand
            previous_cash_on_hand = current_cash_on_hand

            # Identifying the deficits which are negative differences
            if difference < 0:
                # Append all deficits into a list 
                total_deficit.append([day, difference])

        # Calculating the highest increment and decrement of cash on hand
        for day, difference in difference_in_cash_on_hand:
            
            # Checking if the current difference is less than the current highest decrement
            # If it is, this becomes the new highest decrement
            if difference < highest_decrement[1]:
                highest_decrement=[day, difference]
            # Checking if the current difference is greater than the current highest increment
            # If it is, this becomes the new highest increment
            elif difference > highest_increment[1]:
                highest_increment=[day, difference]