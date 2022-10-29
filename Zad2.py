# %%
import numpy as np
import pandas as pd
data = np.genfromtxt('Zadanie_2.csv', delimiter=';')
data

# %%
w, v = np.linalg.eig(data)
print("Eigenvalues:",w)
print("Eigenvectors:",v)

# %%
det = np.linalg.det(data)
inv = np.linalg.inv(data)
print("det(A) =", det)
print("Inverse of A:", inv)
# %%
