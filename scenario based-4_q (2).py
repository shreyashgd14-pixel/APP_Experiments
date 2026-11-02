import numpy as np
import pandas as pd

salaries = np.array([45000, 55000, 65000, 72000, 50000, 80000])

print("Average Salary:", np.mean(salaries))
print("Maximum Salary:", np.max(salaries))
print("Minimum Salary:", np.min(salaries))

df = pd.DataFrame({
    'Employee': ['Rahul', 'Priya', 'Amit', 'Sneha', 'Neha', 'Kiran'],
    'Salary': salaries
})

print("\nEmployees earning more than ₹60,000:")
print(df[df['Salary'] > 60000])
