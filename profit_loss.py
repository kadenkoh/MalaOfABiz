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
            difference_in_net_profit.append([day, difference])  # Store the day and difference as a 

            # Update previous net profit with current net profit
            previous_net_profit = current_net_profit

            # Identifying the deficits which are negative differences
            if difference < 0:
                # Append all deficits into a list 
                total_deficit.append([day, difference]) 

        # Calculating the highest increment and decrement of net profit
        for day, difference in difference_in_net_profit:

            # Checking if the current difference of net profit is less than the current highest decrement 
            # If it is, this becomes the new highest decrement
            if difference < highest_decrement[1]:
                highest_decrement=[day, difference]
            # Checking if the current difference is greater than the current highest increment
            # If it is, this becomes the new highest increment
            elif difference > highest_increment[1]:
                highest_increment=[day, difference]

    # file path to txt file
    fp = Path.cwd()/"summary_report.txt"

    # creating txt file
    fp.touch()

    # Opening the summary text file in append mode to ensure that the profit and loss calculation results, is added without overwriting existing data. 
    with fp.open(mode="a", encoding="UTF-8", newline="") as file:

        # Checking if theres always only a increasing trend in the net profit by seeing if everydays net profit is higher than the previous day and if there is, write the highest increment day and amount in the summary text file
        if highest_increment[1] > 0 and highest_decrement[1] == 0:
            file.write(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS\n [HIGHEST NET PROFIT SURPLUS] DAY: {highest_increment[0]}, AMOUNT: SGD{int(highest_increment[1])}")
        # Checking if theres always only a decreasing trend in the net profit by seeing if everydays net profit is lower than the previous day and if there is, write the highest decrement day and amount in the summary text file
        elif highest_decrement[1] < 0 and highest_increment[1] == 0:
            file.write(f"[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN THE PREVIOUS\n [HIGHEST PROFIT DEFICIT] DAY: {highest_decrement[0]}, AMOUNT: SGD{int(abs(highest_decrement[1]))}")
        # Checking if there is a fluctuating data trend in the net profit by seeing if theres an higher net profit on some days and lower on some days and if there is, write all the deficits into the summary text file
        elif highest_increment[1] > 0 and highest_decrement[1] < 0:
            for day, deficit in total_deficit:
                file.write(f"[NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{int(abs(deficit))}\n")

                # Identify the highest deficit
                if deficit < first_deficit[1]:
                    # If the deficit is more negative than the deficit in first_deficit, then update it with the new deficit and its corresponding day
                    first_deficit= [day, deficit]
                # Identify the second highest deficit
                elif deficit < second_deficit[1]:
                    # If the deficit is less negative than the deficit in first_deficit but more negative than the deficit in second_deficit, then update it with the new deficit and its corresponding day
                    second_deficit = [day, deficit]
                # Identify the third highest deficit
                elif deficit< third_deficit[1]:
                    # If the deficit is less negative than both the first and second but greater than the third largest recorded deficit, then update it with the new deficit and its corresponding day
                    third_deficit = [day, deficit]

            # Writing the top 3 deficits into the summary text file
            file.write(f"[HIGHEST NET PROFIT DEFICIT] DAY: {first_deficit[0]}, AMOUNT: SGD{int(abs(first_deficit[1]))}\n[2ND HIGHEST NET PROFIT DEFICIT] DAY: {second_deficit[0]}, AMOUNT: SGD{int(abs(second_deficit[1]))}\n[3RD HIGHEST NET PROFIT DEFICIT] DAY: {third_deficit[0]}, AMOUNT: SGD{int(abs(third_deficit[1]))}\n")







