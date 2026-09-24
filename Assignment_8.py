import csv
with open("student.txt", "w") as file:
    file.write("Hello World \n")
    file.write("Welcome to Mit adt\n")
    file.write("branch cse\n")
    file.write("SY -1\n")

with open("student.txt", "r") as file:
    lines = input_file.readlines()

line_count = len(lines)


first_two_lines = lines[:2]

with open("student_2.txt", "w") as file2:
    file2.writelines(first_two_lines)

file.close()
file2.close()
