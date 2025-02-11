import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Create Inbuilt Data (Simulating a CSV File)
data = {
    "Order ID": [1001, 1002, 1003, 1004, 1005],
    "Product Category": ["Office Supplies", "Furniture", "Technology", "Furniture", "Office Supplies"],
    "Sales": [200.50, 1500.00, 300.00, 700.00, 50.00],
    "Profit": [50.00, -200.00, 80.00, 150.00, 10.00],
    "Quantity": [3, 2, 1, 5, 10],
    "Discount": [0.1, 0.2, 0.05, 0.15, 0.0],
    "Region": ["East", "West", "Central", "South", "East"],
    "Ship Mode": ["Standard", "First Class", "Same Day", "Second Class", "Standard"],
    "Customer Segment": ["Corporate", "Home Office", "Consumer", "Corporate", "Consumer"]
}

# Convert Dictionary to DataFrame
df = pd.DataFrame(data)

# Step 2: Data Cleaning
df.drop_duplicates(inplace=True)  # Remove Duplicates
df.fillna(df.median(numeric_only=True), inplace=True)  # Fill missing values with median

# Step 3: Handling Outliers using IQR
Q1 = df[["Sales", "Profit"]].quantile(0.25)
Q3 = df[["Sales", "Profit"]].quantile(0.75)
IQR = Q3 - Q1
df = df[~((df[["Sales", "Profit"]] < (Q1 - 1.5 * IQR)) | (df[["Sales", "Profit"]] > (Q3 + 1.5 * IQR))).any(axis=1)]

# Step 4: Statistical Summary
print("Dataset Summary:\n", df.describe())
# Select only numerical columns before computing correlation
numeric_df = df.select_dtypes(include=[np.number])  

# Now compute correlation
print("\nCorrelation Matrix:\n", numeric_df.corr())


# Step 6: Data Visualization
plt.figure(figsize=(10,5))
sns.histplot(df['Sales'], bins=10, kde=True)  # Histogram for Sales
plt.title("Sales Distribution")
plt.show()

plt.figure(figsize=(10,5))
sns.boxplot(x=df['Profit'])  # Boxplot for Profit
plt.title("Profit Boxplot")
plt.show()

plt.figure(figsize=(10,5))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')  # Heatmap of correlations
plt.title("Feature Correlation Heatmap")
plt.show()
