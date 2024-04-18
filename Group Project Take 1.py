import pandas as pd
import matplotlib.pyplot as plt

# Load the data
batting_df = pd.read_excel('C:/Users/WaltersJ07/Downloads/Batting.xlsx')
people_df = pd.read_excel('C:/Users/WaltersJ07/Downloads/People.xlsx')

# Join the data on the playerID
df = pd.merge(batting_df, people_df, on='playerID')

# Calculate the players' ages
df['age'] = df['yearID'] - df['birthYear']

# Filter out records where 'AB' is 0 and 'age' is not within a reasonable range
df = df[(df['AB'] >= 100) & (df['age'] >= 20) & (df['age'] <= 38)]

# Set a threshold for the minimum number of players per age group
min_players_per_age = 200

# Group the data by age and sum up 'H' and 'AB' for each age
grouped_by_age = df.groupby('age').agg(
    total_hits=('H', 'sum'),
    total_at_bats=('AB', 'sum'),
    num_players=('playerID', 'nunique')
)

# Filter out age groups that do not meet the minimum player threshold
grouped_by_age = grouped_by_age[grouped_by_age['num_players'] >= min_players_per_age]

# Calculate the weighted batting average for each age
grouped_by_age['weighted_batting_average'] = grouped_by_age['total_hits'] / grouped_by_age['total_at_bats']

# Find the age with the highest weighted batting average
peak_batting_age = grouped_by_age['weighted_batting_average'].idxmax()

print(f"The age with the highest weighted batting average is {peak_batting_age}.")

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(grouped_by_age.index, grouped_by_age['weighted_batting_average'])
plt.scatter(peak_batting_age, grouped_by_age['weighted_batting_average'].max(), color='red')  # mark the peak
plt.xlabel('Age')
plt.ylabel('Weighted Batting Average')
plt.title('Weighted Batting Average by Age')
plt.grid(True)
plt.show()
