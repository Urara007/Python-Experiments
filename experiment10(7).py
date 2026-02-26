import matplotlib.pyplot as plt
import numpy as np

# 1. Prepare Data
x = np.arange(1, 11)
y = [10, 24, 36, 40, 52, 61, 75, 88, 92, 110]
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 15, 7, 10, 12]
data_dist = np.random.normal(50, 10, 1000) # Data for Histogram

# 2. Create a figure with 2x2 subplots
plt.figure(figsize=(12, 8))

# Subplot 1: Line Plot (Shows Trends)
plt.subplot(2, 2, 1)
plt.plot(x, y, color='blue', marker='o', linestyle='-', linewidth=2)
plt.title("Line Plot: Trend Over Time")
plt.xlabel("Time")
plt.ylabel("Value")
plt.grid(True)

# Subplot 2: Bar Chart (Compares Categories)
plt.subplot(2, 2, 2)
plt.bar(categories, values, color='teal')
plt.title("Bar Chart: Category Comparison")
plt.xlabel("Category")
plt.ylabel("Count")

# Subplot 3: Histogram (Shows Distribution)
plt.subplot(2, 2, 3)
plt.hist(data_dist, bins=20, color='salmon', edgecolor='black')
plt.title("Histogram: Data Distribution")
plt.xlabel("Score Ranges")
plt.ylabel("Frequency")

# Subplot 4: Scatter Plot (Shows Relationships)
plt.subplot(2, 2, 4)
plt.scatter(x, y, color='purple', s=100, alpha=0.6)
plt.title("Scatter Plot: X vs Y Relationship")
plt.xlabel("Variable X")
plt.ylabel("Variable Y")

# 3. Adjust layout and display
plt.tight_layout()
plt.show()