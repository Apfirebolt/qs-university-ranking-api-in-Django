import pandas as pd


df = pd.read_csv('data/2023_data.csv')

result = df.head(10)

for index, row in df.iterrows():
    print(row['Rank'], row['institution'], row['location'], row['location code'], row['ar score'], row['ar rank'])
    