# %%
import numpy as np
import pandas as pd
data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])
print(heights)

# %%
mean = np.mean(heights)
std = np.std(heights)
min = np.min(heights)
max = np.max(heights)
q1 = np.quantile(heights, 0.25)
median = np.median(heights)
q3 = np.quantile(heights, 0.75)

# %%
print("Mean height:       ", mean)
print("Standard deviation:", std)
print("Minimum height:    ", min)
print("Maximum height:    ", max)
print("25th percentile:   ", q1)
print("Median:            ", median)
print("75th percentile:   ", q3)
# %%
