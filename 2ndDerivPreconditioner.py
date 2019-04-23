import numpy as np
import pylab as plt
from math import sin

dot = np.dot

def makeA(n):
  """
  Make the A matrix for the discrete derivative d2x/dt2.
  Include Dirchlet boundary conditions.
  
  n - The size of the matrix.
  """
  A = []
  row = [0]*n
  row[0] = 1
  A.append(row)
  
  for i in range(n-2):
    row = [0]*n
    row[i:i+3] = [1,-2,1]
    A.append(row)
  
  row = [0]*n
  row[n-1] = 1
  A.append(row)
  return np.array(A)

n = 60
A = makeA(n)

# Start with identity matrix as preconditioner base
P = np.eye(n)

# Calculate the orthogonality pattern of adjacent columns.
# Create a preconditioner that orthoginalizes the middle row.
u, v, w = A[1,:], A[2,:], A[3,:]
vm = dot(v, v)**0.5
um = dot(v,u)/vm
V = v - u*um
wm = dot(V,w)/vm
V = V - w*wm
Vm = vm/dot(V,V)**0.5
s = np.array([-um, 1, -wm])*Vm
#print(s)

# Modify the preconditioner
for i in range(2, n-2, 2):
  P[i,i-1:i+2] = s

Ad = np.linalg.det(A)
PAd = np.linalg.det(dot(P,A))
A = dot(P,A)

v = np.linalg.eig(A)
eig = sorted([abs(v1) for v1 in v[0]])
for val in eig:
  print(val)
print("")
print(Ad)
print(PAd)

plt.plot(eig,'o')

dx = 12/(n-1)
b = [sin(i*dx)*dx**2 for i in range(n)]
b[0] = 1
b[-1] = 10

b = dot(P,b)

x = np.linalg.solve(A,b)
plt.plot(x)
plt.show()