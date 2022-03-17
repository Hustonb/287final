# Import pandas
import pandas as pd

# Read in CSV from https://www.basketball-reference.com/leagues/NBA_2021_per_game.html
df = pd.read_csv("basketballref2020.csv")

# Print the first 5 rows
#print(df.head())

# Get the summary
#print(df.describe())

# Print just the player column
#print(df["Player"])

# Create a new dataframe that is a copy of the old one
dfNew = df;

# Create a new column in the new dataframe that is just the player's name (without the 9 character ID code)
dfNew['Name'] = dfNew['Player'].str[:-10]
#print(dfNew.iloc[20:21, 20:])
#print(dfNew.info())

# Create a new dataframe that reorders the columns in the old dataframe and only includes 9 defensive stats
dfReordered = dfNew[['Rk', 'Name', 'Age', 'Tm', 'ORB', 'DRB', 'TRB', 'STL', 'BLK']]
print(dfReordered.head())

# See a list of the column names
cols = list(dfReordered.columns.values)
print(cols)


