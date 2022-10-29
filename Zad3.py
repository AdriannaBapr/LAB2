# %%
import numpy as np
import pandas as pd
import numpy.ma as ma

# use pandas to extract rainfall inches as a NumPy array
rainfall = pd.read_csv('Seattle2014.csv')['PRCP'].values
# zmieniamy na inches
inches = rainfall / 254.0  # 1/10mm -> inches
inches.shape
inches

# %%
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn; seaborn.set()  # set plot styles
plt.hist(inches, 40);

# %%
#without rain
array1 = inches[inches==0]
a1 = array1.size

#with rain
array2 = inches[inches>0]
a2 = array2.size

#more than 0.5 inches
array3 = inches[inches>0.5]
a3 = array3.size

#less than 0.2 but with rain
array4 = array2[(array2<0.2)]
a4 = array4.size

# %%
print("Number days without rain:      ", a1)
print("Number days with rain:         ", a2)
print("Days with more than 0.5 inches:", a3)
print("Rainy days with < 0.2 inches  :", a4)

# %%
#array with rainy days
array5 = ma.masked_where(inches == 0, inches)
median1 = np.ma.median(array5)

#array with indexes
ind = np.arange(365)
#mask 1
array_mask1 = ma.masked_outside(ind, 172, 262)
mask1 = array_mask1.mask
#array with summer days
array6 = ma.masked_array(inches, mask1)
median2 = np.ma.median(array6)

#maxixmum in summer
max1 = np.ma.max(array6)

#mask 2
array_mask2 = ma.masked_inside(ind, 172, 262)
mask2 = array_mask2.mask
#array with not summer days
array7 = ma.masked_array(inches, mask2)
array7
#maximum not in summer
max2 = np.ma.max(array7)

#median not in summer
median3 = np.ma.median(array7)
median3

# %%
print("Median precip on rainy days in 2014 (inches):   ", median1)
print("Median precip on summer days in 2014 (inches):  ", median2)
print("Maximum precip on summer days in 2014 (inches): ", max1)
print("Maximum precip on non=summer days in 2014 (inches): ", max2)
print("Median precip on non-summer rainy days (inches):", median3)
# %%
