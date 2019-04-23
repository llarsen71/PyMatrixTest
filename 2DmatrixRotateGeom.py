import pylab as plt
import numpy as np
from math import pi, cos, sin

def ortho(degrees):
  """
  Return a 2D rotation matrix that rotates by the specified degrees.
  """
  a = degrees*pi/180
  return np.matrix([[cos(a),sin(a)],[-sin(a),cos(a)]])

A = np.matrix([[10,0],[0,0.01]])

degrees = []
cosAngle = []
lenAvg = []
lenMax = []
lenMin = []
lenDiff = []

for deg in range(0,361):
  degrees.append(deg)

  # Rotation Matrix
  P = ortho(deg)

  # Rotated Matrix
  Ar = P*A*P.T

  # Cosine of angle between Matrix column vectors
  cosAngle.append(float(Ar[0,:] * Ar[1,:].T)/(float(Ar[0,:]*Ar[0,:].T)**0.5*float(Ar[1,:]*Ar[1,:].T)**0.5))

  # Average length of vectors in matrix
  lenAvg.append((float(Ar[0,:]*Ar[0,:].T)**0.5+float(Ar[1,:]*Ar[1,:].T)**0.5)/2)

  # Maximum length of matrix vectors
  lenMax.append(max(float(Ar[0,:]*Ar[0,:].T)**0.5,float(Ar[1,:]*Ar[1,:].T)**0.5))

  # Minimum length of matrix vectors
  lenMin.append(min(float(Ar[0,:]*Ar[0,:].T)**0.5,float(Ar[1,:]*Ar[1,:].T)**0.5))

  # Difference in length of vectors
  lenDiff.append(float(Ar[0,:]*Ar[0,:].T)**0.5-float(Ar[1,:]*Ar[1,:].T)**0.5)

plt.plot(degrees, cosAngle)
plt.ylabel("Cos of angle between vectors")
plt.xlabel("Degrees")

plt.figure()
plt.plot(degrees, lenAvg)
plt.plot(degrees, lenMax)
plt.plot(degrees, lenMin)
plt.ylabel("Vec. Avg Len, Max Len, Min Len")
plt.xlabel("Degrees")

plt.figure()
plt.plot(degrees, lenDiff)
plt.ylabel("Vec")
plt.xlabel("Degrees")

plt.show()
