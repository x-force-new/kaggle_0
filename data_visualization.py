import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (assuming there is a dataset.csv file in the current directory)
df = pd.read_csv('salaries.csv')

# Display the first few rows of the dataframe
print(df.head())

# Example visualization: Plotting the distribution of salaries in USD
plt.figure(figsize=(10, 6))
plt.hist(df['salary_in_usd'], bins=30, edgecolor='black')
plt.title('Distribution of Salaries in USD')
plt.xlabel('Salary in USD')
plt.ylabel('Frequency')
plt.show()
