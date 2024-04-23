import pandas as pd
import matplotlib.pyplot as plt

# Load the data
batting_df = pd.read_excel('C:/Users/WaltersJ07/Downloads/Batting.xlsx')
people_df = pd.read_excel('C:/Users/WaltersJ07/Downloads/People.xlsx')

# Join the data on the playerID
df = pd.merge(batting_df, people_df, on='playerID')

# Calculate the players' birthdates
df['age'] = df['yearID'] - df['birthYear']

# Filter out records where 'AB' is 0 and 'exact_age' is not within a reasonable range
df = df[(df['AB'] >= 300) & (df['age'] >= 20) & (df['age'] <= 38)]

# Calculate the batting average for each player at each age
df['batting_average'] = df['H'] / df['AB']

# Group the data by age and calculate the mean batting average at each age
mean_batting_average_by_age = df.groupby('age')['batting_average'].mean()

# Create a scatter plot of each player's batting average at each age
plt.scatter(df['age'], df['batting_average'], alpha=0.5)

# Overlay a line graph of the mean batting average at each age
plt.plot(mean_batting_average_by_age.index, mean_batting_average_by_age.values, color='red')

plt.xlabel('Age')
plt.ylabel('Batting Average')
plt.title('Batting Average by Age')
plt.show()