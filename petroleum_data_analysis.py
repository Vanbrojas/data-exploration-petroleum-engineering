
import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset: Oil production (barrels per day) by country
data = {
    'Country': ['USA', 'Saudi Arabia', 'Russia', 'Canada', 'China'],
    'Production_bpd': [11000000, 10000000, 9500000, 4500000, 3900000]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Oil Production Data (barrels per day):")
print(df)

# Basic statistics
print("\nBasic Statistics:")
print(df['Production_bpd'].describe())

# Plotting
plt.figure(figsize=(8, 5))
plt.bar(df['Country'], df['Production_bpd'], color='skyblue')
plt.xlabel('Country')
plt.ylabel('Production (bpd)')
plt.title('Oil Production by Country')
plt.grid(True)
plt.tight_layout()

# Save the plot as an image
plt.savefig('oil_production_chart.png')

# Show the plot
plt.show()