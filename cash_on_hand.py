from pathlib import Path
import csv

#Creating file path to the cash on hand file
fp = Path.cwd()/"csv_reports"/"increasing.csv"
#Checking if file path exists
print(fp.exists()) 

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header