# pip install pandas
import pandas as pd

# Read the csv file
df = pd.read_csv('data.csv')

# print first 5 rows of data
# print(df.head())

# print last 5 rows
# print(df.tail())


# Check for missing values
print(df.isnull().sum())

# Get some initial statistics
print(df.describe())

# Provide variable descriptions
print(df.info())

# Check the dimensions of the DataFrame
print(f'The DataFrame has {df.shape[0]} rows and {df.shape[1]} columns.')