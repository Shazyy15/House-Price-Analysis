# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the CSV file
df = pd.read_csv('house_price_data.csv')

# Display the first few rows of the dataset
print("Dataset:")
print(df.head())

# --- Data Analysis ---

# 1. Correlation between numerical features
correlation = df.corr()
print("\nCorrelation between features:")
print(correlation)

# 2. Distribution of House Prices (Histogram)
plt.figure(figsize=(10, 6))
plt.hist(df['Price'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of House Prices (Data Analyst: Shazil Shahid)', fontsize=14, fontweight='bold')
plt.xlabel('Price ($)')
plt.ylabel('Frequency')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 3. Box Plot: Price by Location
plt.figure(figsize=(10, 6))
locations = df['Location'].unique()
prices_by_location = [df[df['Location'] == loc]['Price'] for loc in locations]
plt.boxplot(prices_by_location, labels=locations)
plt.title('House Prices by Location (Data Analyst: Shazil Shahid)', fontsize=14, fontweight='bold')
plt.xlabel('Location')
plt.ylabel('Price ($)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 4. Scatter Plot: House Size vs. Price
plt.figure(figsize=(10, 6))
plt.scatter(df['Size'], df['Price'], c=df['Rooms'], cmap='viridis', s=100, edgecolor='black')
plt.colorbar(label='Number of Rooms')
plt.title('House Size vs. Price (Colored by Number of Rooms) (Data Analyst: Shazil Shahid)', fontsize=14, fontweight='bold')
plt.xlabel('Size (sq ft)')
plt.ylabel('Price ($)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 5. Bar Plot: Total Price per Location
plt.figure(figsize=(10, 6))
total_price_by_location = df.groupby('Location')['Price'].sum()
locations = total_price_by_location.index
prices = total_price_by_location.values
plt.bar(locations, prices, color='orange', edgecolor='black')
plt.title('Total House Prices by Location (Data Analyst: Shazil Shahid)', fontsize=14, fontweight='bold')
plt.xlabel('Location')
plt.ylabel('Total Price ($)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 6. Line Plot: Year Built vs. Price
plt.figure(figsize=(10, 6))
years = df.groupby('YearBuilt')['Price'].mean().index
avg_price_by_year = df.groupby('YearBuilt')['Price'].mean().values
plt.plot(years, avg_price_by_year, marker='o', color='green')
plt.title('Average House Prices Over the Years (Data Analyst: Shazil Shahid)', fontsize=14, fontweight='bold')
plt.xlabel('Year Built')
plt.ylabel('Average Price ($)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Display final results
print("\nTotal Price by Location:")
print(total_price_by_location)
