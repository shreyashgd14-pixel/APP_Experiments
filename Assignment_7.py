import re

text = "abc.14@gmail.com or 123.rg@yahoo.com"
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(pattern, text)

print(emails)
