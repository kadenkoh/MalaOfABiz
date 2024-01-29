from pathlib import Path
import csv

#Creating file path to the cash on hand file
fp = Path.cwd()/"csv_reports"/"Overheads.csv"
#Checking if file path exists
print(fp.exists()) 

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    #setting up the variables 
    highest_overhead_amount= -0.1 #set the highest overhead amount as -0.1 to allow for all overhead values to be cycled through

    # read the data from each row
    for row in reader:
            category = row[0]
            overhead_amount = float(row[1])
            #loop through all the overhead amounts in the csv file till the largest amount is captured and no other values can be greater than that and the loop stops and presents the highest overhead amount
            if overhead_amount > highest_overhead_amount:
                highest_overhead_amount=overhead_amount
                highest_overhead_category=category
                
    #file path to txt file
    fp = Path.cwd()/"summary_report.txt"
    #creating txt file
    fp.touch()
    #opening the summary text file and set it to write mode
    with fp.open(mode="w", encoding="UTF-8", newline="") as file:
        #writing the highest overhead into the summary text file
        file.write(f"[HIGHEST OVERHEAD] {highest_overhead_category.upper()}: {highest_overhead_amount}%")