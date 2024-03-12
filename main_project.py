import pandas as pd
import random

# Generating random data for the Diabetes CSV file
data = {
    'age': [random.randint(20, 80) for i in range(1000)],
    'gender': [random.choice(['Male', 'Female']) for i in range(1000)],
    'bmi': [round(random.uniform(18.5, 40.0), 2) for i in range(1000)],
    'bp': [random.randint(80, 130) for i in range(1000)],
    's1': [random.uniform(0, 200) for i in range(1000)],
    's2': [random.uniform(0, 200) for i in range(1000)],
    's3': [random.uniform(0, 200) for i in range(1000)],
    's4': [random.uniform(0, 200) for i in range(1000)],
    's5': [random.uniform(0, 200) for i in range(1000)],
    's6': [random.uniform(0, 200) for i in range(1000)],
    'progression': [random.randint(0, 2) for i in range(1000)],
}

# Creating the dataframe and saving the data to a CSV file
df = pd.DataFrame(data)
df.to_csv('Diabetes_Random Forest.csv', index=True)

# Reading the data from the CSV file into a pandas dataframe
df = pd.read_csv('Diabetes_Random Forest.csv')

# Printing the first 5 rows of the data
print(df.head())
