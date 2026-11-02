import re

text = "Contact us at support@example.com, sales-info@company.co.uk, or john.doe123@sub.domain.org."
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(pattern, text)

print(emails)
