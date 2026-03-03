import pandas as pd

df = pd.read_csv('dz.csv')
df['Test'] = [new for new in range(12)]


print(df.head())
df.drop('Test', axis=1, inplace=True)
group=df.groupby('City')['Salary'].mean()
print(group)





