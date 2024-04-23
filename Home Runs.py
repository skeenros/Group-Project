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
df = df[(df['AB'] >= 300) & (df['age'] >= 20) & (df['age'] <= 38)]

# Group the data by age and playerID and sum up 'HR' for each player at each age
grouped_by_age_and_player = df.groupby(['age', 'playerID']).agg(
    total_home_runs=('HR', 'sum')
)

# Reset index to make 'age' and 'playerID' as columns again
grouped_by_age_and_player.reset_index(inplace=True)

# Create a scatter plot
plt.scatter(grouped_by_age_and_player['age'], grouped_by_age_and_player['total_home_runs'])
plt.xlabel('Age')
plt.ylabel('Home Runs')
plt.title('Home Runs by Age')
plt.show()