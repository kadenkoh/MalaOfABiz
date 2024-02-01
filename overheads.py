from pathlib import Path
import csv

def overheads_function():
    """
    - This function finds out the highest overhead percentage and writes it into the summary text file 
    - No parameter needed 
    """
    #Creating file path to the cash on hand file
    fp = Path.cwd()/"csv_reports"/"Overheads.csv"
    #Checking if file path exists
    print(fp.exists()) 

    # read the csv file.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        #setting up the variable to keep track of the highest overhead amount
        highest_overhead_amount= -0.1 #set the highest overhead amount as -0.1 which is a small negative number to ensure any overhead amount in the CSV file will replace it

        #read the data from each row of the csv file
        for row in reader:
                category = row[0]
                current_overhead_amount = float(row[1])
                #compare each current overhead amount to the current highest overhead amount
                if current_overhead_amount > highest_overhead_amount:
                    #if the current overhead amount is greater, update the highest overhead amount and category
                    highest_overhead_amount=current_overhead_amount
                    highest_overhead_category=category
            
    #file path to txt file
    fp = Path.cwd()/"summary_report.txt"
    #creating txt file
    fp.touch()
    #opening the summary text file and set it to write mode
    with fp.open(mode="w", encoding="UTF-8", newline="") as file:
        #writing the highest overhead into the summary text file
        file.write(f"[HIGHEST OVERHEAD] {highest_overhead_category.upper()}: {highest_overhead_amount}%")

