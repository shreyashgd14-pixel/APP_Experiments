import pandas as pd
import numpy as np

print(pd.Series(np.random.rand(10)))


s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [24, 27]})

print(df['Name'])
print(df.iloc[0])
print(df.loc[0])

df = df.dropna().drop_duplicates()
df['Age'] = df['Age'].fillna(df['Age'].mean())


df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['Alice', 'Bob']})
df2 = pd.DataFrame({'ID': [1, 2], 'Age': [24, 27]})
merged = pd.merge(df1, df2, on='ID', how='inner')

df = pd.DataFrame({'Dept': ['HR', 'IT', 'HR'], 'Salary': [50000, 60000, 52000]})
print(df.groupby('Dept')['Salary'].agg(['mean', 'sum', 'max']))

df = pd.read_csv('employees.csv').dropna().drop_duplicates()
print(df.groupby('Department')['Salary'].mean())
print(df.groupby('Department')['Age'].agg(['max', 'min']))
