import csv
import json

file_1= with open("student.csv","r")
file_2= with open("students.json","r")
data=["raj",3,10]
csv_reader= csv.reader(file_1)
for row in csv_reader:
  data.append(row)
json_file = json.reader(file_2)
json.dump(data,json_file)
file_1.close()
file_2.close()
