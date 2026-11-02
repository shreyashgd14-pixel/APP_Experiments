import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Tenure': [1, 24, 3, 12, 48],
    'MonthlyCharges': [70.5, 55.0, 85.0, np.nan, 30.0],
    'Contract': ['Month', 'Year', 'Month', 'Two-Year', 'Two-Year'],
    'Churn': ['Yes', 'No', 'Yes', 'No', 'No']
})

df['MonthlyCharges'] = df['MonthlyCharges'].fillna(df['MonthlyCharges'].mean())
df['Churn_Num'] = (df['Churn'] == 'Yes').astype(int)

print("Summary Stats:\n", df.describe())
print("\nMean Metrics by Churn:\n", df.groupby('Churn').mean(numeric_only=True))
print("\nChurn Rate by Contract:\n", df.groupby('Contract')['Churn_Num'].mean() * 100)
