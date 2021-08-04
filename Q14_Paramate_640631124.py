''' Name: Paramate Phuengtrakul
    ID: 640631124 '''

import numpy as np
from scipy.linalg import solve

# Quiz14: Try this
A = np.array([[1., 2.], [3., 4.]])
b = np.array([1., 4.])
x = solve(A, b)
print('x1 and x2  =', x, 'respectively.')

# Quiz15: Create a Matrix X_4x3
X = np.array([[1., 2., 3.],
             [4., 5., 6.],
             [7., 8., 9.],
             [10., 11., 12.]])

print(X[2, :]) # the row index number 2 is retrieved and all number in the row index 2 are totally grabed 
print(X[2:]) # the code retrieves the index of row number 2 to the last number index of the row which is number 3

# Quiz16: Create Matrix Aij

# rows(i) = 1,2,3,4,5,.., m =10
# cols(j) = 1,2,3,4,5,...,n=10
# i < j and j != m ==> A[i,j] = 0
# i = j and j = m ==> A[i,j] = 1
# else ==> A[i,j] = -1


#rows = 1
#cols = 1
#for i in range(2, 11):
m = 10
object_A = []
A_ij = np.zeros((m, m))


for i in range(m):
    for j in range(m):
        if i < j and j != m:
            A_ij[i, j] = 0
        elif i == j or j == m:
            A_ij[i, j] = 1
        else:
            A_ij[i, j] = -1

print(A_ij)
        






