import pandas as pd 

df = pd.read_csv('Q2-Dataset.csv')

print("                      ----------------OLD CSV FILE WITH NaN AND NULL VALUES-----------------                 ")
print(df)
print("                      ----------------NUMBER OF NULL VALUES IN EACH COLUMNS-----------------                 ")
print(df.isnull().sum())

df = df.fillna(0)

print("                      ----------------NEW CSV FILE WITH NULL VALUES FILLED WITH ZEROES-----------------                 ")
print(df)
print("                      ----------------NUMBER OF NULL VALUES IN EACH COLUMNS (UPDATED)-----------------                 ")
print(df.isnull().sum())

df.to_csv('Q2-Dataset_new.csv')