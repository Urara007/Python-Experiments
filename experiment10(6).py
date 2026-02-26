import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Part A: Replace Missing Values ---
df_missing = pd.DataFrame({'score': [12.5, np.nan, 16.5, np.nan, 9]})
# Fill NaN with 0 or the mean
df_filled = df_missing.fillna(0)
print("DataFrame after replacing missing values:\n", df_filled)

# --- Part B: Matplotlib Visualizations ---
x = [1, 2, 3, 4, 5]
y = [10, 24, 36, 40, 52]

plt.figure(figsize=(10, 6))

# Line Plot
plt.subplot(1, 3, 1)
plt.plot(x, y, color='blue', marker='o')
plt.title("Line Plot")

# Bar Plot
plt.subplot(1, 3, 2)
plt.bar(x, y, color='green')
plt.title("Bar Chart")

# Scatter Plot
plt.subplot(1, 3, 3)
plt.scatter(x, y, color='red')
plt.title("Scatter Plot")

plt.tight_layout()
plt.show()