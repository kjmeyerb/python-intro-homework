import os
import csv
import datetime
import sys

data_file= os.path.join("..","data","expenses.csv")

def parsecategories(records):
    catoptions = set()
    for row in records:
        catoptions.add(row["category"])
    category=input(f"Generate a report for which category? \n{catoptions}\n").capitalize()
    while category not in catoptions:
        category=input(f"Category not found. Try again. \n{catoptions}\n").capitalize()
    return category

#Ideally, I would create another function to compare the report to any previous report.
#I would give the client an option to aggregate or create a report of only new records.
#If aggregate, I would use the write method to overwrite with all the information.
#If only new, I would filter out existing records and append. 

def catreport(category):
    catrecords = []
    cattotal = 0
    today = datetime.datetime.now().strftime("%B %d, %Y")
    with open(f"{category}Report.txt", "a", newline="") as file:
        content = file.write(f"\n{category} Expense Report - generated {today}\n")
        for row in records:
            amount=float(row["amount"])
            if row["category"]== category.capitalize():
                catrecords.append(row)
                cattotal += amount
                content = file.write(f"\n{row["date"]}: ${amount:.2f}")
            else:
                continue
        content = file.write(f"\n\nTotal: ${cattotal:.2f}")
    print(f"{category}Report.txt created.")

if os.path.exists(data_file):
    print(f"{data_file} exists!")
    with open(data_file, "r") as file:
        records = list(csv.DictReader(file))
        catreport(parsecategories(records))
else:
    print(f"{data_file} was not found. \n Aborting.")
    sys.exit()

