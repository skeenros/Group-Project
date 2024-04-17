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
df = df[(df['AB'] != 0) & (df['age'] >= 19) & (df['age'] <= 45)]

# Group the data by age and sum up 'H' and 'AB' for each age
sums_by_age = df.groupby('age')[['H', 'AB']].sum()

# Calculate the batting average for each age
sums_by_age['batting_average'] = sums_by_age['H'] / sums_by_age['AB']

# Find the age with the highest average batting average
peak_batting_age = sums_by_age['batting_average'].idxmax()

print(f'The age with the highest average batting average is {peak_batting_age}.')

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(sums_by_age.index, sums_by_age['batting_average'])
plt.scatter(peak_batting_age, sums_by_age['batting_average'].max(), color='red')  # mark the peak
plt.xlabel('Age')
plt.ylabel('Average Batting Average')
plt.title('Average Batting Average by Age')
plt.grid(True)
plt.show()