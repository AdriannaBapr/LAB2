# %%
import numpy as np

A = [0,3,2,5]
B = [0,3,1,4]

# sum = []
# for i in range(len(A)):
#   sum.append(A[i]+B[i])

sum=np.add(A, B)
sum

# %%
# sub = []
# for i in range(len(A)):
#   sub.append(B[i]-A[i])

sub=np.subtract(B, A)
sub

# %%
# mult = []
# for i in range(len(A)):
#   mult.append(4*A[i])

mult = np.multiply(A, 4)
mult

# %%
# sc = 0
# for i in range(len(A)):
#   sc += A[i]*B[i]

sc = np.dot(A, B)
sc

# %%
# x=0
# for i in range(len(B)):
#   x += B[i]**2

# result = x ** 0.5

l = np.linalg.norm(B)
l