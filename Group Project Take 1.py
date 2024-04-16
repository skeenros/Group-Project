import pandas as pd

# Load the data
batting_df = pd.read_excel('C:/Users/WaltersJ07/Downloads/Batting.xlsx')
pitching_df = pd.read_excel('C:/Users/WaltersJ07/Downloads/Pitching.xlsx')
people_df = pd.read_excel('C:/Users/WaltersJ07/Downloads/People.xlsx')

# Calculate the batting average for each player in the batting dataframe
batting_df['batting_average'] = batting_df['H'] / batting_df['AB']

# Join the data on the playerID
df = pd.merge(batting_df, people_df, on='playerID')
df = pd.merge(df, pitching_df, on=['playerID', 'yearID'])

# Calculate the players' ages
df['age'] = df['yearID'] - df['birthYear']

# Group the data by age and calculate the average batting average in each age group
average_batting_by_age = df.groupby('age')['batting_average'].mean()

# Find the age with the highest average batting average
peak_batting_age = average_batting_by_age.idxmax()

print(f'The age with the highest average batting average is {peak_batting_age}.')