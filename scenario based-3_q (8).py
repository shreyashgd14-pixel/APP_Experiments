import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

with open(args.filename, 'r') as file:
    records = list(csv.reader(file))

print("All Course Records:")
for row in records:
    print(row)

course_id = input("\nEnter Course ID to search: ")
for row in records:
    if row and row[0] == course_id:
        print("Found:", row)
        break
