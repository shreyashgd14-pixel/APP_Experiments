import numpy as np
import pandas as pd

prices = np.array([45, 120, 15, 250, 85, 30])

print("Mean Price:", np.mean(prices))
print("Median Price:", np.median(prices))
print("Maximum Price:", np.max(prices))
print("Minimum Price:", np.min(prices))

df = pd.DataFrame({
    'Item': ['Milk', 'Rice', 'Bread', 'Olive Oil', 'Butter', 'Eggs'],
    'Price': prices,
    'Quantity': [5, 20, 8, 3, 15, 12]
})

print("\nItems with quantity less than 10:")
print(df[df['Quantity'] < 10])
