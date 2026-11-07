import os
import csv

file=os.path.join("..", "data", "messy_data.csv")

def parse_file(file):
    reader=csv.DictReader(file)
    row_attempt=0
    row_parsed=0
    row_skipped=0
    report_rows=[]
    report_errors=[]
    for i, row in enumerate(reader, start=1):
        row_attempt += 1
        if None in row:
            row_skipped+=1
            report_errors.append(f"Row {i}: 'None' detected.")
            continue
        try:
            report_rows.append([row['name'],row['category'],float(row['amount'])])
        except ValueError as e:
            row_skipped+=1
            report_errors.append(f"Row {i}: Value Error - could not convert '{row['amount']}' to float.")
        except KeyError as e:
            row_skipped+=1
            report_errors.append(f"Row {i}: KeyError - missing expected column.")
        else:
            row_parsed+=1
    return row_attempt, row_parsed, row_skipped, report_rows, report_errors

def printsummary(row_attempt, row_parsed, row_skipped, report_rows, report_errors):
    print(f"\n=== CSV Report ===")
    print(f"Rows attempted: {row_attempt}")
    print(f"Rows parsed: {row_parsed}")
    print(f"Rows skipped: {row_skipped}")
    print(f"\nSkipped Rows:")
    for line in report_errors:
        print(line)
    print(f"\nClean Data:")
    for line in report_rows:
        print(line)

try:
    with open(file, "r") as file:
        row_attempt, row_parsed, row_skipped, report_rows, report_errors=parse_file(file)
except FileNotFoundError:
    print("File not found.")
else:
    printsummary(row_attempt, row_parsed, row_skipped, report_rows, report_errors)