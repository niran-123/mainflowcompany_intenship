import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("C:\intenship\task 1 data analysis and data science\main.csv") 

# Data Exploration
print("Initial Data:")
print(data.head())
print("\nMissing Values:")
print(data.isnull().sum())
print("\nData Types:")
print(data.dtypes)
print("\nDataset Shape:", data.shape)

# Data Cleaning
# Assuming no missing values for simplicity
# data = data.fillna(data['G3'].median())  # Replace with median if needed
data = data.drop_duplicates()

# Data Analysis
average_score = data['G3'].mean()
print(f"\nAverage score in math (G3): {average_score:.2f}")

above_15 = data[data['G3'] > 15]
num_students_above_15 = len(above_15)
print(f"Number of students who scored above 15 in G3: {num_students_above_15}")

correlation = data['studytime'].corr(data['G3'])
print(f"Correlation between study time and final grade: {correlation:.2f}")

average_score_by_gender = data.groupby('sex')['G3'].mean()
print("\nAverage final grade by gender:\n", average_score_by_gender)

# Data Visualization
plt.figure(figsize=(8, 6))
plt.hist(data['G3'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel("Final Grade (G3)")
plt.ylabel("Number of Students")
plt.title("Distribution of Final Grades")
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='studytime', y='G3', data=data)
plt.xlabel("Study Time (hours/week)")
plt.ylabel("Final Grade (G3)")
plt.title("Study Time vs. Final Grade")
plt.show()

average_score_by_gender.plot(kind='bar', color=['lightblue', 'pink'])
plt.xlabel("Gender")
plt.ylabel("Average Final Grade (G3)")
plt.title("Average Final Grade by Gender")
plt.show()
