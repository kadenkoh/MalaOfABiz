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