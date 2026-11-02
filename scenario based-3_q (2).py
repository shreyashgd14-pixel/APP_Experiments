import csv
import sys

filename = sys.argv[1]

with open(filename, 'r') as file:
    records = list(csv.reader(file))

print("All Employee Details:")
for row in records:
    print(row)

emp_id = input("\nEnter Employee ID to search: ")
for row in records:
    if row and row[0] == emp_id:
        print("Found:", row)
        break
