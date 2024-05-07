import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# Load the dataset
data = pd.read_csv('salaries.csv')

# Display the first few rows of the dataset
print(data.head())

# Save the script and check if we need to install any libraries
# Preprocessing
data = pd.get_dummies(data, columns=['experience_level', 'employment_type', 'job_title', 'salary_currency', 'employee_residence', 'company_location', 'company_size'], drop_first=True)

# Handle missing values if any
data = data.dropna()

# Define the target variable and features
X = data.drop(columns=['salary', 'salary_in_usd'])
y = data['salary_in_usd']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)

# Save the model performance to a text file
with open('model_performance.txt', 'w') as f:
    f.write(f'Mean Squared Error: {mse}\n')

print('Model evaluation completed and saved to model_performance.txt')
