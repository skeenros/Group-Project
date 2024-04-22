import pandas as pd
import matplotlib.pyplot as plt

# Load the data
batting_df = pd.read_excel('C:/Users/WaltersJ07/Downloads/Batting.xlsx')
people_df = pd.read_excel('C:/Users/WaltersJ07/Downloads/People.xlsx')

# Join the data on the playerID
df = pd.merge(batting_df, people_df, on='playerID')

# Calculate the players' ages
df['age'] = df['yearID'] - df['birthYear']

# Filter out records where 'AB' is less than 200 and 'age' is not within a reasonable range
df = df[(df['AB'] >= 100) & (df['age'] >= 20) & (df['age'] <= 38)]

# Set a threshold for the minimum number of players per age group
min_players_per_age = 300

# Group the data by age and sum up 'HR' for each age and count the number of players
grouped_by_age = df.groupby('age').agg(
    total_home_runs=('HR', 'sum'),
    num_players=('playerID', 'nunique')
)

# Filter out age groups that do not meet the minimum player threshold
grouped_by_age = grouped_by_age[grouped_by_age['num_players'] >= min_players_per_age]

# Calculate the average home runs for each age
grouped_by_age['average_home_runs'] = grouped_by_age['total_home_runs'] / grouped_by_age['num_players']

# Find the age with the highest average home runs
peak_home_runs_age = grouped_by_age['average_home_runs'].idxmax()

print(f"The age with the highest average home runs is {peak_home_runs_age}.")

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(grouped_by_age.index, grouped_by_age['average_home_runs'])
plt.scatter(peak_home_runs_age, grouped_by_age['average_home_runs'].max(), color='red')  # mark the peak
plt.xlabel('Age')
plt.ylabel('Average Home Runs')
plt.title('Average Home Runs by Age')
plt.grid(True)
plt.show()